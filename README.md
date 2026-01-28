# 🇲🇦 LMA - Library Management App

> Gestionnaire de bibliothèque d'articles PDF avec lecteur intégré et annotations intelligentes

## 📖 Description

**LMA** (Library Management App) est une application de gestion de bibliothèque d'articles scientifiques en PDF. Elle vous permet d'**organiser**, **rechercher** et **annoter** vos articles académiques facilement.

### ✨ Fonctionnalités

#### 📚 Gestion de Bibliothèque
- **Indexation automatique** de vos PDFs
- **Base de données** SQLite ultra-rapide
- **Recherche instantanée** par titre, auteur ou contenu
- **Organisation** : marquer les articles à lire ou déjà lus
- **Nettoyage automatique** des fichiers manquants

#### 📖 Lecteur PDF Intégré
- **Navigation fluide** avec le trackpad MacBook
- **Zoom intelligent** avec raccourcis clavier
- **Surlignage** en 4 couleurs (Jaune, Rouge, Vert, Bleu)
- **Annotations persistantes** sauvegardées automatiquement
- **Recherche dans le PDF** avec navigation
- **Miniatures** pour aperçu rapide
- **Thème clair/sombre**

#### 🎨 Interface Moderne
- **Design inspiré des couleurs du Maroc** 🇲🇦
- Interface épurée et professionnelle
- Tableau principal agrandi pour meilleure lisibilité
- Raccourcis clavier intuitifs

---

## 💻 Configuration Requise

### Système d'exploitation
- **macOS** 10.14+ (testé sur Monterey 12.7.6)
- **Linux** (Ubuntu, Debian, Fedora)
- **Windows** 10/11 (avec Python installé)

### Logiciels
- **Python 3.8+** (inclus sur macOS)
- **Terminal** (Applications > Utilitaires > Terminal)

---

## 🚀 Installation Complète via Terminal

### Étape 1 : Créer la Structure

Ouvrez le **Terminal** et copiez-collez ces commandes :

```bash
# Créer le dossier LMA sur le Bureau
mkdir -p ~/Desktop/LMA/scripts
mkdir -p ~/Desktop/LMA/articles
mkdir -p ~/Desktop/LMA/data

# Aller dans le dossier
cd ~/Desktop/LMA
```

### Étape 2 : Télécharger les Fichiers

Téléchargez les 3 fichiers Python et placez-les dans `~/Desktop/LMA/scripts/` :
- `interface_pro.py`
- `biblio_improved.py`
- `lecteur_pdf_moderne.py`

**Via terminal (si vous avez git) :**
```bash
# Cloner le dépôt (remplacez par votre URL)
git clone https://github.com/votre-username/LMA.git ~/Desktop/LMA
cd ~/Desktop/LMA
```

### Étape 3 : Installer les Dépendances

```bash
# Installer les bibliothèques Python
pip3 install PyMuPDF pillow fuzzywuzzy python-levenshtein
```

**Si erreur "externally-managed-environment" sur macOS :**
```bash
pip3 install --break-system-packages PyMuPDF pillow fuzzywuzzy python-levenshtein
```

### Étape 4 : Vérifier l'Installation

```bash
# Vérifier que tout fonctionne
python3 -c "import fitz; import PIL; import fuzzywuzzy; print('✅ Installation réussie !')"
```

Si vous voyez **"✅ Installation réussie !"**, continuez !

### Étape 5 : Créer l'Alias LMA

Pour lancer l'application en tapant simplement `lma` dans le terminal :

```bash
# Ajouter l'alias à votre configuration shell
echo "alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'" >> ~/.zshrc

# Recharger la configuration
source ~/.zshrc
```

**Pour bash (Linux ou vieux macOS) :**
```bash
echo "alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'" >> ~/.bashrc
source ~/.bashrc
```

---

## 🎯 Lancer l'Application

### Méthode 1 : Via l'Alias (Recommandé)

Ouvrez le **Terminal** et tapez simplement :

```bash
lma
```

C'est tout ! L'application se lance. 🚀

### Méthode 2 : Via Commande Complète

```bash
cd ~/Desktop/LMA/scripts
python3 interface_pro.py
```

### Méthode 3 : Double-Clic (Optionnel)

Créer un raccourci sur le Bureau :

```bash
# Créer un fichier .command
cat > ~/Desktop/LMA.command << 'EOF'
#!/bin/bash
cd ~/Desktop/LMA/scripts
python3 interface_pro.py
EOF

# Rendre exécutable
chmod +x ~/Desktop/LMA.command
```

Maintenant vous pouvez **double-cliquer** sur `LMA.command` !

---

## 📁 Première Utilisation

### 1. Ajouter vos PDFs

