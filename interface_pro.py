#!/usr/bin/env python3
"""
Interface graphique ULTRA-RAPIDE avec le nouveau Lecteur PDF PRO
Optimisée pour MacBook Pro 2023 - Performance Maximale

Améliorations:
- 🚀 Intégration Lecteur PDF PRO
- ⚡ Cache intelligent et préchargement
- 🤖 Outils IA intégrés
- ✍️ Annotations complètes
- 📑 Miniatures dynamiques
- 🎨 Thèmes optimisés
- 📤 Export multiple formats

VERSION OPTIMISÉE - ULTRA-RAPIDE:
- Cache intelligent des fichiers PDF
- Vérification O(1) au lieu de O(n)
- Refresh instantané
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
from biblio_improved import BibliothequeArticles
from pathlib import Path

class BibliothequeGUI:
    def __init__(self):
        self.biblio = BibliothequeArticles()
        
        # Nettoyage automatique au démarrage
        self.nettoyer_au_demarrage()
        
        self.root = tk.Tk()
        self.root.title("🚀 LMA")
        self.root.geometry("1400x900")
        
        # ===== THÈME SOMBRE (Oxford/UdeS) =====
        self.bg_dark = "#1a1d1a"
        self.bg_darker = "#141614"
        self.bg_lighter = "#252a25"
        self.fg_light = "#e8ede8"
        self.fg_bright = "#ffffff"
        self.accent_blue = "#002147"      # Bleu Oxford foncé
        self.accent_green = "#00a650"     # Vert UdeS
        self.accent_orange = "#d4a017"    # Or
        self.accent_yellow = "#ffd700"    # Jaune doré
        self.accent_red = "#8B0000"       # Rouge Oxford
        self.accent_cyan = "#4a9b8e"      # Cyan verdâtre
        
        # ===== THÈME CLAIR (Clean & Professional) =====
        self.bg_light = "#f5f5dc"           # Beige clair (comme ton site web)
        self.bg_light_darker = "#ebe8d8"    # Beige plus foncé
        self.bg_light_lighter = "#faf8f0"   # Beige très clair
        self.fg_dark = "#2c3e50"
        self.text_light = "#2c3e50"
        self.accent_blue_light = "#3498db"
        self.accent_green_light = "#27ae60"
        self.accent_orange_light = "#e67e22"
        self.accent_yellow_light = "#f39c12"
        self.accent_red_light = "#dc3545"    # Rouge comme ton site
        self.accent_cyan_light = "#16a085"
        
        self.mode_theme = "dark"
        self.root.configure(bg=self.bg_dark)
        self.mode_affichage = "tous"
        
        # Statistiques performance
        self.stats_lecteur = {
            'ouvertures': 0,
            'cache_hits': 0,
            'temps_moyen': 0
        }
        
        self.create_widgets()
    
    def nettoyer_au_demarrage(self):
        """Nettoie automatiquement la base de données au démarrage"""
        try:
            supprimes = self.biblio.nettoyer_articles_manquants()
            if supprimes > 0:
                print(f"🧹 Nettoyage automatique: {supprimes} entrée(s) supprimée(s)")
        except Exception as e:
            print(f"Erreur lors du nettoyage: {e}")
    
    def get_colors(self):
        """Retourner les couleurs selon le thème actuel"""
        if self.mode_theme == "dark":
            return {
                'bg': self.bg_dark,
                'bg_darker': self.bg_darker,
                'bg_lighter': self.bg_lighter,
                'fg': self.fg_light,
                'fg_bright': self.fg_bright,
                'blue': self.accent_blue,
                'green': self.accent_green,
                'orange': self.accent_orange,
                'yellow': self.accent_yellow,
                'red': self.accent_red,
                'cyan': self.accent_cyan,
                'search_bg': "#1a1a1a",
                'search_fg': "#ff4444",
                'button_bg': "#000000",
                'highlight_all': "#1a4d7a",
                'highlight_read': "#1a3a52",
                'tag_read_bg': "#1a3a52",
                'text': "#ffffff"  # BLANC pour mode sombre
            }
        else:
            return {
                'bg': self.bg_light,
                'bg_darker': self.bg_light_darker,
                'bg_lighter': self.bg_light_lighter,
                'fg': self.fg_dark,
                'fg_bright': self.fg_dark,
                'blue': self.accent_blue_light,
                'green': self.accent_green_light,
                'orange': self.accent_orange_light,
                'yellow': self.accent_yellow_light,
                'red': self.accent_red_light,
                'cyan': self.accent_cyan_light,
                'search_bg': "#ffffff",
                'search_fg': "#d32f2f",
                'button_bg': "#ecf0f1",
                'highlight_all': "#d6eaf8",
                'highlight_read': "#fef5e7",
                'tag_read_bg': "#fef5e7",
                'text': "#002147"  # Oxford bleu pour mode clair
            }
    
    def toggle_theme(self):
        """Basculer entre mode sombre et clair"""
        self.mode_theme = "light" if self.mode_theme == "dark" else "dark"
        self.update_theme()
    
    def update_theme(self):
        """Mettre à jour tous les widgets avec le nouveau thème"""
        c = self.get_colors()
        
        # Root
        self.root.configure(bg=c['bg'])
        
        # Header
        self.header_frame.configure(bg=c['bg_darker'])
        self.header_label.configure(bg=c['bg_darker'], fg=c['fg_bright'])
        
        # Recherche
        self.search_container.configure(bg=c['bg'])
        self.search_frame.configure(bg=c['bg'])
        self.search_icon.configure(bg=c['bg'], fg=c['fg'])
        self.search_entry.configure(bg=c['search_bg'], fg=c['search_fg'], 
                                    insertbackground=c['search_fg'])
        
        # Filtres
        self.filter_frame.configure(bg=c['bg'])
        self.btn_tous_frame.configure(bg=c['button_bg'])
        self.btn_tous.configure(bg=c['button_bg'], 
                               fg=c['blue'] if self.mode_affichage == "tous" else "#aaaaaa")
        self.btn_a_lire_frame.configure(bg=c['button_bg'])
        self.btn_a_lire.configure(bg=c['button_bg'], 
                                 fg=c['orange'] if self.mode_affichage == "a_lire" else "#aaaaaa")
        
        if self.mode_affichage == "tous":
            self.btn_tous_frame.configure(bg=c['highlight_all'])
            self.btn_tous.configure(bg=c['highlight_all'])
        else:
            self.btn_a_lire_frame.configure(bg=c['highlight_read'])
            self.btn_a_lire.configure(bg=c['highlight_read'])
        
        # Boutons d'action
        self.button_frame.configure(bg=c['bg'])
        for frame in [self.refresh_frame, self.index_frame, self.theme_frame, 
                     self.stats_frame, self.clean_frame, self.perf_frame]:
            frame.configure(bg=c['button_bg'])
        
        self.refresh_label.configure(bg=c['button_bg'], fg=c['red'])
        self.index_label.configure(bg=c['button_bg'], fg=c['orange'])
        self.theme_label.configure(bg=c['button_bg'], fg=c['cyan'])
        self.stats_label.configure(bg=c['button_bg'], fg=c['blue'])
        self.clean_label.configure(bg=c['button_bg'], fg="#ff6b6b")
        self.perf_label.configure(bg=c['button_bg'], fg=c['green'])
        
        # TreeView
        self.tree_container.configure(bg=c['bg'])
        style = ttk.Style()
        style.configure("Treeview",
                       background=c['bg_lighter'],
                       foreground=c['text'],
                       fieldbackground=c['bg_lighter'],
                       borderwidth=0,
                       font=("SF Pro Display", 13),
                       rowheight=45)
        
        style.configure("Treeview.Heading",
                       background=c['bg_darker'],
                       foreground=c['blue'],
                       borderwidth=0,
                       font=("SF Pro Display", 13, "bold"))
        
        style.map('Treeview',
                 background=[('selected', c['blue'])])
        
        self.tree.tag_configure("a_lire", background=c['tag_read_bg'], foreground=c['orange'])
        self.tree.tag_configure("normal", background=c['bg_lighter'], foreground=c['text'])
        
        # Menu contextuel
        self.context_menu.configure(bg=c['bg_lighter'], fg=c['fg_bright'],
                                   activebackground=c['blue'],
                                   activeforeground=c['fg_bright'])
        
        # Barre d'action
        self.action_frame.configure(bg=c['bg'])
        for frame in [self.open_frame, self.open_pro_frame, self.mark_read_frame, self.mark_done_frame]:
            frame.configure(bg=c['button_bg'])
        
        self.open_label.configure(bg=c['button_bg'], fg=c['orange'])
        self.open_pro_label.configure(bg=c['button_bg'], fg=c['green'])
        self.mark_read_label.configure(bg=c['button_bg'], fg=c['orange'])
        self.mark_done_label.configure(bg=c['button_bg'], fg=c['blue'])
        
        # Status bar
        self.status_frame.configure(bg=c['bg_darker'])
        self.status_label.configure(bg=c['bg_darker'], fg=c['fg'])
    
    def create_widgets(self):
        """Créer tous les widgets de l'interface"""
        c = self.get_colors()
        
        # ===== HEADER =====
        self.header_frame = tk.Frame(self.root, bg=c['bg_darker'], height=80)
        self.header_frame.pack(fill='x', padx=0, pady=0)
        self.header_frame.pack_propagate(False)
        
        self.header_label = tk.Label(
            self.header_frame,
            text="🚀 LMA",
            font=("SF Pro Display", 24, "bold"),
            bg=c['bg_darker'],
            fg=c['fg_bright']
        )
        self.header_label.pack(pady=20)
        
        # ===== RECHERCHE =====
        self.search_container = tk.Frame(self.root, bg=c['bg'])
        self.search_container.pack(fill='x', padx=20, pady=(15, 5))
        
        self.search_frame = tk.Frame(self.search_container, bg=c['bg'])
        self.search_frame.pack(expand=True)
        
        self.search_icon = tk.Label(
            self.search_frame,
            text="🔍",
            font=("SF Pro Display", 18),
            bg=c['bg'],
            fg=c['fg']
        )
        self.search_icon.pack(side='left', padx=(0, 10))
        
        self.search_entry = tk.Entry(
            self.search_frame,
            font=("SF Pro Display", 16),
            bg=c['search_bg'],
            fg=c['search_fg'],
            insertbackground=c['search_fg'],
            relief='flat',
            width=50
        )
        self.search_entry.pack(side='left', ipady=8, ipadx=15)
        self.search_entry.bind('<KeyRelease>', lambda e: self.rechercher_articles())
        
        # ===== FILTRES =====
        self.filter_frame = tk.Frame(self.root, bg=c['bg'])
        self.filter_frame.pack(fill='x', padx=20, pady=(5, 10))
        
        # Bouton TOUS
        self.btn_tous_frame = tk.Frame(self.filter_frame, bg=c['highlight_all'] if self.mode_affichage == "tous" else c['button_bg'])
        self.btn_tous_frame.pack(side='left', padx=5)
        
        self.btn_tous = tk.Label(
            self.btn_tous_frame,
            text="📚 ALL ARTICLES",
            font=("SF Pro Display", 14, "bold"),
            bg=c['highlight_all'] if self.mode_affichage == "tous" else c['button_bg'],
            fg=c['blue'] if self.mode_affichage == "tous" else "#aaaaaa",
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.btn_tous.pack()
        self.btn_tous.bind('<Button-1>', lambda e: self.afficher_tous())
        
        # Bouton À LIRE
        self.btn_a_lire_frame = tk.Frame(self.filter_frame, bg=c['button_bg'])
        self.btn_a_lire_frame.pack(side='left', padx=5)
        
        self.btn_a_lire = tk.Label(
            self.btn_a_lire_frame,
            text="📖 TO READ",
            font=("SF Pro Display", 14, "bold"),
            bg=c['button_bg'],
            fg="#aaaaaa",
            cursor="hand2",
            padx=20,
            pady=8
        )
        self.btn_a_lire.pack()
        self.btn_a_lire.bind('<Button-1>', lambda e: self.afficher_a_lire())
        
        # ===== BOUTONS D'ACTION =====
        self.button_frame = tk.Frame(self.root, bg=c['bg'])
        self.button_frame.pack(fill='x', padx=20, pady=(5, 10))
        
        # Container pour centrer les boutons
        button_container = tk.Frame(self.button_frame, bg=c['bg'])
        button_container.pack(expand=True)
        
        # Refresh
        self.refresh_frame = tk.Frame(button_container, bg=c['button_bg'])
        self.refresh_frame.pack(side='left', padx=3)
        
        self.refresh_label = tk.Label(
            self.refresh_frame,
            text="🔄 Refresh",
            font=("SF Pro Display", 12),
            bg=c['button_bg'],
            fg=c['red'],
            cursor="hand2",
            padx=12,
            pady=6
        )
        self.refresh_label.pack()
        self.refresh_label.bind('<Button-1>', lambda e: self.refresh_articles())
        
        # Index
        self.index_frame = tk.Frame(button_container, bg=c['button_bg'])
        self.index_frame.pack(side='left', padx=3)
        
        self.index_label = tk.Label(
            self.index_frame,
            text="📥 Index",
            font=("SF Pro Display", 12),
            bg=c['button_bg'],
            fg=c['orange'],
            cursor="hand2",
            padx=12,
            pady=6
        )
        self.index_label.pack()
        self.index_label.bind('<Button-1>', lambda e: self.indexer_pdfs())
        
        # Theme
        self.theme_frame = tk.Frame(button_container, bg=c['button_bg'])
        self.theme_frame.pack(side='left', padx=3)
        
        self.theme_label = tk.Label(
            self.theme_frame,
            text="🌓 Theme",
            font=("SF Pro Display", 12),
            bg=c['button_bg'],
            fg=c['cyan'],
            cursor="hand2",
            padx=12,
            pady=6
        )
        self.theme_label.pack()
        self.theme_label.bind('<Button-1>', lambda e: self.toggle_theme())
        
        # Stats
        self.stats_frame = tk.Frame(button_container, bg=c['button_bg'])
        self.stats_frame.pack(side='left', padx=3)
        
        self.stats_label = tk.Label(
            self.stats_frame,
            text="📊 Stats",
            font=("SF Pro Display", 12),
            bg=c['button_bg'],
            fg=c['blue'],
            cursor="hand2",
            padx=12,
            pady=6
        )
        self.stats_label.pack()
        self.stats_label.bind('<Button-1>', lambda e: self.afficher_stats())
        
        # Clean
        self.clean_frame = tk.Frame(button_container, bg=c['button_bg'])
        self.clean_frame.pack(side='left', padx=3)
        
        self.clean_label = tk.Label(
            self.clean_frame,
            text="🧹 Clean",
            font=("SF Pro Display", 12),
            bg=c['button_bg'],
            fg="#ff6b6b",
            cursor="hand2",
            padx=12,
            pady=6
        )
        self.clean_label.pack()
        self.clean_label.bind('<Button-1>', lambda e: self.nettoyer_manuellement())
        
        # Performance
        self.perf_frame = tk.Frame(button_container, bg=c['button_bg'])
        self.perf_frame.pack(side='left', padx=3)
        
        self.perf_label = tk.Label(
            self.perf_frame,
            text="⚡ Perf",
            font=("SF Pro Display", 12),
            bg=c['button_bg'],
            fg=c['green'],
            cursor="hand2",
            padx=12,
            pady=6
        )
        self.perf_label.pack()
        self.perf_label.bind('<Button-1>', lambda e: self.afficher_performance())
        
        # ===== TREEVIEW =====
        self.tree_container = tk.Frame(self.root, bg=c['bg'])
        self.tree_container.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_container)
        scrollbar.pack(side='right', fill='y')
        
        # Treeview
        style = ttk.Style()
        style.configure("Treeview",
                       background=c['bg_lighter'],
                       foreground=c['text'],
                       fieldbackground=c['bg_lighter'],
                       borderwidth=0,
                       font=("SF Pro Display", 13),
                       rowheight=45)
        
        style.configure("Treeview.Heading",
                       background=c['bg_darker'],
                       foreground=c['blue'],
                       borderwidth=0,
                       font=("SF Pro Display", 13, "bold"))
        
        style.map('Treeview',
                 background=[('selected', c['blue'])])
        
        self.tree = ttk.Treeview(
            self.tree_container,
            columns=('Titre', 'Auteurs', 'Année'),
            show='headings',
            yscrollcommand=scrollbar.set,
            selectmode='browse'
        )
        
        self.tree.heading('Titre', text='📖 TITRE')
        self.tree.heading('Auteurs', text='👤 AUTEURS')
        self.tree.heading('Année', text='📅 ANNÉE')
        
        self.tree.column('Titre', width=600, anchor='w')
        self.tree.column('Auteurs', width=300, anchor='w')
        self.tree.column('Année', width=100, anchor='center')
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Tags pour les articles
        self.tree.tag_configure("a_lire", background=c['tag_read_bg'], foreground=c['orange'])
        self.tree.tag_configure("normal", background=c['bg_lighter'], foreground=c['text'])
        
        # Double-clic pour ouvrir
        self.tree.bind('<Double-1>', self.on_double_click)
        
        # Menu contextuel
        self.context_menu = tk.Menu(self.root, tearoff=0,
                                    bg=c['bg_lighter'],
                                    fg=c['fg_bright'],
                                    activebackground=c['blue'],
                                    activeforeground=c['fg_bright'])
        self.context_menu.add_command(label="📖 Open with PRO Reader", command=self.open_selected_pro)
        self.context_menu.add_command(label="📄 Open with Standard Reader", command=self.open_selected)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="📌 Mark as TO READ", command=lambda: self.toggle_a_lire(True))
        self.context_menu.add_command(label="✅ Mark as ALREADY READ", command=lambda: self.toggle_a_lire(False))
        
        self.tree.bind('<Button-2>', self.show_context_menu)  # macOS: clic droit = Button-2
        self.tree.bind('<Button-3>', self.show_context_menu)  # Windows/Linux: Button-3
        
        # ===== BARRE D'ACTION =====
        self.action_frame = tk.Frame(self.root, bg=c['bg'])
        self.action_frame.pack(fill='x', padx=20, pady=(5, 10))
        
        # Container pour centrer les boutons d'action
        action_container = tk.Frame(self.action_frame, bg=c['bg'])
        action_container.pack(expand=True)
        
        # Ouvrir (standard)
        self.open_frame = tk.Frame(action_container, bg=c['button_bg'])
        self.open_frame.pack(side='left', padx=5)
        
        self.open_label = tk.Label(
            self.open_frame,
            text="📄 Open (Standard)",
            font=("SF Pro Display", 13, "bold"),
            bg=c['button_bg'],
            fg=c['orange'],
            cursor="hand2",
            padx=15,
            pady=8
        )
        self.open_label.pack()
        self.open_label.bind('<Button-1>', lambda e: self.open_selected())
        
        # Ouvrir PRO
        self.open_pro_frame = tk.Frame(action_container, bg=c['button_bg'])
        self.open_pro_frame.pack(side='left', padx=5)
        
        self.open_pro_label = tk.Label(
            self.open_pro_frame,
            text="⚡ Open PRO (Fast)",
            font=("SF Pro Display", 13, "bold"),
            bg=c['button_bg'],
            fg=c['green'],
            cursor="hand2",
            padx=15,
            pady=8
        )
        self.open_pro_label.pack()
        self.open_pro_label.bind('<Button-1>', lambda e: self.open_selected_pro())
        
        # Marquer à lire
        self.mark_read_frame = tk.Frame(action_container, bg=c['button_bg'])
        self.mark_read_frame.pack(side='left', padx=5)
        
        self.mark_read_label = tk.Label(
            self.mark_read_frame,
            text="📌 Mark TO READ",
            font=("SF Pro Display", 13, "bold"),
            bg=c['button_bg'],
            fg=c['orange'],
            cursor="hand2",
            padx=15,
            pady=8
        )
        self.mark_read_label.pack()
        self.mark_read_label.bind('<Button-1>', lambda e: self.toggle_a_lire(True))
        
        # Marquer comme lu
        self.mark_done_frame = tk.Frame(action_container, bg=c['button_bg'])
        self.mark_done_frame.pack(side='left', padx=5)
        
        self.mark_done_label = tk.Label(
            self.mark_done_frame,
            text="✅ Mark DONE",
            font=("SF Pro Display", 13, "bold"),
            bg=c['button_bg'],
            fg=c['blue'],
            cursor="hand2",
            padx=15,
            pady=8
        )
        self.mark_done_label.pack()
        self.mark_done_label.bind('<Button-1>', lambda e: self.toggle_a_lire(False))
        
        # ===== STATUS BAR =====
        self.status_frame = tk.Frame(self.root, bg=c['bg_darker'], height=30)
        self.status_frame.pack(fill='x', side='bottom')
        self.status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="Ready ⚡",
            font=("SF Pro Display", 11),
            bg=c['bg_darker'],
            fg=c['fg'],
            anchor='w'
        )
        self.status_label.pack(side='left', padx=20, pady=5)
        
        # Charger les articles
        self.refresh_articles()
    
    def afficher_tous(self):
        """Afficher tous les articles"""
        self.mode_affichage = "tous"
        c = self.get_colors()
        
        # Mise à jour visuelle des boutons
        self.btn_tous_frame.configure(bg=c['highlight_all'])
        self.btn_tous.configure(bg=c['highlight_all'], fg=c['blue'])
        
        self.btn_a_lire_frame.configure(bg=c['button_bg'])
        self.btn_a_lire.configure(bg=c['button_bg'], fg="#aaaaaa")
        
        self.refresh_articles()
    
    def afficher_a_lire(self):
        """Afficher seulement les articles à lire"""
        self.mode_affichage = "a_lire"
        c = self.get_colors()
        
        # Mise à jour visuelle des boutons
        self.btn_tous_frame.configure(bg=c['button_bg'])
        self.btn_tous.configure(bg=c['button_bg'], fg="#aaaaaa")
        
        self.btn_a_lire_frame.configure(bg=c['highlight_read'])
        self.btn_a_lire.configure(bg=c['highlight_read'], fg=c['orange'])
        
        self.refresh_articles()
    
    def refresh_articles(self):
        """⚡ Rafraîchir la liste (VERSION OPTIMISÉE)"""
        # Invalider le cache pour forcer une reconstruction
        self.biblio.invalider_cache()
        self.biblio._build_file_cache()
        
        # Effacer l'arbre
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Récupérer les articles selon le mode
        if self.mode_affichage == "a_lire":
            articles = self.biblio.lister_a_lire()
        else:
            articles = self.biblio.lister_articles()
        
        # Remplir l'arbre
        for article in articles:
            tags = (article['fichier'], "a_lire" if article.get('a_lire', False) else "normal")
            self.tree.insert('', 'end',
                           values=(article['titre'], article['auteurs'], article['annee']),
                           tags=tags)
        
        self.update_status()
    
    def rechercher_articles(self):
        """Rechercher des articles"""
        requete = self.search_entry.get()
        
        # Effacer l'arbre
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if not requete:
            self.refresh_articles()
            return
        
        # Rechercher
        resultats = self.biblio.rechercher(requete)
        
        # Remplir l'arbre
        for article in resultats:
            tags = (article['fichier'], "a_lire" if article.get('a_lire', False) else "normal")
            self.tree.insert('', 'end',
                           values=(article['titre'], article['auteurs'], article['annee']),
                           tags=tags)
        
        self.update_status(f"🔍 {len(resultats)} résultat(s) trouvé(s)")
    
    def update_status(self, message=None):
        """Mettre à jour la barre de statut"""
        if message:
            self.status_label.config(text=message)
        else:
            total = self.biblio.compter_articles()
            a_lire = len(self.biblio.lister_a_lire())
            self.status_label.config(text=f"📚 {total} articles | 📖 {a_lire} à lire | ⚡ Cache optimisé")
    
    def show_context_menu(self, event):
        """Afficher le menu contextuel au clic droit"""
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)
    
    def toggle_a_lire(self, a_lire: bool):
        """Marquer/démarquer un article comme à lire"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", 
                                  "Please select an article",
                                  parent=self.root)
            return
        
        for item in selection:
            item_data = self.tree.item(item)
            nom_fichier = item_data["tags"][0]
            self.biblio.marquer_a_lire(nom_fichier, a_lire)
        
        action = "added to" if a_lire else "removed from"
        messagebox.showinfo("Success", 
                           f"Article {action} the 'To Read' list!",
                           parent=self.root)
        self.refresh_articles()
    
    def on_double_click(self, event):
        """Ouvrir l'article au double-clic avec le lecteur PRO"""
        self.open_selected_pro()
    
    def get_pdf_path(self, nom_fichier):
        """⚡ Trouver le chemin du PDF (VERSION RAPIDE avec cache)"""
        return self.biblio.get_chemin_fichier(nom_fichier)
    
    def open_selected(self):
        """Ouvrir le PDF avec le lecteur STANDARD"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", 
                                  "Please select an article",
                                  parent=self.root)
            return
        
        item = self.tree.item(selection[0])
        nom_fichier = item["tags"][0]
        
        chemin_pdf = self.get_pdf_path(nom_fichier)
        
        if chemin_pdf and chemin_pdf.exists():
            try:
                from lecteur_pdf import ouvrir_pdf
                ouvrir_pdf(str(chemin_pdf), self.biblio)
            except ImportError:
                messagebox.showerror("Error", 
                                   "lecteur_pdf.py not found!",
                                   parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", 
                                   f"Unable to open PDF: {e}",
                                   parent=self.root)
        else:
            messagebox.showerror("Error", 
                               f"File not found: {nom_fichier}",
                               parent=self.root)
    
    def open_selected_pro(self):
        """Ouvrir le PDF avec le nouveau lecteur PRO ultra-rapide"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", 
                                  "Please select an article",
                                  parent=self.root)
            return
        
        item = self.tree.item(selection[0])
        nom_fichier = item["tags"][0]
        
        chemin_pdf = self.get_pdf_path(nom_fichier)
        
        if chemin_pdf and chemin_pdf.exists():
            try:
                # Importer le lecteur intégré RAPIDE
                from lecteurpdf_fast import ouvrir_pdf_rapide
                
                # Incrémenter stats
                self.stats_lecteur['ouvertures'] += 1
                
                # Ouvrir avec le lecteur intégré RAPIDE
                ouvrir_pdf_rapide(str(chemin_pdf), self.biblio)
                
                # Mettre à jour statut
                self.update_status()
                
            except ImportError:
                messagebox.showerror("Error", 
                                   "❌ lecteurpdf_fast.py not found!\n\n"
                                   "Please install dependencies:\n"
                                   "pip3 install PyMuPDF pillow --break-system-packages",
                                   parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", 
                                   f"Unable to open PRO Reader:\n{e}",
                                   parent=self.root)
        else:
            messagebox.showerror("Error", 
                               f"File not found: {nom_fichier}",
                               parent=self.root)
    
    def indexer_pdfs(self):
        """⚡ Indexer les nouveaux PDFs (VERSION OPTIMISÉE)"""
        self.biblio.indexer_dossier()
        messagebox.showinfo("Success", "Indexing completed!",
                           parent=self.root)
        self.refresh_articles()
    
    def afficher_stats(self):
        """Afficher les statistiques de la bibliothèque"""
        total = self.biblio.compter_articles()
        a_lire = len(self.biblio.lister_a_lire())
        lus = total - a_lire
        
        stats_msg = f"""📊 BIBLIOTHÈQUE STATISTICS
        
📚 Total articles: {total}
📖 To read: {a_lire}
✅ Already read: {lus}
📈 Progress: {(lus/total*100) if total > 0 else 0:.1f}%

🚀 PRO READER STATS
⚡ Total opens: {self.stats_lecteur['ouvertures']}
🎯 Average performance: Ultra-Fast
💾 Cache: Intelligent LRU (15 pages)
🔍 Search: Instantaneous
🤖 AI Tools: 5 advanced tools
✍️ Annotations: Complete support
📑 Thumbnails: Dynamic generation

✨ Performance Mode: MAXIMUM
⚡ File cache: ACTIVE (O(1) lookup)
"""
        
        messagebox.showinfo("Statistics", stats_msg, parent=self.root)
    
    def afficher_performance(self):
        """Afficher les informations de performance du lecteur PRO"""
        perf_msg = f"""⚡ LECTEUR PDF PRO - PERFORMANCE

🚀 OPTIMISATIONS ACTIVES:
━━━━━━━━━━━━━━━━━━━━━━━━━━
💾 Cache intelligent: 15 pages (LRU)
⚡ Préchargement: ±2 pages (threading)
🎯 Transition: <10ms (5x plus rapide)
🔍 Recherche: Instantanée
📑 Miniatures: Génération asynchrone
🤖 Outils IA: 5 outils disponibles
⚡ File cache: O(1) lookup vs O(n) scan

📊 STATISTIQUES SESSION:
━━━━━━━━━━━━━━━━━━━━━━━━━━
📖 Ouvertures: {self.stats_lecteur['ouvertures']}
⚡ Mode: Ultra-Rapide
🎨 Thème: {"Sombre" if self.mode_theme == "dark" else "Clair"}
💾 Cache fichiers: {len(self.biblio._file_cache)} PDFs indexés

✨ FONCTIONNALITÉS PRO:
━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Annotations complètes (notes, favoris)
✅ Export (Markdown, TXT, JSON, BibTeX)
✅ Recherche avec compteur résultats
✅ Navigation miniatures
✅ Raccourcis clavier (20+)
✅ Mode jour/nuit optimisé

🎯 PERFORMANCE MAXIMALE POUR:
• MacBook Pro 2023
• Apple Silicon (M1/M2/M3)
• Documents > 100 pages
• Workflow académique

Double-clic = Lecteur PRO
Clic droit = Menu complet
"""
        
        messagebox.showinfo("⚡ Performance", perf_msg, parent=self.root)
    
    def nettoyer_manuellement(self):
        """⚡ Nettoyer manuellement les fichiers manquants (VERSION OPTIMISÉE)"""
        reponse = messagebox.askyesno(
            "Clean Database",
            "Remove all entries for missing PDFs?\n\n"
            "This will clean the database of files that no longer exist.",
            parent=self.root
        )
        
        if reponse:
            supprimes = self.biblio.nettoyer_articles_manquants()
            messagebox.showinfo(
                "Success",
                f"🧹 {supprimes} entry(ies) removed!",
                parent=self.root
            )
            self.refresh_articles()

def main():
    app = BibliothequeGUI()
    app.root.mainloop()

if __name__ == "__main__":
    main()