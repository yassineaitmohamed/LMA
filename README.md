# LMA

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



---

## 🚀 Installation depuis le Terminal

### Étape 1 : Télécharger les Fichiers

Créez un dossier `LMA` sur votre Bureau et placez-y les fichiers suivants :

```
Desktop/
└── LMA/
    ├── scripts/
    │   ├── interface_pro.py          # Interface principale
    │   ├── biblio_improved.py        # Gestion base de données
    │   └── lecteur_pdf_moderne.py    # Lecteur PDF
    ├── articles/                     # Vos PDFs ici
    └── data/                         # Base de données (créé auto)
```

### Étape 2 : Installer les Dépendances

Ouvrez le **Terminal** et exécutez :

```bash
# Installer les bibliothèques Python nécessaires
pip3 install PyMuPDF pillow fuzzywuzzy python-levenshtein
```

**Si vous avez une erreur sur macOS :**
```bash
pip3 install --break-system-packages PyMuPDF pillow fuzzywuzzy python-levenshtein
```

### Étape 3 : Vérifier l'Installation

```bash
# Vérifier que tout est installé
python3 -c "import fitz; import PIL; import fuzzywuzzy; print('✅ Tout est OK !')"
```

Si vous voyez "✅ Tout est OK !", vous pouvez continuer !

### Étape 4 : Lancer l'Application

```bash
# Aller dans le dossier LMA
cd ~/Desktop/LMA/scripts

# Lancer l'interface
python3 interface_pro.py
```

---

## 📁 Première Utilisation

### 1. Ajouter vos PDFs

Copiez vos articles PDF dans le dossier `articles/` :

```bash
# Exemple : copier des PDFs
cp /chemin/vers/vos/articles/*.pdf ~/Desktop/LMA/articles/
```

**Convention de nommage recommandée :**
- `Auteur_2024_Titre.pdf`
- Exemple : `Dupont_2024_Machine_Learning.pdf`

### 2. Indexer les PDFs

1. Ouvrez l'application
2. Cliquez sur le bouton **📥** (Index)
3. Attendez la fin de l'indexation
4. Vos articles apparaissent dans le tableau !

### 3. Utiliser l'Application

#### Rechercher un Article
- Tapez dans la barre de recherche 🔍
- La recherche filtre instantanément les résultats

#### Ouvrir un Article
- **Double-clic** sur l'article dans le tableau
- OU clic droit → "📖 Open PDF"

#### Marquer un Article
- Sélectionnez l'article
- Cliquez sur **📌 TO READ** (à lire)
- OU **✅ DONE** (déjà lu)

#### Filtrer les Articles
- **📚 ALL** : voir tous les articles
- **📖 TO READ** : voir seulement ceux à lire

---

## 🎨 Utiliser le Lecteur PDF

### Navigation

#### Au Clavier
- `←` `→` : Page précédente/suivante
- `Space` : Page suivante
- `Home` / `End` : Première/dernière page

#### Au Trackpad (MacBook)
- **Scroll 2 doigts** : Navigation fluide
- En haut/bas de page : Change automatiquement de page

### Zoom

- `⌘ +` / `⌘ -` : Zoomer/Dézoomer
- `⌘ 0` : Ajuster à la fenêtre
- **Double-clic** : Ajuster automatiquement

### Surlignage

1. Appuyer sur `⌘ P` pour activer le stylo
2. Choisir une couleur :
   - `⌘ Y` : Jaune 🟨
   - `⌘ R` : Rouge 🟥
   - `⌘ G` : Vert 🟩
   - `⌘ B` : Bleu 🟦
3. **Cliquer-glisser** sur le texte à surligner
4. Les annotations sont **sauvegardées automatiquement**

### Recherche dans le PDF

- `⌘ F` : Ouvrir la recherche
- Taper le mot à chercher
- Utiliser les flèches ◀ ▶ pour naviguer

### Miniatures

- `⌘ M` : Afficher les miniatures
- Cliquer sur une page pour y accéder

### Thème Clair/Sombre

- `⌘ T` : Changer de thème

---

## 🔧 Dépannage

### L'application ne démarre pas

**Problème** : `ModuleNotFoundError: No module named 'fitz'`