```bash
# Copier vos PDFs dans le dossier articles
cp /chemin/vers/vos/pdfs/*.pdf ~/Desktop/LMA/articles/

# Exemple avec un fichier spécifique
cp ~/Downloads/Article_2024.pdf ~/Desktop/LMA/articles/
```

**Convention de nommage recommandée :**
- Format : `Auteur_Année_Titre.pdf`
- Exemple : `Dupont_2024_Machine_Learning.pdf`

### 2. Lancer et Indexer

```bash
# Lancer l'application
lma
```

Puis dans l'interface :
1. Cliquez sur **📥** (Index)
2. Attendez la fin de l'indexation
3. Vos articles apparaissent !

### 3. Utiliser l'Application

- **Recherche** : Tapez dans la barre 🔍
- **Ouvrir** : Double-clic sur un article
- **Filtrer** : 📚 ALL ou 📖 TO READ
- **Marquer** : 📌 TO READ ou ✅ DONE

---

## 🎨 Utiliser le Lecteur PDF

### Navigation Clavier
```
←  →         Page précédente/suivante
Space        Page suivante
Home / End   Première/dernière page
```

### Zoom
```
⌘ +  / ⌘ -   Zoomer/Dézoomer
⌘ 0          Ajuster à la fenêtre
Double-clic  Ajuster automatiquement
```

### Surlignage
```bash
# Activer le stylo
⌘ P

# Choisir une couleur
⌘ Y    # Jaune 🟨
⌘ R    # Rouge 🟥
⌘ G    # Vert 🟩
⌘ B    # Bleu 🟦

# Puis cliquer-glisser sur le texte
```

### Autres Fonctions
```
⌘ F    Rechercher dans le PDF
⌘ M    Afficher miniatures
⌘ T    Changer thème
⌘ W    Fermer
```

---

## 🔧 Commandes Utiles

### Vérifier l'Installation

```bash
# Version Python
python3 --version

# Modules installés
pip3 list | grep -i "pymupdf\|pillow\|fuzzywuzzy"

# Tester l'import
python3 -c "import fitz; print('PyMuPDF OK')"
```

### Gérer les PDFs

```bash
# Voir combien de PDFs vous avez
ls ~/Desktop/LMA/articles/*.pdf | wc -l

# Chercher un PDF
ls ~/Desktop/LMA/articles/ | grep "Machine"

# Copier plusieurs PDFs
cp ~/Downloads/*.pdf ~/Desktop/LMA/articles/
```

### Maintenance

```bash
# Nettoyer la base de données
rm ~/Desktop/LMA/data/articles.db
# Puis relancer et cliquer sur 📥 Index

# Voir la taille de la base
du -h ~/Desktop/LMA/data/articles.db

# Sauvegarder tout
cd ~/Desktop
tar -czf LMA_backup_$(date +%Y%m%d).tar.gz LMA/
```

### Mise à Jour

```bash
# Mettre à jour les dépendances
pip3 install --upgrade PyMuPDF pillow fuzzywuzzy python-levenshtein

# Re-télécharger les fichiers
cd ~/Desktop/LMA
# Puis remplacer les fichiers .py
```

---

## 🐛 Dépannage via Terminal

### L'alias 'lma' ne fonctionne pas

```bash
# Vérifier que l'alias existe
grep "lma" ~/.zshrc

# Si absent, le recréer
echo "alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'" >> ~/.zshrc
source ~/.zshrc

# Tester
lma
```

### Module 'fitz' introuvable

```bash
# Réinstaller PyMuPDF
pip3 install --force-reinstall PyMuPDF

# Vérifier
python3 -c "import fitz; print('OK')"
```

### Permission refusée

```bash
# Donner les permissions
chmod +x ~/Desktop/LMA/scripts/*.py

# Vérifier
ls -la ~/Desktop/LMA/scripts/
```

### Lecteur PDF ne s'ouvre pas

```bash
# Vérifier que le fichier existe
ls -la ~/Desktop/LMA/scripts/lecteur_pdf_moderne.py

# Tester le lecteur seul
cd ~/Desktop/LMA/scripts
python3 lecteur_pdf_moderne.py
```

### Erreur au lancement

```bash
# Voir les erreurs détaillées
cd ~/Desktop/LMA/scripts
python3 interface_pro.py

# Les erreurs s'affichent dans le terminal
```

---

## 💡 Astuces Terminal

### Ouvrir le Dossier Articles

```bash
# Ouvrir dans Finder (macOS)
open ~/Desktop/LMA/articles/

# Aller dans le dossier
cd ~/Desktop/LMA/articles/
```

### Compter les Articles

```bash
# Total de PDFs
find ~/Desktop/LMA/articles/ -name "*.pdf" | wc -l

# Par année (si nommage Auteur_Année_Titre.pdf)
ls ~/Desktop/LMA/articles/ | grep "2024" | wc -l
```

