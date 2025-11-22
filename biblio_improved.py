#!/usr/bin/env python3
"""
Système de recherche d'articles PDF avec nettoyage automatique
Supprime automatiquement de la base de données les articles dont le fichier n'existe plus
"""

import os
import json
import sqlite3
from pathlib import Path
import argparse
from typing import List, Dict, Optional
import hashlib
import subprocess
import re

# Installation requise : pip install PyPDF2 fuzzywuzzy python-levenshtein
try:
    import PyPDF2
    from fuzzywuzzy import fuzz, process
except ImportError:
    print("Erreur: Installez les dépendances avec:")
    print("pip install PyPDF2 fuzzywuzzy python-levenshtein")
    exit(1)

class BibliothequeArticles:
    def __init__(self, dossier_articles: str = None, db_path: str = None):
        # Chemins absolus vers le dossier LMA sur le Bureau
        base_dir = Path.home() / "Desktop" / "LMA"
        
        if dossier_articles is None:
            self.dossier_articles = base_dir / "articles"
        else:
            self.dossier_articles = Path(dossier_articles)
        
        if db_path is None:
            self.db_path = base_dir / "data" / "articles.db"
        else:
            self.db_path = Path(db_path)
        
        self.db_path.parent.mkdir(exist_ok=True, parents=True)
        self.init_database()
    
    def init_database(self):
        """Initialise la base de données SQLite"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                nom_fichier TEXT UNIQUE,
                titre TEXT,
                auteurs TEXT,
                annee INTEGER,
                mots_cles TEXT,
                contenu_extrait TEXT,
                hash_fichier TEXT,
                a_lire BOOLEAN DEFAULT 0,
                date_ajout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def verifier_fichier_existe(self, nom_fichier: str) -> bool:
        """Vérifie si le fichier PDF existe dans le dossier articles"""
        if not self.dossier_articles.exists():
            return False
        
        # Recherche récursive du fichier
        for pdf_file in self.dossier_articles.rglob(nom_fichier):
            if pdf_file.exists():
                return True
        return False
    
    def nettoyer_articles_manquants(self) -> int:
        """
        Supprime de la base de données tous les articles dont le fichier n'existe plus
        Retourne le nombre d'articles supprimés
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Récupérer tous les articles
        cursor.execute("SELECT id, nom_fichier FROM articles")
        articles = cursor.fetchall()
        
        articles_supprimes = 0
        for article_id, nom_fichier in articles:
            if not self.verifier_fichier_existe(nom_fichier):
                cursor.execute("DELETE FROM articles WHERE id = ?", (article_id,))
                articles_supprimes += 1
                print(f"  ✗ Supprimé de la base: {nom_fichier} (fichier introuvable)")
        
        conn.commit()
        conn.close()
        
        return articles_supprimes
    
    def extraire_texte_pdf(self, chemin_pdf: Path) -> str:
        """Extrait le texte d'un fichier PDF"""
        try:
            with open(chemin_pdf, 'rb') as fichier:
                lecteur = PyPDF2.PdfReader(fichier)
                texte = ""
                for page in lecteur.pages:
                    page_text = page.extract_text()
                    if page_text:  # Vérification que la page contient du texte
                        texte += page_text + "\n"
                return texte
        except Exception as e:
            print(f"Erreur lors de l'extraction de {chemin_pdf}: {e}")
            return ""
    
    def calculer_hash(self, chemin_fichier: Path) -> str:
        """Calcule le hash MD5 d'un fichier"""
        hash_md5 = hashlib.md5()
        with open(chemin_fichier, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def extraire_metadonnees(self, texte: str, nom_fichier: str) -> Dict[str, str]:
        """Extrait les métadonnées du nom de fichier et du contenu"""
        # Retirer l'extension .pdf
        nom_base = nom_fichier.replace('.pdf', '')
        
        # Pattern pour nom_fichier: Auteur_Année_Titre (plus flexible)
        patterns = [
            r'^([^_]+)_(\d{4})_(.+)$',  # Auteur_Année_Titre
            r'^(.+)_(\d{4})_([^_]+)$',  # Titre_Année_Auteur
            r'^(\d{4})_([^_]+)_(.+)$',  # Année_Auteur_Titre
        ]
        
        for pattern in patterns:
            match = re.match(pattern, nom_base)
            if match:
                if pattern == patterns[0]:  # Auteur_Année_Titre
                    auteur = match.group(1).replace('_', ' ')
                    annee = int(match.group(2))
                    titre = match.group(3).replace('_', ' ')
                elif pattern == patterns[1]:  # Titre_Année_Auteur
                    titre = match.group(1).replace('_', ' ')
                    annee = int(match.group(2))
                    auteur = match.group(3).replace('_', ' ')
                elif pattern == patterns[2]:  # Année_Auteur_Titre
                    annee = int(match.group(1))
                    auteur = match.group(2).replace('_', ' ')
                    titre = match.group(3).replace('_', ' ')
                
                return {
                    'titre': titre[:200],
                    'auteurs': auteur[:200],
                    'annee': annee
                }
        
        # Fallback si le pattern ne correspond pas
        parts = nom_base.split('_')
        if len(parts) >= 3:
            auteur = parts[0]
            # Chercher une année dans les premières parties
            annee = None
            for part in parts[1:3]:
                if part.isdigit() and len(part) == 4 and 1990 <= int(part) <= 2030:
                    annee = int(part)
                    break
            if annee is None:
                annee = 2024  # Année par défaut
            titre = '_'.join(parts[2:]).replace('_', ' ')
        else:
            auteur = "Auteur inconnu"
            annee = 2024
            titre = nom_base.replace('_', ' ')
        
        # Essayer d'extraire plus d'infos du contenu si disponible
        if texte and len(texte) > 50:
            # Chercher une année dans le texte si pas trouvée
            if annee == 2024:
                annees_trouvees = re.findall(r'\b(19[9]\d|20[0-3]\d)\b', texte[:2000])
                if annees_trouvees:
                    annee = int(annees_trouvees[0])
            
            # Améliorer le titre si c'est juste le nom de fichier
            if titre == nom_base.replace('_', ' '):
                lignes = texte.split('\n')[:5]
                for ligne in lignes:
                    ligne = ligne.strip()
                    if 10 < len(ligne) < 150 and not re.search(r'(www\.|http|@)', ligne.lower()):
                        titre = ligne
                        break
        
        return {
            'titre': titre[:200],
            'auteurs': auteur[:200],
            'annee': annee
        }
    
    def indexer_article(self, chemin_pdf: Path):
        """Indexe un article PDF dans la base de données"""
        if not chemin_pdf.exists() or chemin_pdf.suffix.lower() != '.pdf':
            return False
        
        hash_fichier = self.calculer_hash(chemin_pdf)
        
        # Vérifier si déjà indexé
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM articles WHERE hash_fichier = ?", (hash_fichier,))
        if cursor.fetchone():
            conn.close()
            return False  # Déjà indexé
        
        # Extraire le contenu
        texte = self.extraire_texte_pdf(chemin_pdf)
        # Même si le texte est vide, on indexe quand même avec les métadonnées du nom
        
        # Extraire les métadonnées
        metadata = self.extraire_metadonnees(texte, chemin_pdf.name)
        
        # Sauvegarder en base
        try:
            cursor.execute('''
                INSERT INTO articles (nom_fichier, titre, auteurs, annee, contenu_extrait, hash_fichier)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                str(chemin_pdf.name),
                metadata['titre'],
                metadata['auteurs'],
                metadata['annee'],
                texte[:5000],  # Garde les 5000 premiers caractères
                hash_fichier
            ))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erreur lors de l'indexation de {chemin_pdf.name}: {e}")
            conn.close()
            return False
    
    def indexer_dossier(self, nettoyer_avant: bool = True):
        """
        Indexe tous les PDFs du dossier et sous-dossiers
        Si nettoyer_avant=True, supprime d'abord les entrées de fichiers manquants
        """
        if not self.dossier_articles.exists():
            print(f"Le dossier {self.dossier_articles} n'existe pas.")
            return
        
        # Nettoyage automatique avant indexation
        if nettoyer_avant:
            print("\n🧹 Nettoyage de la base de données...")
            supprimes = self.nettoyer_articles_manquants()
            if supprimes > 0:
                print(f"  • {supprimes} article(s) supprimé(s) (fichiers manquants)")
            else:
                print("  • Aucun fichier manquant détecté")
        
        # Recherche récursive avec rglob au lieu de glob
        fichiers_pdf = list(self.dossier_articles.rglob("*.pdf"))
        print(f"\n📑 Indexation de {len(fichiers_pdf)} fichiers PDF trouvés (y compris sous-dossiers)...")
        
        nouveaux = 0
        echecs = 0
        for pdf in fichiers_pdf:
            try:
                if self.indexer_article(pdf):
                    nouveaux += 1
                    print(f"  ✓ {pdf.name}")
                else:
                    print(f"  - {pdf.name} (déjà indexé)")
            except Exception as e:
                echecs += 1
                print(f"  ✗ {pdf.name} (erreur: {e})")
        
        print(f"\n📊 Résumé:")
        print(f"  • {nouveaux} nouveaux articles indexés")
        print(f"  • {echecs} échecs")
        print(f"  • {len(fichiers_pdf)} fichiers traités au total")
    
    def rechercher(self, requete: str, limite: int = None) -> List[Dict]:
        """Recherche des articles par titre, auteurs ou contenu"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if limite:
            cursor.execute('''
                SELECT nom_fichier, titre, auteurs, annee, date_ajout, a_lire
                FROM articles
                WHERE titre LIKE ? OR auteurs LIKE ? OR contenu_extrait LIKE ?
                ORDER BY annee DESC, date_ajout DESC
                LIMIT ?
            ''', (f'%{requete}%', f'%{requete}%', f'%{requete}%', limite))
        else:
            cursor.execute('''
                SELECT nom_fichier, titre, auteurs, annee, date_ajout, a_lire
                FROM articles
                WHERE titre LIKE ? OR auteurs LIKE ? OR contenu_extrait LIKE ?
                ORDER BY annee DESC, date_ajout DESC
            ''', (f'%{requete}%', f'%{requete}%', f'%{requete}%'))
        
        resultats = []
        for row in cursor.fetchall():
            # Vérifier que le fichier existe toujours
            if self.verifier_fichier_existe(row[0]):
                resultats.append({
                    'fichier': row[0],
                    'titre': row[1],
                    'auteurs': row[2],
                    'annee': row[3],
                    'date': row[4],
                    'a_lire': bool(row[5]) if len(row) > 5 else False
                })
        
        conn.close()
        return resultats
    
    def lister_articles(self, limite: int = None) -> List[Dict]:
        """Liste tous les articles indexés dont le fichier existe"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if limite:
            cursor.execute('''
                SELECT nom_fichier, titre, auteurs, annee, date_ajout, a_lire
                FROM articles
                ORDER BY annee DESC, date_ajout DESC
                LIMIT ?
            ''', (limite,))
        else:
            cursor.execute('''
                SELECT nom_fichier, titre, auteurs, annee, date_ajout, a_lire
                FROM articles
                ORDER BY annee DESC, date_ajout DESC
            ''')
        
        resultats = []
        for row in cursor.fetchall():
            # Vérifier que le fichier existe toujours
            if self.verifier_fichier_existe(row[0]):
                resultats.append({
                    'fichier': row[0],
                    'titre': row[1],
                    'auteurs': row[2],
                    'annee': row[3],
                    'date': row[4],
                    'a_lire': bool(row[5]) if len(row) > 5 else False
                })
        
        conn.close()
        return resultats
    
    def compter_articles(self) -> int:
        """Compte le nombre total d'articles indexés dont le fichier existe"""
        articles = self.lister_articles()
        return len(articles)
    
    def marquer_a_lire(self, nom_fichier: str, a_lire: bool = True):
        """Marque ou démarque un article comme à lire"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE articles 
            SET a_lire = ? 
            WHERE nom_fichier = ?
        ''', (1 if a_lire else 0, nom_fichier))
        conn.commit()
        conn.close()
    
    def lister_a_lire(self) -> List[Dict]:
        """Liste tous les articles marqués comme à lire dont le fichier existe"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT nom_fichier, titre, auteurs, annee, date_ajout, a_lire
            FROM articles
            WHERE a_lire = 1
            ORDER BY annee DESC, date_ajout DESC
        ''')
        
        resultats = []
        for row in cursor.fetchall():
            # Vérifier que le fichier existe toujours
            if self.verifier_fichier_existe(row[0]):
                resultats.append({
                    'fichier': row[0],
                    'titre': row[1],
                    'auteurs': row[2],
                    'annee': row[3],
                    'date': row[4],
                    'a_lire': True
                })
        
        conn.close()
        return resultats
    
    def obtenir_statut_lecture(self, nom_fichier: str) -> bool:
        """Vérifie si un article est marqué comme à lire"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT a_lire FROM articles WHERE nom_fichier = ?', (nom_fichier,))
        result = cursor.fetchone()
        conn.close()
        return bool(result[0]) if result else False

def main():
    parser = argparse.ArgumentParser(description="Système de gestion d'articles PDF")
    parser.add_argument('--dossier', '-d', default='articles', 
                       help='Dossier contenant les articles PDF')
    parser.add_argument('--indexer', '-i', action='store_true',
                       help='Indexer tous les PDFs du dossier')
    parser.add_argument('--nettoyer', '-n', action='store_true',
                       help='Nettoyer la base de données (supprimer les entrées de fichiers manquants)')
    parser.add_argument('--rechercher', '-r', type=str,
                       help='Rechercher un article')
    parser.add_argument('--lister', '-l', action='store_true',
                       help='Lister tous les articles')
    parser.add_argument('--limite', type=int,
                       help='Limiter le nombre de résultats')
    
    args = parser.parse_args()
    
    biblio = BibliothequeArticles(args.dossier)
    
    if args.nettoyer:
        print("\n🧹 Nettoyage de la base de données...")
        supprimes = biblio.nettoyer_articles_manquants()
        if supprimes > 0:
            print(f"\n✅ {supprimes} article(s) supprimé(s) de la base de données")
        else:
            print("\n✅ Aucun fichier manquant détecté")
        total = biblio.compter_articles()
        print(f"📚 Total d'articles dans la bibliothèque: {total}")
    
    elif args.indexer:
        biblio.indexer_dossier()
        total = biblio.compter_articles()
        print(f"\n📚 Total d'articles dans la bibliothèque: {total}")
    
    elif args.rechercher:
        print(f"\n🔍 Recherche: '{args.rechercher}'")
        print("=" * 50)
        
        resultats = biblio.rechercher(args.rechercher, args.limite)
        
        if resultats:
            print(f"Trouvé {len(resultats)} résultat(s):")
            for i, article in enumerate(resultats, 1):
                print(f"\n{i}. {article['titre']}")
                print(f"   📄 {article['fichier']}")
                print(f"   👤 {article['auteurs']}")
                print(f"   📅 {article['annee']}")
        else:
            print("Aucun article trouvé.")
    
    elif args.lister:
        print("\n📚 Articles indexés:")
        print("=" * 50)
        
        total = biblio.compter_articles()
        articles = biblio.lister_articles(args.limite)
        
        if args.limite:
            print(f"Affichage des {min(len(articles), args.limite)} premiers articles sur {total} total:")
        else:
            print(f"Affichage de tous les {len(articles)} articles:")
        
        for i, article in enumerate(articles, 1):
            print(f"\n{i}. {article['titre']}")
            print(f"   📄 {article['fichier']}")
            print(f"   👤 {article['auteurs']}")
            print(f"   📅 {article['annee']}")
    
    else:
        # Affichage par défaut
        total = biblio.compter_articles()
        print(f"\n📚 Bibliothèque d'articles PDF")
        print("=" * 30)
        print(f"Total d'articles indexés: {total}")
        print("\nUtilisez --help pour voir les options disponibles.")

if __name__ == "__main__":
    main()