**Solution** :
```bash
pip3 install PyMuPDF
```

### Les PDFs ne s'ouvrent pas

**Problème** : "lecteur_pdf_moderne.py introuvable"

**Solution** :
```bash
# Vérifier que le fichier existe
ls ~/Desktop/LMA/scripts/lecteur_pdf_moderne.py

# Si absent, télécharger le fichier manquant
```

### Erreur "externally-managed-environment"

**Sur macOS récent** :
```bash
pip3 install --break-system-packages PyMuPDF pillow fuzzywuzzy python-levenshtein
```

**OU avec --user** :
```bash
pip3 install --user PyMuPDF pillow fuzzywuzzy python-levenshtein
```

### Python introuvable

**Vérifier Python** :
```bash
python3 --version
```

Si absent, installer depuis [python.org](https://www.python.org/downloads/)

### Permission refusée

```bash
# Donner les permissions d'exécution
chmod +x ~/Desktop/LMA/scripts/*.py
```

---

## 💡 Astuces Pro

### Créer un Raccourci

Pour lancer l'application d'un double-clic :

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

Maintenant, **double-cliquez** sur `LMA.command` pour lancer !

### Créer un Alias Terminal

```bash
# Ajouter à votre .zshrc (macOS) ou .bashrc (Linux)
echo "alias lma='cd ~/Desktop/LMA/scripts && python3 interface_pro.py'" >> ~/.zshrc

# Recharger
source ~/.zshrc

# Maintenant tapez juste :
lma
```

### Sauvegarde de la Bibliothèque

Vos données sont dans :
- `~/Desktop/LMA/data/articles.db` (base de données)
- `~/Desktop/LMA/articles/*.annotations.json` (surlignages)

**Sauvegarde complète** :
```bash
# Créer une archive
cd ~/Desktop
tar -czf LMA_backup_$(date +%Y%m%d).tar.gz LMA/

# Restaurer
tar -xzf LMA_backup_YYYYMMDD.tar.gz
```

---

## 📊 Structure des Fichiers

```
LMA/
├── scripts/
│   ├── interface_pro.py          # Interface principale (🇲🇦)
│   ├── biblio_improved.py        # Gestion BDD + cache
│   └── lecteur_pdf_moderne.py    # Lecteur PDF optimisé
│
├── articles/                     # 📚 VOS PDFs ICI
│   ├── Yassine ait mohamed_2025_LMA.pdf
│   
├── data/                         # Créé automatiquement
│   └── articles.db              # Base de données SQLite
│
└── LMA.command                   # Raccourci (optionnel)

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
| Raccourci | Action |
|-----------|--------|
| `←` `→` | Page précédente/suivante |
| `Space` | Page suivante |
| `⌘ +` `-` | Zoom in/out |
| `⌘ 0` | Ajuster |
| `⌘ F` | Rechercher |
| `⌘ P` | Mode stylo |
| `⌘ Y` `R` `G` `B` | Couleurs |
| `⌘ M` | Miniatures |
| `⌘ T` | Thème |
| `⌘ W` | Fermer |

---

## 🆘 Support

### Problèmes Courants

**Q : L'indexation est lente**
- Normal pour le premier scan
- Le cache accélère les suivantes

**Q : Les surlignages disparaissent**
- Vérifiez les fichiers `.annotations.json`
- Vérifiez les permissions du dossier

**Q : Le scroll ne fonctionne pas**
- Sur MacBook : utilisez 2 doigts
- Au clavier : utilisez les flèches

**Q : Erreur "self.or invalid syntax"**
- Version obsolète du fichier
- Re-téléchargez la dernière version

### Obtenir de l'Aide

1. Vérifiez ce guide
2. Testez en mode standalone : `python3 lecteur_pdf_moderne.py`
3. Vérifiez les logs d'erreur dans le terminal

---

## 📝 Notes Importantes

### Compatibilité PDF
- ✅ PDFs texte (recherchable)
- ✅ PDFs scannés (affichage seulement)
- ⚠️ PDFs protégés (lecture seule)







**🇲🇦 Profitez de LMA pour organiser vos articles scientifiques ! 📚**