### Rechercher dans les Noms de Fichiers

```bash
# Chercher "Machine Learning"
find ~/Desktop/LMA/articles/ -name "*Machine*Learning*.pdf"

# Lister tous les PDFs d'un auteur
ls ~/Desktop/LMA/articles/ | grep "Dupont"
```

### Statistiques

```bash
# Taille totale des PDFs
du -sh ~/Desktop/LMA/articles/

# Nombre d'annotations
find ~/Desktop/LMA/articles/ -name "*.annotations.json" | wc -l

# Taille de la base de données
du -h ~/Desktop/LMA/data/articles.db
```

---

## 📊 Structure des Fichiers

```
~/Desktop/LMA/
├── scripts/
│   ├── interface_pro.py          # Interface principale 🇲🇦
│   ├── biblio_improved.py        # Gestion BDD + cache
│   └── lecteur_pdf_moderne.py    # Lecteur PDF optimisé
│
├── articles/                     # 📚 VOS PDFs ICI
│   ├── Auteur_2024_Titre.pdf
│   └── Auteur_2024_Titre.annotations.json
│
├── data/                         # Créé automatiquement
│   └── articles.db              # Base SQLite
│
└── LMA.command                   # Raccourci (optionnel)
```

---

## ⌨️ Tous les Raccourcis

### Terminal

```bash
lma              # Lancer l'application
cd ~/Desktop/LMA # Aller dans le dossier
```

### Interface LMA

| Raccourci | Action |
|-----------|--------|
| `⌘ F` | Rechercher |
| `↑` `↓` | Naviguer |
| `Enter` | Ouvrir |
| `⌘ Q` | Quitter |

### Lecteur PDF

| Raccourci | Action |
|-----------|--------|
| `←` `→` | Pages |
| `Space` | Page suivante |
| `⌘ +` `-` | Zoom |
| `⌘ F` | Rechercher |
| `⌘ P` | Stylo |
| `⌘ Y` `R` `G` `B` | Couleurs |
| `⌘ M` | Miniatures |
| `⌘ T` | Thème |

---

## 🆘 Support

### Problèmes Fréquents

**"command not found: lma"**
```bash
# Recréer l'alias
echo "alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'" >> ~/.zshrc
source ~/.zshrc
```

**"No module named 'fitz'"**
```bash
pip3 install --break-system-packages PyMuPDF
```

**"Permission denied"**
```bash
chmod +x ~/Desktop/LMA/scripts/*.py
```

### Réinstallation Complète

```bash
# Supprimer tout
rm -rf ~/Desktop/LMA

# Recommencer l'installation
mkdir -p ~/Desktop/LMA/scripts
mkdir -p ~/Desktop/LMA/articles
mkdir -p ~/Desktop/LMA/data
# ... puis suivre les étapes d'installation
```

---

## 📝 Commandes Récapitulatives

### Installation

```bash
# 1. Créer structure
mkdir -p ~/Desktop/LMA/{scripts,articles,data}

# 2. Installer dépendances
pip3 install --break-system-packages PyMuPDF pillow fuzzywuzzy python-levenshtein

# 3. Créer alias
echo "alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'" >> ~/.zshrc
source ~/.zshrc

# 4. Lancer
lma
```

### Utilisation Quotidienne

```bash
# Ouvrir terminal et taper :
lma

# C'est tout ! 🎉
```

---

## 🎓 Workflow Complet

```bash
# 1. Télécharger un PDF
# (Via navigateur dans ~/Downloads/)

# 2. Le copier dans LMA
cp ~/Downloads/Article_2024.pdf ~/Desktop/LMA/articles/

# 3. Lancer LMA
lma

# 4. Cliquer sur 📥 Index

# 5. Double-cliquer sur l'article pour l'ouvrir

# 6. Surligner avec ⌘ P puis ⌘ Y

# 7. Fermer avec ⌘ W
```

---

## 🌟 Pour Toujours Avoir LMA Disponible

Ajoutez ceci à votre `~/.zshrc` ou `~/.bashrc` :

```bash
# LMA - Library Management App 🇲🇦
alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'
alias lma-articles='cd ~/Desktop/LMA/articles && ls -lh'
alias lma-backup='cd ~/Desktop && tar -czf LMA_backup_$(date +%Y%m%d).tar.gz LMA/'
```

Maintenant vous avez :
- `lma` → Lance l'application
- `lma-articles` → Voir vos PDFs
- `lma-backup` → Sauvegarder tout

---

**🇲🇦 Profitez de LMA ! Tapez simplement `lma` dans le terminal pour commencer ! 📚**

*Dernière mise à jour : Janvier 2024*
