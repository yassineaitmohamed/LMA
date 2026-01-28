# 🇲🇦 LMA - Library Management App

> Gestionnaire de bibliothèque d'articles PDF avec lecteur intégré et annotations intelligentes

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)]()

![LMA Interface](https://via.placeholder.com/800x500/C1272D/FFFFFF?text=LMA+Interface)

## 📖 Description

**LMA** (Library Management App) est une application de gestion de bibliothèque d'articles scientifiques en PDF. Organisez, recherchez et annotez vos articles académiques en toute simplicité.

### ✨ Fonctionnalités Principales

#### 📚 Gestion de Bibliothèque
- ⚡ **Indexation automatique** de vos PDFs avec extraction de métadonnées
- 🗄️ **Base de données SQLite** ultra-rapide avec cache intelligent
- 🔍 **Recherche instantanée** par titre, auteur ou contenu
- 🏷️ **Organisation** : marquez les articles à lire ou déjà lus
- 🧹 **Nettoyage automatique** des fichiers manquants

#### 📖 Lecteur PDF Professionnel
- 🖱️ **Navigation fluide** optimisée pour trackpad MacBook
- 🔎 **Zoom intelligent** avec raccourcis clavier (⌘ +/-)
- 🖍️ **Surlignage en 4 couleurs** : Jaune, Rouge, Vert, Bleu
- 💾 **Annotations persistantes** sauvegardées automatiquement
- 🔍 **Recherche dans le PDF** avec navigation entre résultats
- 🖼️ **Miniatures** pour aperçu et navigation rapide
- 🌓 **Thème clair/sombre** adaptatif

#### 🎨 Interface Moderne
- 🇲🇦 **Design aux couleurs du Maroc** (Rouge #C1272D, Vert #006233, Or #FFD700)
- 🎯 Interface épurée avec tableau agrandi
- ⌨️ Raccourcis clavier intuitifs
- 📱 Responsive et fluide

---

## 🚀 Installation Rapide

### Prérequis

- **Python 3.8+** (inclus sur macOS)
- **macOS** 10.14+, **Linux**, ou **Windows** 10/11
- **16 Go RAM** recommandé

### Installation en 3 commandes

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/LMA.git
cd LMA

# 2. Installer les dépendances
pip3 install -r requirements.txt

# 3. Lancer l'application
cd scripts
python3 interface_pro.py
```

### Installation manuelle des dépendances

```bash
pip3 install PyMuPDF pillow fuzzywuzzy python-levenshtein
```

**Sur macOS Monterey+ :**
```bash
pip3 install --break-system-packages PyMuPDF pillow fuzzywuzzy python-levenshtein
```

---

## 📁 Structure du Projet

```
LMA/
├── scripts/
│   ├── interface_pro.py          # Interface principale 🇲🇦
│   ├── biblio_improved.py        # Gestion BDD + cache O(1)
│   └── lecteur_pdf_moderne.py    # Lecteur PDF optimisé
│
├── articles/                     # 📚 Placez vos PDFs ici
│   ├── Article1.pdf
│   ├── Article1.annotations.json # Annotations
│   └── ...
│
├── data/                         # Créé automatiquement
│   └── articles.db              # Base de données SQLite
│
├── requirements.txt              # Dépendances Python
├── README.md                     # Ce fichier
└── LICENSE                       # Licence MIT
```

---

## 🎯 Utilisation

### 1️⃣ Ajouter vos PDFs

Copiez vos articles dans le dossier `articles/` :

```bash
cp /chemin/vers/vos/articles/*.pdf ~/Desktop/LMA/articles/
```

**Convention de nommage recommandée :**
- Format : `Auteur_Année_Titre.pdf`
- Exemple : `Dupont_2024_Machine_Learning.pdf`

### 2️⃣ Indexer les PDFs

1. Lancez l'application
2. Cliquez sur **📥** (Index)
3. Attendez la fin de l'indexation
4. Vos articles apparaissent dans le tableau !

### 3️⃣ Rechercher et Ouvrir

- **Recherche** : Tapez dans la barre 🔍
- **Ouvrir** : Double-clic sur l'article
- **Filtrer** : 📚 ALL ou 📖 TO READ

### 4️⃣ Annoter un PDF

1. **Ouvrir** un PDF (double-clic)
2. **Activer le stylo** : `⌘ P`
3. **Choisir une couleur** : `⌘ Y` (jaune), `⌘ R` (rouge), etc.
4. **Surligner** : Cliquer-glisser sur le texte
5. **Sauvegarder** : Automatique !

---

## ⌨️ Raccourcis Clavier

### Interface Principale

| Raccourci | Action |
|-----------|--------|
| `⌘ F` | Rechercher |
| `↑` `↓` | Naviguer dans la liste |
| `Enter` | Ouvrir l'article sélectionné |
| `⌘ Q` | Quitter |

### Lecteur PDF

#### Navigation
| Raccourci | Action |
|-----------|--------|
| `←` `→` | Page précédente/suivante |
| `Space` | Page suivante |
| `Backspace` | Page précédente |
| `Home` / `End` | Première/dernière page |

#### Zoom
| Raccourci | Action |
|-----------|--------|
| `⌘ +` / `⌘ -` | Zoomer/Dézoomer |
| `⌘ 0` | Ajuster à la fenêtre |
| `Double-clic` | Ajuster automatiquement |

#### Annotations
| Raccourci | Action |
|-----------|--------|
| `⌘ P` | Activer/désactiver le stylo |
| `⌘ Y` | Couleur jaune 🟨 |
| `⌘ R` | Couleur rouge 🟥 |
| `⌘ G` | Couleur vert 🟩 |
| `⌘ B` | Couleur bleu 🟦 |

#### Autres
| Raccourci | Action |
|-----------|--------|
| `⌘ F` | Rechercher dans le PDF |
| `⌘ M` | Afficher miniatures |
| `⌘ T` | Changer thème clair/sombre |
| `⌘ W` | Fermer le lecteur |

---

## 🔧 Configuration

### Créer un Raccourci Desktop (macOS)

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

Double-cliquez sur `LMA.command` pour lancer !

### Créer un Alias Terminal

```bash
# Ajouter à .zshrc (macOS) ou .bashrc (Linux)
echo "alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'" >> ~/.zshrc

# Recharger
source ~/.zshrc

# Utiliser
lma
```

---

## 🐛 Dépannage

### L'application ne démarre pas

**Erreur** : `ModuleNotFoundError: No module named 'fitz'`

**Solution** :
```bash
pip3 install PyMuPDF
```

### Les PDFs ne s'ouvrent pas

**Erreur** : "lecteur_pdf_moderne.py introuvable"

**Solution** :
```bash
# Vérifier que le fichier existe
ls scripts/lecteur_pdf_moderne.py

# Si absent, vérifier le dépôt
git status
```

### Erreur "externally-managed-environment"

**Sur macOS récent** :
```bash
pip3 install --break-system-packages PyMuPDF pillow fuzzywuzzy python-levenshtein
```

### Permission refusée

```bash
chmod +x scripts/*.py
```

### Base de données corrompue

```bash
# Nettoyer et réindexer
rm data/articles.db
# Puis relancer et cliquer sur 📥 Index
```

---

## 💡 Astuces Pro

### Sauvegarde Complète

```bash
# Créer une archive
tar -czf LMA_backup_$(date +%Y%m%d).tar.gz LMA/

# Restaurer
tar -xzf LMA_backup_YYYYMMDD.tar.gz
```

### Optimiser les Performances

- Limiter à **~500 PDFs** pour performance optimale
- Le cache s'adapte automatiquement
- Fermer les miniatures si lenteur

### Organiser par Thématique

Créez des sous-dossiers dans `articles/` :

```
articles/
├── Machine_Learning/
├── Statistiques/
└── Neurosciences/
```

L'indexation scanne récursivement tous les sous-dossiers !

---

## 📊 Performance

| Critère | Valeur |
|---------|--------|
| **Indexation** | ~100 PDFs/min |
| **Recherche** | Instantanée (O(1) cache) |
| **Ouverture PDF** | <10ms (avec cache) |
| **Surlignage** | Temps réel |
| **Cache** | 15 pages en mémoire |
| **Préchargement** | ±2 pages adjacentes |

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! 

1. **Fork** le projet
2. Créez une **branche** : `git checkout -b feature/AmazingFeature`
3. **Commit** : `git commit -m 'Add AmazingFeature'`
4. **Push** : `git push origin feature/AmazingFeature`
5. Ouvrez une **Pull Request**

### Idées de Contributions

- [ ] Export annotations en PDF
- [ ] Tags personnalisés
- [ ] Notes de lecture
- [ ] Synchronisation cloud
- [ ] Mode présentation
- [ ] Export BibTeX automatique
- [ ] Support d'autres formats (EPUB, MOBI)

---

## 📝 TODO

- [x] Interface aux couleurs du Maroc 🇲🇦
- [x] Lecteur PDF avec annotations
- [x] Cache intelligent O(1)
- [x] Recherche instantanée
- [x] Thème clair/sombre
- [ ] Export annotations PDF
- [ ] Import BibTeX
- [ ] Mode tablette
- [ ] Application web (Flask)
- [ ] API REST

---

## 🎓 Cas d'Usage

### 👨‍🎓 Étudiants
- Organiser les articles de recherche
- Surligner les passages importants
- Préparer les examens

### 👨‍🔬 Chercheurs
- Gérer une bibliographie complète
- Annoter des centaines d'articles
- Rechercher rapidement

### 👨‍🏫 Professeurs
- Organiser les lectures de cours
- Recommander des articles
- Préparer les références

---

## 🛡️ Vie Privée

- ✅ **100% local** : aucune donnée envoyée en ligne
- ✅ Base de données SQLite sur votre machine
- ✅ Annotations sauvegardées localement
- ✅ Pas de tracking, pas de télémétrie

---

## 📄 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2024 LMA Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Remerciements

- **PyMuPDF (fitz)** pour le rendu PDF
- **Pillow** pour le traitement d'images
- **FuzzyWuzzy** pour la recherche floue
- **Tkinter** pour l'interface graphique
- Inspiration : Preview.app (macOS), WPS Office

---

## 📧 Contact

- **GitHub Issues** : [Signaler un bug](https://github.com/votre-username/LMA/issues)
- **Pull Requests** : [Contribuer](https://github.com/votre-username/LMA/pulls)
- **Discussions** : [Forum](https://github.com/votre-username/LMA/discussions)

---

## 📸 Screenshots

### Interface Principale
![Interface](https://via.placeholder.com/800x500/C1272D/FFFFFF?text=Interface+Principale)

*Tableau agrandi, couleurs du Maroc, recherche instantanée*

### Lecteur PDF
![Lecteur](https://via.placeholder.com/800x500/006233/FFFFFF?text=Lecteur+PDF)

*Surlignage, miniatures, navigation fluide*

### Annotations
![Annotations](https://via.placeholder.com/800x500/FFD700/000000?text=Annotations)

*4 couleurs, sauvegarde automatique, recherche*

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=votre-username/LMA&type=Date)](https://star-history.com/#votre-username/LMA&Date)

---

## 📊 Statistiques

![GitHub stats](https://github-readme-stats.vercel.app/api?username=votre-username&show_icons=true&theme=radical)

---

<div align="center">

**🇲🇦 Fait avec ❤️ pour la communauté académique**

[⬆ Retour en haut](#-lma---library-management-app)

</div>

---

*Dernière mise à jour : Janvier 2024*
