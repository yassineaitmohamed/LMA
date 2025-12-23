#!/usr/bin/env python3
"""
🚀 LECTEUR PDF PRO - Ultra-Rapide & Intelligent
Version MacBook Pro 2023 - Performance Maximale

Fonctionnalités:
- ⚡ Navigation ultra-rapide (préchargement intelligent)
- 🤖 Outils IA (résumé, extraction, analyse)
- ✍️ Annotations avancées (surlignage, notes, favoris)
- 🔍 Recherche instantanée avec prévisualisation
- 📑 Miniatures pour navigation rapide
- 🎨 Thèmes élégants (mode jour/nuit)
- 📤 Export (Markdown, annotations, citations)
- ⌨️ Raccourcis clavier pro
- 🎯 Performance optimisée (cache intelligent, threading)
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog, filedialog
import fitz  # PyMuPDF
from pathlib import Path
import re
from datetime import datetime
import subprocess
import json
import threading
from functools import lru_cache
from collections import OrderedDict
import hashlib
from PIL import Image, ImageTk

# ============================================================================
# GESTIONNAIRE DE CACHE INTELLIGENT
# ============================================================================

class CacheIntelligent:
    """Cache LRU optimisé pour pages PDF"""
    
    def __init__(self, max_size=10):
        self.cache = OrderedDict()
        self.max_size = max_size
        self.stats = {'hits': 0, 'misses': 0}
    
    def get(self, key):
        if key in self.cache:
            self.stats['hits'] += 1
            self.cache.move_to_end(key)
            return self.cache[key]
        self.stats['misses'] += 1
        return None
    
    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)
    
    def clear(self):
        self.cache.clear()
    
    def get_stats(self):
        total = self.stats['hits'] + self.stats['misses']
        if total == 0:
            return "Cache: 0 requêtes"
        hit_rate = (self.stats['hits'] / total) * 100
        return f"Cache: {hit_rate:.1f}% hits ({len(self.cache)}/{self.max_size})"


# ============================================================================
# GESTIONNAIRE D'ANNOTATIONS
# ============================================================================

class GestionnaireAnnotations:
    """Gestion des annotations (surlignages, notes, favoris)"""
    
    def __init__(self, fichier_pdf):
        self.fichier_pdf = Path(fichier_pdf)
        self.fichier_annotations = self.fichier_pdf.with_suffix('.annotations.json')
        self.annotations = self.charger()
    
    def charger(self):
        if self.fichier_annotations.exists():
            try:
                with open(self.fichier_annotations, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                pass
        return {
            'highlights': {},  # {page_num: [{'rect': [...], 'color': ..., 'text': ...}]}
            'notes': {},       # {page_num: [{'x': ..., 'y': ..., 'text': ...}]}
            'bookmarks': []    # [page_num, ...]
        }
    
    def sauvegarder(self):
        try:
            with open(self.fichier_annotations, 'w', encoding='utf-8') as f:
                json.dump(self.annotations, f, indent=2)
            return True
        except Exception as e:
            print(f"Erreur sauvegarde annotations: {e}")
            return False
    
    def ajouter_surlignage(self, page_num, rect, color='yellow', text=''):
        if str(page_num) not in self.annotations['highlights']:
            self.annotations['highlights'][str(page_num)] = []
        self.annotations['highlights'][str(page_num)].append({
            'rect': rect,
            'color': color,
            'text': text,
            'date': datetime.now().isoformat()
        })
        self.sauvegarder()
    
    def ajouter_note(self, page_num, x, y, text):
        if str(page_num) not in self.annotations['notes']:
            self.annotations['notes'][str(page_num)] = []
        self.annotations['notes'][str(page_num)].append({
            'x': x,
            'y': y,
            'text': text,
            'date': datetime.now().isoformat()
        })
        self.sauvegarder()
    
    def toggle_favori(self, page_num):
        if page_num in self.annotations['bookmarks']:
            self.annotations['bookmarks'].remove(page_num)
        else:
            self.annotations['bookmarks'].append(page_num)
            self.annotations['bookmarks'].sort()
        self.sauvegarder()
    
    def est_favori(self, page_num):
        return page_num in self.annotations['bookmarks']


# ============================================================================
# OUTILS IA
# ============================================================================

class OutilsIA:
    """Outils d'intelligence artificielle pour analyse PDF"""
    
    @staticmethod
    def extraire_citations(texte, max_citations=10):
        """Extraire les citations du texte"""
        citations = []
        
        # Pattern pour citations avec année
        pattern_citations = r'\b([A-Z][a-z]+(?:\s+(?:et\s+al\.|and\s+others|&))?\s*(?:\(\d{4}\)|,\s*\d{4}))'
        matches = re.findall(pattern_citations, texte)
        
        # Pattern pour références bibliographiques
        pattern_refs = r'\[(\d+)\]|\((\d+)\)'
        refs = re.findall(pattern_refs, texte)
        
        for match in matches[:max_citations]:
            citations.append({
                'type': 'inline',
                'text': match,
                'source': 'text'
            })
        
        for ref in refs[:max_citations]:
            num = ref[0] or ref[1]
            citations.append({
                'type': 'reference',
                'number': num,
                'source': 'text'
            })
        
        return citations
    
    @staticmethod
    def extraire_equations(texte, max_equations=10):
        """Extraire les équations mathématiques"""
        equations = []
        
        # Patterns pour équations LaTeX
        patterns = [
            r'\$\$(.+?)\$\$',
            r'\$(.+?)\$',
            r'\\begin\{equation\}(.+?)\\end\{equation\}',
            r'\\begin\{align\}(.+?)\\end\{align\}'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, texte, re.DOTALL)
            for match in matches[:max_equations]:
                equations.append({
                    'latex': match.strip(),
                    'type': 'equation'
                })
        
        return equations
    
    @staticmethod
    def generer_resume(texte, nb_phrases=5):
        """Générer un résumé simple (extraction de phrases clés)"""
        # Séparer en phrases
        phrases = re.split(r'[.!?]+', texte)
        phrases = [p.strip() for p in phrases if len(p.strip()) > 50]
        
        if not phrases:
            return "Aucun texte suffisant pour générer un résumé."
        
        # Calculer score pour chaque phrase (mots importants)
        mots_importants = ['theorem', 'proof', 'proposition', 'lemma', 'corollary', 
                          'definition', 'example', 'result', 'conclude', 'show']
        
        scores = []
        for phrase in phrases:
            score = sum(1 for mot in mots_importants if mot.lower() in phrase.lower())
            score += len(phrase.split()) / 50  # Favoriser phrases moyennes
            scores.append((score, phrase))
        
        # Trier et prendre les meilleures
        scores.sort(reverse=True, key=lambda x: x[0])
        resume_phrases = [phrase for _, phrase in scores[:nb_phrases]]
        
        return " ".join(resume_phrases)
    
    @staticmethod
    def extraire_mots_cles(texte, nb_mots=10):
        """Extraire les mots-clés principaux"""
        # Nettoyer le texte
        texte_clean = re.sub(r'[^a-zA-Z\s]', '', texte.lower())
        mots = texte_clean.split()
        
        # Filtrer mots courts et communs
        mots_communs = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'as', 'are', 
                       'was', 'were', 'be', 'been', 'for', 'in', 'of', 'to', 'and',
                       'or', 'but', 'by', 'from', 'with', 'this', 'that', 'these',
                       'those', 'it', 'its', 'can', 'may', 'will', 'would', 'should'}
        
        mots_filtres = [m for m in mots if len(m) > 4 and m not in mots_communs]
        
        # Compter fréquences
        freq = {}
        for mot in mots_filtres:
            freq[mot] = freq.get(mot, 0) + 1
        
        # Trier et prendre les plus fréquents
        mots_cles = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:nb_mots]
        
        return [mot for mot, _ in mots_cles]


# ============================================================================
# LECTEUR PDF PRO
# ============================================================================

class LecteurPDFPro:
    def __init__(self, fichier_pdf, biblio=None):
        self.fichier_pdf = Path(fichier_pdf)
        self.biblio = biblio
        self.doc = None
        self.page_actuelle = 0
        self.zoom = 1.2  # Zoom par défaut optimisé
        self.bibtex = ""
        
        # Cache intelligent avec plus de pages
        self.cache = CacheIntelligent(max_size=15)
        
        # Gestionnaire d'annotations
        self.gestionnaire_annotations = GestionnaireAnnotations(fichier_pdf)
        
        # Outils IA
        self.outils_ia = OutilsIA()
        
        # Mode sombre par défaut
        self.mode_sombre = True
        
        # Recherche
        self.resultats_recherche = []
        self.index_recherche = -1
        
        # Préchargement
        self.preload_thread = None
        self.preload_queue = []
        
        # Miniatures
        self.miniatures_cache = {}
        self.afficher_miniatures = False
        
        # Gestes
        self.geste_en_cours = False
        self.derniere_position_x = 0
        
        # Date d'ouverture
        self.date_ouverture = datetime.now()
        
        # Créer la fenêtre
        self.root = tk.Toplevel()
        self.root.title(f"🚀 {self.fichier_pdf.name}")
        self.root.geometry("1600x1000")
        
        # Thèmes
        self.init_themes()
        self.appliquer_theme()
        
        # Charger le PDF
        try:
            self.doc = fitz.open(str(self.fichier_pdf))
            self.total_pages = len(self.doc)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le PDF:\n{e}")
            self.root.destroy()
            return
        
        # Créer l'interface
        self.create_widgets()
        
        # Extraire BibTeX
        self.extraire_bibtex()
        
        # Afficher première page
        self.afficher_page()
        
        # Démarrer préchargement en arrière-plan
        self.demarrer_preload()
        
        # Bind raccourcis clavier
        self.bind_raccourcis()
    
    def init_themes(self):
        """Initialiser les thèmes"""
        self.theme_sombre = {
            'bg_dark': "#1a1a1a",
            'bg_darker': "#222222", 
            'bg_lighter': "#2a2a2a",
            'fg_light': "#e0e0e0",
            'accent_blue': "#5dade2",
            'accent_green': "#52c77a",
            'accent_orange': "#ffa726",
            'accent_red': "#ef5350",
            'accent_yellow': "#ffd54f",
            'canvas_bg': "#2d2d2d",
            'highlight': "#3d3d3d"
        }
        
        self.theme_clair = {
            'bg_dark': "#f8f9fa",
            'bg_darker': "#e9ecef",
            'bg_lighter': "#ffffff",
            'fg_light': "#212529",
            'accent_blue': "#0d6efd",
            'accent_green': "#198754",
            'accent_orange': "#fd7e14",
            'accent_red': "#dc3545",
            'accent_yellow': "#ffc107",
            'canvas_bg': "#ffffff",
            'highlight': "#e7f3ff"
        }
        
        self.theme = self.theme_sombre if self.mode_sombre else self.theme_clair
    
    def appliquer_theme(self):
        """Appliquer le thème actuel"""
        self.theme = self.theme_sombre if self.mode_sombre else self.theme_clair
        for key, value in self.theme.items():
            setattr(self, key, value)
        self.root.configure(bg=self.bg_dark)
    
    def create_widgets(self):
        """Créer l'interface utilisateur"""
        
        # ===== BARRE SUPÉRIEURE =====
        self.top_bar = tk.Frame(self.root, bg=self.bg_darker, height=50)
        self.top_bar.pack(fill="x")
        self.top_bar.pack_propagate(False)
        
        # Container principal
        top_container = tk.Frame(self.top_bar, bg=self.bg_darker)
        top_container.pack(fill="both", expand=True, padx=10, pady=8)
        
        # Titre (gauche)
        title_frame = tk.Frame(top_container, bg=self.bg_darker)
        title_frame.pack(side="left", fill="y")
        
        title = tk.Label(title_frame, 
                        text=f"📄 {self.fichier_pdf.name}",
                        font=("SF Pro Display", 13, "bold"),
                        bg=self.bg_darker, fg=self.accent_blue,
                        anchor="w")
        title.pack(side="left")
        
        # Info cache
        self.cache_label = tk.Label(title_frame,
                                    text="",
                                    font=("SF Pro Display", 9),
                                    bg=self.bg_darker, fg=self.fg_light,
                                    anchor="w")
        self.cache_label.pack(side="left", padx=10)
        
        # Boutons (droite)
        buttons_frame = tk.Frame(top_container, bg=self.bg_darker)
        buttons_frame.pack(side="right")
        
        # Bouton IA
        self.btn_ia = self.creer_bouton(buttons_frame, "🤖 IA", self.menu_ia, self.accent_blue)
        
        # Bouton Annotations
        self.btn_annotations = self.creer_bouton(buttons_frame, "✍️ Notes", self.menu_annotations, self.accent_orange)
        
        # Bouton Miniatures
        self.btn_miniatures = self.creer_bouton(buttons_frame, "📑 Pages", self.toggle_miniatures, self.accent_green)
        
        # Bouton Export
        self.btn_export = self.creer_bouton(buttons_frame, "📤 Export", self.menu_export, self.accent_yellow)
        
        # Bouton BibTeX
        self.btn_bibtex = self.creer_bouton(buttons_frame, "📋 BibTeX", self.copier_bibtex, self.accent_orange)
        
        # Bouton Theme
        icone = "🌙" if self.mode_sombre else "☀️"
        self.btn_theme = self.creer_bouton(buttons_frame, icone, self.toggle_theme, self.accent_yellow)
        
        # ===== PANNEAU PRINCIPAL =====
        main_frame = tk.Frame(self.root, bg=self.bg_dark)
        main_frame.pack(fill="both", expand=True)
        
        # Panneau miniatures (gauche, caché par défaut)
        self.panneau_miniatures = tk.Frame(main_frame, bg=self.bg_darker, width=200)
        
        # Titre miniatures
        tk.Label(self.panneau_miniatures, 
                text="📑 PAGES",
                font=("SF Pro Display", 11, "bold"),
                bg=self.bg_darker, fg=self.accent_green).pack(pady=10)
        
        # Canvas pour miniatures avec scrollbar
        miniatures_container = tk.Frame(self.panneau_miniatures, bg=self.bg_darker)
        miniatures_container.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.miniatures_scrollbar = tk.Scrollbar(miniatures_container)
        self.miniatures_scrollbar.pack(side="right", fill="y")
        
        self.miniatures_canvas = tk.Canvas(miniatures_container,
                                          bg=self.bg_darker,
                                          highlightthickness=0,
                                          yscrollcommand=self.miniatures_scrollbar.set)
        self.miniatures_canvas.pack(side="left", fill="both", expand=True)
        self.miniatures_scrollbar.config(command=self.miniatures_canvas.yview)
        
        self.miniatures_frame = tk.Frame(self.miniatures_canvas, bg=self.bg_darker)
        self.miniatures_canvas.create_window((0, 0), window=self.miniatures_frame, anchor="nw")
        
        # Panneau central (PDF)
        center_frame = tk.Frame(main_frame, bg=self.bg_dark)
        center_frame.pack(side="left", fill="both", expand=True)
        
        # Barre de recherche
        search_frame = tk.Frame(center_frame, bg=self.bg_darker, height=45)
        search_frame.pack(fill="x")
        search_frame.pack_propagate(False)
        
        search_container = tk.Frame(search_frame, bg=self.bg_darker)
        search_container.pack(fill="both", expand=True, padx=15, pady=8)
        
        tk.Label(search_container, text="🔍", bg=self.bg_darker, fg=self.accent_green,
                font=("SF Pro Display", 12)).pack(side="left", padx=(0, 5))
        
        self.search_entry = tk.Entry(search_container,
                                     font=("SF Pro Display", 11),
                                     bg=self.bg_lighter, fg=self.fg_light,
                                     insertbackground=self.fg_light,
                                     relief="flat")
        self.search_entry.pack(side="left", fill="x", expand=True)
        self.search_entry.bind("<Return>", lambda e: self.rechercher())
        self.search_entry.bind("<Escape>", lambda e: self.effacer_recherche())
        
        self.btn_search = tk.Label(search_container, text="Rechercher",
                                   font=("SF Pro Display", 10, "bold"),
                                   bg=self.bg_darker, fg=self.accent_green,
                                   cursor="hand2", padx=10)
        self.btn_search.pack(side="left", padx=5)
        self.btn_search.bind("<Button-1>", lambda e: self.rechercher())
        
        self.search_result_label = tk.Label(search_container, text="",
                                           font=("SF Pro Display", 9),
                                           bg=self.bg_darker, fg=self.fg_light)
        self.search_result_label.pack(side="left", padx=10)
        
        # Canvas PDF avec scrollbars
        canvas_frame = tk.Frame(center_frame, bg=self.bg_dark)
        canvas_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.scrollbar_y = tk.Scrollbar(canvas_frame)
        self.scrollbar_y.pack(side="right", fill="y")
        
        self.scrollbar_x = tk.Scrollbar(canvas_frame, orient="horizontal")
        self.scrollbar_x.pack(side="bottom", fill="x")
        
        self.canvas = tk.Canvas(canvas_frame,
                               bg=self.canvas_bg,
                               highlightthickness=0,
                               xscrollcommand=self.scrollbar_x.set,
                               yscrollcommand=self.scrollbar_y.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.scrollbar_y.config(command=self.canvas.yview)
        self.scrollbar_x.config(command=self.canvas.xview)
        
        # Bind événements canvas
        self.canvas.bind("<Double-Button-1>", lambda e: self.toggle_zoom_rapide())
        self.canvas.bind("<MouseWheel>", self.geste_scroll_intelligent)
        self.canvas.bind("<Button-4>", self.geste_scroll_intelligent)
        self.canvas.bind("<Button-5>", self.geste_scroll_intelligent)
        
        # ===== BARRE INFÉRIEURE =====
        self.bottom_bar = tk.Frame(self.root, bg=self.bg_darker, height=45)
        self.bottom_bar.pack(fill="x")
        self.bottom_bar.pack_propagate(False)
        
        bottom_container = tk.Frame(self.bottom_bar, bg=self.bg_darker)
        bottom_container.pack(fill="both", expand=True, padx=15, pady=8)
        
        # Navigation (gauche)
        nav_frame = tk.Frame(bottom_container, bg=self.bg_darker)
        nav_frame.pack(side="left")
        
        self.btn_first = self.creer_bouton_nav(nav_frame, "⏮", lambda: self.aller_page(0))
        self.btn_prev = self.creer_bouton_nav(nav_frame, "◀", self.page_precedente)
        
        self.page_entry = tk.Entry(nav_frame, width=6, font=("SF Pro Display", 11),
                                   bg=self.bg_lighter, fg=self.fg_light,
                                   justify="center", relief="flat")
        self.page_entry.pack(side="left", padx=5)
        self.page_entry.bind("<Return>", self.aller_page_saisie)
        
        self.page_label = tk.Label(nav_frame, text=f"/ {self.total_pages}",
                                   font=("SF Pro Display", 11),
                                   bg=self.bg_darker, fg=self.fg_light)
        self.page_label.pack(side="left")
        
        self.btn_next = self.creer_bouton_nav(nav_frame, "▶", self.page_suivante)
        self.btn_last = self.creer_bouton_nav(nav_frame, "⏭", lambda: self.aller_page(self.total_pages - 1))
        
        # Favoris
        self.btn_bookmark = tk.Label(nav_frame, text="⭐",
                                     font=("SF Pro Display", 14),
                                     bg=self.bg_darker, fg=self.fg_light,
                                     cursor="hand2", padx=8)
        self.btn_bookmark.pack(side="left", padx=10)
        self.btn_bookmark.bind("<Button-1>", lambda e: self.toggle_favori())
        
        # Centre - Info document
        info_frame = tk.Frame(bottom_container, bg=self.bg_darker)
        info_frame.pack(side="left", expand=True)
        
        # Zoom (droite)
        zoom_frame = tk.Frame(bottom_container, bg=self.bg_darker)
        zoom_frame.pack(side="right")
        
        self.btn_zoom_out = self.creer_bouton_nav(zoom_frame, "−", lambda: self.changer_zoom(-0.2))
        
        self.zoom_label = tk.Label(zoom_frame, text=f"{int(self.zoom * 100)}%",
                                   font=("SF Pro Display", 11),
                                   bg=self.bg_darker, fg=self.fg_light,
                                   width=6)
        self.zoom_label.pack(side="left", padx=5)
        
        self.btn_zoom_in = self.creer_bouton_nav(zoom_frame, "+", lambda: self.changer_zoom(0.2))
    
    def creer_bouton(self, parent, texte, commande, couleur):
        """Créer un bouton stylisé"""
        btn = tk.Label(parent, text=texte,
                      font=("SF Pro Display", 10, "bold"),
                      bg=self.bg_darker, fg=couleur,
                      cursor="hand2", padx=12, pady=4)
        btn.pack(side="left", padx=3)
        btn.bind("<Button-1>", lambda e: commande())
        return btn
    
    def creer_bouton_nav(self, parent, texte, commande):
        """Créer un bouton de navigation"""
        btn = tk.Label(parent, text=texte,
                      font=("SF Pro Display", 13),
                      bg=self.bg_darker, fg=self.accent_blue,
                      cursor="hand2", padx=8)
        btn.pack(side="left", padx=2)
        btn.bind("<Button-1>", lambda e: commande())
        return btn
    
    # ========== AFFICHAGE PAGE ==========
    
    def afficher_page(self):
        """Afficher la page actuelle (OPTIMISÉ)"""
        if not self.doc or self.page_actuelle < 0 or self.page_actuelle >= self.total_pages:
            return
        
        # Vérifier cache
        cache_key = f"{self.page_actuelle}_{self.zoom}"
        cached_image = self.cache.get(cache_key)
        
        if cached_image:
            photo = cached_image
        else:
            # Générer l'image
            page = self.doc[self.page_actuelle]
            mat = fitz.Matrix(self.zoom * 2, self.zoom * 2)  # DPI élevé pour clarté
            pix = page.get_pixmap(matrix=mat, alpha=False)
            
            # Convertir en PhotoImage
            img_data = pix.tobytes("ppm")
            photo = tk.PhotoImage(data=img_data, format="PPM")
            
            # Mettre en cache
            self.cache.set(cache_key, photo)
        
        # Afficher
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=photo, tags="page")
        self.canvas.image = photo  # Garder référence
        
        # Configurer scrollregion
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        # Mettre à jour UI
        self.page_entry.delete(0, tk.END)
        self.page_entry.insert(0, str(self.page_actuelle + 1))
        
        # Mettre à jour favori
        if self.gestionnaire_annotations.est_favori(self.page_actuelle):
            self.btn_bookmark.config(fg=self.accent_yellow)
        else:
            self.btn_bookmark.config(fg=self.fg_light)
        
        # Mettre à jour cache stats
        self.cache_label.config(text=self.cache.get_stats())
        
        # Afficher annotations si présentes
        self.afficher_annotations_page()
    
    def afficher_annotations_page(self):
        """Afficher les annotations de la page actuelle"""
        page_key = str(self.page_actuelle)
        
        # Surlignages
        if page_key in self.gestionnaire_annotations.annotations['highlights']:
            for hl in self.gestionnaire_annotations.annotations['highlights'][page_key]:
                # TODO: Dessiner rectangles de surlignage
                pass
        
        # Notes
        if page_key in self.gestionnaire_annotations.annotations['notes']:
            for note in self.gestionnaire_annotations.annotations['notes'][page_key]:
                # TODO: Afficher icônes de notes
                pass
    
    # ========== NAVIGATION ==========
    
    def page_precedente(self):
        """Page précédente"""
        if self.page_actuelle > 0:
            self.page_actuelle -= 1
            self.afficher_page()
            self.precharger_adjacentes()
    
    def page_suivante(self):
        """Page suivante"""
        if self.page_actuelle < self.total_pages - 1:
            self.page_actuelle += 1
            self.afficher_page()
            self.precharger_adjacentes()
    
    def aller_page(self, num_page):
        """Aller à une page spécifique"""
        if 0 <= num_page < self.total_pages:
            self.page_actuelle = num_page
            self.afficher_page()
            self.precharger_adjacentes()
    
    def aller_page_saisie(self, event=None):
        """Aller à la page saisie"""
        try:
            num = int(self.page_entry.get()) - 1
            self.aller_page(num)
        except:
            pass
    
    # ========== PRÉCHARGEMENT INTELLIGENT ==========
    
    def demarrer_preload(self):
        """Démarrer le préchargement en arrière-plan"""
        self.precharger_adjacentes()
    
    def precharger_adjacentes(self):
        """Précharger les pages adjacentes"""
        def preload_worker():
            # Précharger pages avant et après
            pages_a_precharger = []
            
            for offset in [1, -1, 2, -2]:
                page_num = self.page_actuelle + offset
                if 0 <= page_num < self.total_pages:
                    pages_a_precharger.append(page_num)
            
            for page_num in pages_a_precharger:
                cache_key = f"{page_num}_{self.zoom}"
                if not self.cache.get(cache_key):
                    try:
                        page = self.doc[page_num]
                        mat = fitz.Matrix(self.zoom * 2, self.zoom * 2)
                        pix = page.get_pixmap(matrix=mat, alpha=False)
                        img_data = pix.tobytes("ppm")
                        photo = tk.PhotoImage(data=img_data, format="PPM")
                        self.cache.set(cache_key, photo)
                    except:
                        pass
        
        # Lancer en thread
        if self.preload_thread is None or not self.preload_thread.is_alive():
            self.preload_thread = threading.Thread(target=preload_worker, daemon=True)
            self.preload_thread.start()
    
    # ========== ZOOM ==========
    
    def changer_zoom(self, delta):
        """Changer le niveau de zoom"""
        nouveau_zoom = max(0.5, min(3.0, self.zoom + delta))
        if nouveau_zoom != self.zoom:
            self.zoom = nouveau_zoom
            self.zoom_label.config(text=f"{int(self.zoom * 100)}%")
            self.cache.clear()
            self.afficher_page()
    
    def toggle_zoom_rapide(self):
        """Toggle zoom rapide (100% <-> 150%)"""
        if self.zoom == 1.0:
            self.zoom = 1.5
        elif self.zoom == 1.5:
            self.zoom = 1.0
        else:
            self.zoom = 1.0
        
        self.zoom_label.config(text=f"{int(self.zoom * 100)}%")
        self.cache.clear()
        self.afficher_page()
    
    # ========== GESTES ==========
    
    def geste_scroll_intelligent(self, event):
        """Scroll intelligent avec changement de page automatique"""
        yview = self.canvas.yview()
        
        if event.delta > 0 or event.num == 4:  # Scroll haut
            if yview[0] <= 0.0 and self.page_actuelle > 0:
                self.page_precedente()
                self.root.after(5, lambda: self.canvas.yview_moveto(1.0))
            else:
                self.canvas.yview_scroll(-1, "units")
        else:  # Scroll bas
            if yview[1] >= 1.0 and self.page_actuelle < self.total_pages - 1:
                self.page_suivante()
                self.root.after(5, lambda: self.canvas.yview_moveto(0.0))
            else:
                self.canvas.yview_scroll(1, "units")
        
        return "break"
    
    # ========== RECHERCHE ==========
    
    def rechercher(self):
        """Rechercher dans le document"""
        query = self.search_entry.get().strip()
        if not query:
            return
        
        self.resultats_recherche = []
        
        # Rechercher dans toutes les pages
        for page_num in range(self.total_pages):
            page = self.doc[page_num]
            text_instances = page.search_for(query)
            if text_instances:
                for inst in text_instances:
                    self.resultats_recherche.append((page_num, inst))
        
        if self.resultats_recherche:
            self.index_recherche = 0
            self.afficher_resultat_recherche()
            self.search_result_label.config(
                text=f"{len(self.resultats_recherche)} résultat(s)",
                fg=self.accent_green
            )
        else:
            self.search_result_label.config(
                text="Aucun résultat",
                fg=self.accent_red
            )
    
    def afficher_resultat_recherche(self):
        """Afficher le résultat de recherche actuel"""
        if 0 <= self.index_recherche < len(self.resultats_recherche):
            page_num, rect = self.resultats_recherche[self.index_recherche]
            self.aller_page(page_num)
            # TODO: Surligner le résultat sur le canvas
    
    def effacer_recherche(self):
        """Effacer la recherche"""
        self.search_entry.delete(0, tk.END)
        self.resultats_recherche = []
        self.index_recherche = -1
        self.search_result_label.config(text="")
    
    # ========== MINIATURES ==========
    
    def toggle_miniatures(self):
        """Afficher/masquer panneau miniatures"""
        self.afficher_miniatures = not self.afficher_miniatures
        
        if self.afficher_miniatures:
            self.panneau_miniatures.pack(side="left", fill="y")
            self.generer_miniatures()
        else:
            self.panneau_miniatures.pack_forget()
    
    def generer_miniatures(self):
        """Générer miniatures de toutes les pages"""
        # Effacer miniatures existantes
        for widget in self.miniatures_frame.winfo_children():
            widget.destroy()
        
        def generer_worker():
            for page_num in range(min(50, self.total_pages)):  # Limiter à 50 pages
                try:
                    if page_num in self.miniatures_cache:
                        continue
                    
                    page = self.doc[page_num]
                    mat = fitz.Matrix(0.15, 0.15)  # Petite taille
                    pix = page.get_pixmap(matrix=mat, alpha=False)
                    
                    # Convertir en PIL puis Tk
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    photo = ImageTk.PhotoImage(img)
                    
                    self.miniatures_cache[page_num] = photo
                    
                    # Afficher dans UI
                    self.root.after(0, lambda p=page_num, ph=photo: self.ajouter_miniature(p, ph))
                except:
                    pass
        
        threading.Thread(target=generer_worker, daemon=True).start()
    
    def ajouter_miniature(self, page_num, photo):
        """Ajouter une miniature au panneau"""
        frame = tk.Frame(self.miniatures_frame, bg=self.bg_darker, 
                        relief="solid", borderwidth=1)
        frame.pack(pady=5, padx=5)
        
        # Image
        label = tk.Label(frame, image=photo, bg=self.bg_darker, cursor="hand2")
        label.image = photo  # Garder référence
        label.pack()
        label.bind("<Button-1>", lambda e, p=page_num: self.aller_page(p))
        
        # Numéro page
        num_label = tk.Label(frame, text=str(page_num + 1),
                            font=("SF Pro Display", 8),
                            bg=self.bg_darker, fg=self.fg_light)
        num_label.pack()
        
        # Mettre à jour scrollregion
        self.miniatures_frame.update_idletasks()
        self.miniatures_canvas.config(scrollregion=self.miniatures_canvas.bbox("all"))
    
    # ========== ANNOTATIONS ==========
    
    def toggle_favori(self):
        """Toggle favori pour page actuelle"""
        self.gestionnaire_annotations.toggle_favori(self.page_actuelle)
        if self.gestionnaire_annotations.est_favori(self.page_actuelle):
            self.btn_bookmark.config(fg=self.accent_yellow)
            messagebox.showinfo("✓", f"Page {self.page_actuelle + 1} ajoutée aux favoris")
        else:
            self.btn_bookmark.config(fg=self.fg_light)
            messagebox.showinfo("✓", f"Page {self.page_actuelle + 1} retirée des favoris")
    
    def menu_annotations(self):
        """Menu des annotations"""
        menu = tk.Toplevel(self.root)
        menu.title("✍️ Annotations")
        menu.geometry("400x500")
        menu.configure(bg=self.bg_dark)
        
        # Titre
        tk.Label(menu, text="✍️ ANNOTATIONS",
                font=("SF Pro Display", 14, "bold"),
                bg=self.bg_dark, fg=self.accent_orange).pack(pady=15)
        
        # Boutons
        btn_frame = tk.Frame(menu, bg=self.bg_dark)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="📝 Ajouter Note",
                 command=self.ajouter_note,
                 font=("SF Pro Display", 11),
                 bg=self.accent_orange, fg="white",
                 relief="flat", padx=20, pady=8).pack(side="left", padx=5)
        
        tk.Button(btn_frame, text="🎨 Surligner Texte",
                 command=self.mode_surlignage,
                 font=("SF Pro Display", 11),
                 bg=self.accent_yellow, fg="black",
                 relief="flat", padx=20, pady=8).pack(side="left", padx=5)
        
        # Liste annotations
        list_frame = tk.Frame(menu, bg=self.bg_darker)
        list_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        tk.Label(list_frame, text="Notes & Surlignages:",
                font=("SF Pro Display", 11, "bold"),
                bg=self.bg_darker, fg=self.fg_light).pack(anchor="w", pady=5)
        
        text_area = scrolledtext.ScrolledText(list_frame,
                                              font=("SF Mono", 10),
                                              bg=self.bg_lighter, fg=self.fg_light,
                                              height=15)
        text_area.pack(fill="both", expand=True)
        
        # Afficher annotations existantes
        for page_key in sorted(self.gestionnaire_annotations.annotations['notes'].keys()):
            for note in self.gestionnaire_annotations.annotations['notes'][page_key]:
                text_area.insert(tk.END, f"[Page {int(page_key)+1}] {note['text']}\n\n")
    
    def ajouter_note(self):
        """Ajouter une note à la page actuelle"""
        note = simpledialog.askstring("Note", 
                                     f"Note pour page {self.page_actuelle + 1}:",
                                     parent=self.root)
        if note:
            self.gestionnaire_annotations.ajouter_note(
                self.page_actuelle, 0, 0, note
            )
            messagebox.showinfo("✓", "Note ajoutée!")
    
    def mode_surlignage(self):
        """Activer mode surlignage"""
        messagebox.showinfo("Info", 
                          "Mode surlignage: Sélectionnez du texte dans le PDF\n"
                          "(Fonctionnalité avancée en développement)")
    
    # ========== OUTILS IA ==========
    
    def menu_ia(self):
        """Menu des outils IA"""
        menu = tk.Toplevel(self.root)
        menu.title("🤖 Outils IA")
        menu.geometry("600x700")
        menu.configure(bg=self.bg_dark)
        
        # Titre
        tk.Label(menu, text="🤖 OUTILS D'INTELLIGENCE ARTIFICIELLE",
                font=("SF Pro Display", 14, "bold"),
                bg=self.bg_dark, fg=self.accent_blue).pack(pady=15)
        
        # Boutons outils
        btn_frame = tk.Frame(menu, bg=self.bg_dark)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="📝 Résumé Page",
                 command=lambda: self.generer_resume_page(),
                 font=("SF Pro Display", 11),
                 bg=self.accent_blue, fg="white",
                 relief="flat", padx=15, pady=8).grid(row=0, column=0, padx=5, pady=5)
        
        tk.Button(btn_frame, text="📚 Résumé Document",
                 command=lambda: self.generer_resume_document(),
                 font=("SF Pro Display", 11),
                 bg=self.accent_green, fg="white",
                 relief="flat", padx=15, pady=8).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(btn_frame, text="🔗 Extraire Citations",
                 command=lambda: self.extraire_citations_ia(),
                 font=("SF Pro Display", 11),
                 bg=self.accent_orange, fg="white",
                 relief="flat", padx=15, pady=8).grid(row=1, column=0, padx=5, pady=5)
        
        tk.Button(btn_frame, text="🔬 Mots-Clés",
                 command=lambda: self.extraire_mots_cles_ia(),
                 font=("SF Pro Display", 11),
                 bg=self.accent_yellow, fg="black",
                 relief="flat", padx=15, pady=8).grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(btn_frame, text="📐 Équations",
                 command=lambda: self.extraire_equations_ia(),
                 font=("SF Pro Display", 11),
                 bg=self.accent_red, fg="white",
                 relief="flat", padx=15, pady=8).grid(row=2, column=0, padx=5, pady=5)
        
        # Zone de résultats
        result_frame = tk.Frame(menu, bg=self.bg_darker)
        result_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        tk.Label(result_frame, text="📊 Résultats:",
                font=("SF Pro Display", 11, "bold"),
                bg=self.bg_darker, fg=self.fg_light).pack(anchor="w", pady=5)
        
        self.ia_result_text = scrolledtext.ScrolledText(result_frame,
                                                        font=("SF Mono", 10),
                                                        bg=self.bg_lighter,
                                                        fg=self.fg_light,
                                                        height=20)
        self.ia_result_text.pack(fill="both", expand=True)
    
    def generer_resume_page(self):
        """Générer résumé de la page actuelle"""
        page = self.doc[self.page_actuelle]
        texte = page.get_text()
        
        resume = self.outils_ia.generer_resume(texte, nb_phrases=5)
        
        self.ia_result_text.delete(1.0, tk.END)
        self.ia_result_text.insert(tk.END, f"=== RÉSUMÉ PAGE {self.page_actuelle + 1} ===\n\n")
        self.ia_result_text.insert(tk.END, resume)
    
    def generer_resume_document(self):
        """Générer résumé du document complet"""
        self.ia_result_text.delete(1.0, tk.END)
        self.ia_result_text.insert(tk.END, "⏳ Génération du résumé du document...\n\n")
        
        def worker():
            texte_complet = ""
            for page in self.doc:
                texte_complet += page.get_text() + "\n"
            
            resume = self.outils_ia.generer_resume(texte_complet, nb_phrases=10)
            
            self.root.after(0, lambda: self.ia_result_text.delete(1.0, tk.END))
            self.root.after(0, lambda: self.ia_result_text.insert(tk.END, 
                f"=== RÉSUMÉ DOCUMENT ({self.total_pages} pages) ===\n\n{resume}"))
        
        threading.Thread(target=worker, daemon=True).start()
    
    def extraire_citations_ia(self):
        """Extraire citations de la page actuelle"""
        page = self.doc[self.page_actuelle]
        texte = page.get_text()
        
        citations = self.outils_ia.extraire_citations(texte)
        
        self.ia_result_text.delete(1.0, tk.END)
        self.ia_result_text.insert(tk.END, f"=== CITATIONS PAGE {self.page_actuelle + 1} ===\n\n")
        
        if citations:
            for i, cit in enumerate(citations, 1):
                self.ia_result_text.insert(tk.END, f"{i}. [{cit['type']}] {cit.get('text', cit.get('number', ''))}\n")
        else:
            self.ia_result_text.insert(tk.END, "Aucune citation détectée.")
    
    def extraire_mots_cles_ia(self):
        """Extraire mots-clés du document"""
        texte_complet = ""
        for page in self.doc:
            texte_complet += page.get_text() + "\n"
        
        mots_cles = self.outils_ia.extraire_mots_cles(texte_complet, nb_mots=15)
        
        self.ia_result_text.delete(1.0, tk.END)
        self.ia_result_text.insert(tk.END, "=== MOTS-CLÉS DOCUMENT ===\n\n")
        
        for i, mot in enumerate(mots_cles, 1):
            self.ia_result_text.insert(tk.END, f"{i}. {mot}\n")
    
    def extraire_equations_ia(self):
        """Extraire équations de la page actuelle"""
        page = self.doc[self.page_actuelle]
        texte = page.get_text()
        
        equations = self.outils_ia.extraire_equations(texte)
        
        self.ia_result_text.delete(1.0, tk.END)
        self.ia_result_text.insert(tk.END, f"=== ÉQUATIONS PAGE {self.page_actuelle + 1} ===\n\n")
        
        if equations:
            for i, eq in enumerate(equations, 1):
                self.ia_result_text.insert(tk.END, f"{i}. {eq['latex']}\n\n")
        else:
            self.ia_result_text.insert(tk.END, "Aucune équation détectée.")
    
    # ========== EXPORT ==========
    
    def menu_export(self):
        """Menu d'export"""
        menu = tk.Toplevel(self.root)
        menu.title("📤 Export")
        menu.geometry("400x400")
        menu.configure(bg=self.bg_dark)
        
        tk.Label(menu, text="📤 EXPORT",
                font=("SF Pro Display", 14, "bold"),
                bg=self.bg_dark, fg=self.accent_yellow).pack(pady=20)
        
        btn_frame = tk.Frame(menu, bg=self.bg_dark)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="📝 Export Texte (.txt)",
                 command=self.export_texte,
                 font=("SF Pro Display", 11),
                 bg=self.accent_blue, fg="white",
                 relief="flat", padx=20, pady=10,
                 width=25).pack(pady=8)
        
        tk.Button(btn_frame, text="📄 Export Markdown (.md)",
                 command=self.export_markdown,
                 font=("SF Pro Display", 11),
                 bg=self.accent_green, fg="white",
                 relief="flat", padx=20, pady=10,
                 width=25).pack(pady=8)
        
        tk.Button(btn_frame, text="✍️ Export Annotations (.json)",
                 command=self.export_annotations,
                 font=("SF Pro Display", 11),
                 bg=self.accent_orange, fg="white",
                 relief="flat", padx=20, pady=10,
                 width=25).pack(pady=8)
        
        tk.Button(btn_frame, text="📋 Export BibTeX (.bib)",
                 command=self.export_bibtex,
                 font=("SF Pro Display", 11),
                 bg=self.accent_yellow, fg="black",
                 relief="flat", padx=20, pady=10,
                 width=25).pack(pady=8)
    
    def export_texte(self):
        """Exporter en texte brut"""
        fichier = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichier texte", "*.txt")],
            initialfile=f"{self.fichier_pdf.stem}.txt"
        )
        
        if fichier:
            try:
                with open(fichier, 'w', encoding='utf-8') as f:
                    for page in self.doc:
                        f.write(page.get_text())
                        f.write("\n\n" + "="*50 + "\n\n")
                messagebox.showinfo("✓", f"Export réussi:\n{fichier}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur export:\n{e}")
    
    def export_markdown(self):
        """Exporter en Markdown"""
        fichier = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown", "*.md")],
            initialfile=f"{self.fichier_pdf.stem}.md"
        )
        
        if fichier:
            try:
                with open(fichier, 'w', encoding='utf-8') as f:
                    f.write(f"# {self.fichier_pdf.name}\n\n")
                    f.write(f"*Exporté le {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")
                    f.write("---\n\n")
                    
                    for i, page in enumerate(self.doc):
                        f.write(f"## Page {i+1}\n\n")
                        f.write(page.get_text())
                        f.write("\n\n")
                
                messagebox.showinfo("✓", f"Export Markdown réussi:\n{fichier}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur export:\n{e}")
    
    def export_annotations(self):
        """Exporter les annotations"""
        fichier = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON", "*.json")],
            initialfile=f"{self.fichier_pdf.stem}_annotations.json"
        )
        
        if fichier:
            try:
                with open(fichier, 'w', encoding='utf-8') as f:
                    json.dump(self.gestionnaire_annotations.annotations, f, indent=2)
                messagebox.showinfo("✓", f"Export annotations réussi:\n{fichier}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur export:\n{e}")
    
    def export_bibtex(self):
        """Exporter la citation BibTeX"""
        fichier = filedialog.asksaveasfilename(
            defaultextension=".bib",
            filetypes=[("BibTeX", "*.bib")],
            initialfile=f"{self.fichier_pdf.stem}.bib"
        )
        
        if fichier:
            try:
                with open(fichier, 'w', encoding='utf-8') as f:
                    f.write(self.bibtex)
                messagebox.showinfo("✓", f"Export BibTeX réussi:\n{fichier}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur export:\n{e}")
    
    # ========== BIBTEX ==========
    
    def extraire_bibtex(self):
        """Extraire et générer citation BibTeX"""
        try:
            metadata = self.doc.metadata
            titre = metadata.get('title', '')
            auteur = metadata.get('author', '')
            
            if not titre:
                premiere_page = self.doc[0]
                texte = premiere_page.get_text()
                lignes = [l.strip() for l in texte.split('\n') if l.strip()]
                if lignes:
                    titre = lignes[0][:200]  # Limiter longueur
            
            # Extraire année
            annee = ""
            if 'creationDate' in metadata:
                try:
                    date_str = metadata['creationDate']
                    annee_match = re.search(r'D:(\d{4})', date_str)
                    if annee_match:
                        annee = annee_match.group(1)
                except:
                    pass
            
            if not annee:
                texte_debut = " ".join([self.doc[i].get_text() for i in range(min(3, self.total_pages))])
                annee_match = re.search(r'\b(19|20)\d{2}\b', texte_debut)
                if annee_match:
                    annee = annee_match.group(0)
            
            # Générer BibTeX
            self.bibtex = self.generer_bibtex(titre, auteur, annee)
            
        except Exception as e:
            print(f"Erreur extraction BibTeX: {e}")
            self.bibtex = f"% Erreur: {e}"
    
    def generer_bibtex(self, titre, auteur="", annee=""):
        """Générer citation BibTeX"""
        if not annee:
            annee = str(datetime.now().year)
        
        if auteur:
            premier_auteur = auteur.split(',')[0].split()[-1].lower()
            cle = f"{premier_auteur}{annee}"
        else:
            cle = f"article{annee}"
        
        cle = re.sub(r'[^a-z0-9]', '', cle)
        
        titre_clean = titre.replace('{', '').replace('}', '').strip()
        auteur_clean = auteur.replace('{', '').replace('}', '').strip() if auteur else "Unknown"
        
        bibtex = f"""@article{{{cle},
  title = {{{titre_clean}}},
  author = {{{auteur_clean}}},
  year = {{{annee}}},
  note = {{Source: {self.fichier_pdf.name}}}
}}"""
        
        return bibtex
    
    def copier_bibtex(self):
        """Copier BibTeX dans presse-papier"""
        if self.bibtex:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.bibtex)
            self.root.update()
            messagebox.showinfo("✓", "Citation BibTeX copiée!")
        else:
            messagebox.showwarning("⚠️", "Aucune citation disponible")
    
    # ========== THÈME ==========
    
    def toggle_theme(self):
        """Basculer entre mode clair/sombre"""
        self.mode_sombre = not self.mode_sombre
        self.appliquer_theme()
        
        # Mettre à jour bouton
        icone = "🌙" if self.mode_sombre else "☀️"
        self.btn_theme.config(text=icone, fg=self.accent_yellow)
        
        # Rafraîchir interface
        self.afficher_page()
        
        # TODO: Mettre à jour tous les widgets récursivement
    
    # ========== RACCOURCIS CLAVIER ==========
    
    def bind_raccourcis(self):
        """Définir les raccourcis clavier"""
        # Navigation
        self.root.bind("<Left>", lambda e: self.page_precedente())
        self.root.bind("<Right>", lambda e: self.page_suivante())
        self.root.bind("<Up>", lambda e: self.canvas.yview_scroll(-1, "units"))
        self.root.bind("<Down>", lambda e: self.canvas.yview_scroll(1, "units"))
        self.root.bind("<Home>", lambda e: self.aller_page(0))
        self.root.bind("<End>", lambda e: self.aller_page(self.total_pages - 1))
        self.root.bind("<space>", lambda e: self.page_suivante())
        self.root.bind("<BackSpace>", lambda e: self.page_precedente())
        
        # Zoom
        self.root.bind("<Control-plus>", lambda e: self.changer_zoom(0.2))
        self.root.bind("<Control-minus>", lambda e: self.changer_zoom(-0.2))
        self.root.bind("<Control-0>", lambda e: setattr(self, 'zoom', 1.0) or self.afficher_page())
        
        # Fonctionnalités
        self.root.bind("<Control-f>", lambda e: self.search_entry.focus())
        self.root.bind("<Control-b>", lambda e: self.copier_bibtex())
        self.root.bind("<Control-t>", lambda e: self.toggle_theme())
        self.root.bind("<Control-m>", lambda e: self.toggle_miniatures())
        self.root.bind("<Control-i>", lambda e: self.menu_ia())
        
        # Annotations
        self.root.bind("<Control-n>", lambda e: self.ajouter_note())
        self.root.bind("<Control-d>", lambda e: self.toggle_favori())
        
        # Quitter
        self.root.bind("<Escape>", lambda e: self.fermer())
        self.root.bind("<Control-q>", lambda e: self.fermer())
    
    # ========== FERMETURE ==========
    
    def fermer(self):
        """Fermer le lecteur"""
        if self.doc:
            self.doc.close()
        self.root.destroy()


# ============================================================================
# FONCTION PRINCIPALE
# ============================================================================

def ouvrir_pdf(fichier_pdf, biblio=None):
    """Ouvrir un PDF avec le lecteur pro"""
    try:
        lecteur = LecteurPDFPro(fichier_pdf, biblio)
        return lecteur
    except Exception as e:
        print(f"Erreur ouverture PDF: {e}")
        return None


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Mode CLI
        root = tk.Tk()
        root.withdraw()
        ouvrir_pdf(sys.argv[1])
        root.mainloop()
    else:
        # Mode GUI - Sélection fichier
        root = tk.Tk()
        root.withdraw()
        
        fichier = filedialog.askopenfilename(
            title="Sélectionner un PDF",
            filetypes=[("PDF", "*.pdf")]
        )
        
        if fichier:
            ouvrir_pdf(fichier)
            root.mainloop()
        else:
            print("Aucun fichier sélectionné")

# Alias pour compatibilité avec interface_pro.py
ouvrir_pdf_rapide = ouvrir_pdf

# Alias pour compatibilité avec interface_pro.py
ouvrir_pdf_rapide = ouvrir_pdf
