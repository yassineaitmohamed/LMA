# 📁 Project Structure

This document describes the organization of the LMA project.

## Repository Structure

```
LMA/
├── README.md                  # Main documentation
├── LICENSE                    # MIT License
├── requirements.txt           # Python dependencies
├── install.sh                # Installation script
│
├── interface_pro.py          # Main GUI application
├── lecteur_pdf_pro.py        # Advanced PDF reader
├── biblio_improved.py        # Library management system
│
├── config.example.json       # Example configuration
│
├── INSTALL.md                # Detailed installation guide
├── CONTRIBUTING.md           # Contribution guidelines
├── CHANGELOG.md              # Version history
├── SHORTCUTS.md              # Keyboard shortcuts reference
├── FAQ.md                    # Frequently asked questions
│
└── docs/                     # Additional documentation (to be created)
    ├── screenshots/          # Application screenshots
    ├── tutorials/            # User tutorials
    └── api/                  # API documentation
```

## User Directory Structure (After Installation)

```
~/Desktop/LMA/
├── articles/                 # Your PDF files
│   ├── Author_2023_Title.pdf
│   ├── Author_2023_Title.annotations.json
│   └── ...
│
├── data/                     # Application data
│   └── articles.db          # SQLite database
│
├── scripts/                  # Application files
│   ├── interface_pro.py
│   ├── lecteur_pdf_pro.py
│   └── biblio_improved.py
│
├── docs/                     # Documentation (copied during install)
│   ├── README.md
│   ├── INSTALL.md
│   └── ...
│
└── LMA.command              # macOS launcher (or .desktop on Linux)
```

## File Descriptions

### Core Application Files

#### `interface_pro.py`
Main GUI application using Tkinter. Handles:
- Library view and management
- Search interface
- Theme switching
- Button actions and menus
- Integration with PDF reader

**Key Classes:**
- `BibliothequeGUI`: Main application window

**Dependencies:**
- `tkinter`: GUI framework
- `biblio_improved`: Library management
- `lecteur_pdf_pro`: PDF reader

#### `lecteur_pdf_pro.py`
Advanced PDF reader with performance optimizations. Features:
- Intelligent caching system (LRU)
- Page preloading
- Annotation support
- Search functionality
- Export capabilities
- AI tools integration

**Key Classes:**
- `CacheIntelligent`: LRU cache for pages
- `GestionnaireAnnotations`: Annotation management
- `LecteurPDFPro`: Main PDF reader window

**Dependencies:**
- `PyMuPDF (fitz)`: PDF rendering
- `Pillow (PIL)`: Image processing
- `tkinter`: GUI components

#### `biblio_improved.py`
Library management and database operations. Handles:
- PDF indexing
- Metadata extraction
- Database operations
- Search functionality
- File system monitoring
- Auto-cleanup

**Key Classes:**
- `BibliothequeArticles`: Main library manager

**Dependencies:**
- `sqlite3`: Database
- `PyPDF2`: PDF text extraction
- `fuzzywuzzy`: Fuzzy search

### Configuration Files

#### `requirements.txt`
Python package dependencies with version specifications.

#### `config.example.json`
Example configuration file showing all available settings. Users can copy this to `~/.config/lma/config.json` and customize.

### Documentation Files

#### `README.md`
Main project documentation:
- Overview and features
- Installation quick start
- Usage basics
- Links to detailed docs

#### `INSTALL.md`
Comprehensive installation guide:
- System requirements
- Step-by-step instructions
- Platform-specific notes
- Troubleshooting

#### `CONTRIBUTING.md`
Guidelines for contributors:
- Code of conduct
- Development setup
- Coding standards
- Submission process

#### `CHANGELOG.md`
Version history and release notes:
- Features added
- Bugs fixed
- Breaking changes
- Migration guides

#### `SHORTCUTS.md`
Complete keyboard shortcuts reference:
- Navigation shortcuts
- Annotation shortcuts
- View controls
- Advanced features

#### `FAQ.md`
Frequently asked questions and answers:
- Installation issues
- Usage questions
- Performance tips
- Feature requests

### Scripts

#### `install.sh`
Automated installation script:
- Checks requirements
- Installs dependencies
- Creates directory structure
- Sets up launchers

### License

#### `LICENSE`
MIT License - permissive open-source license allowing commercial use, modification, and distribution.

## Data Files (Generated at Runtime)

### Database

#### `articles.db` (SQLite)
Stores article metadata:

**Table: articles**
```sql
CREATE TABLE articles (
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
```

### Annotation Files

#### `<pdf_name>.annotations.json`
JSON file storing annotations for each PDF:

```json
{
  "highlights": {
    "page_num": [
      {
        "rect": [x1, y1, x2, y2],
        "color": "yellow",
        "text": "highlighted text"
      }
    ]
  },
  "notes": {
    "page_num": [
      {
        "x": 100,
        "y": 200,
        "text": "note content",
        "timestamp": "2024-11-22 10:30:00"
      }
    ]
  },
  "bookmarks": [1, 5, 12]
}
```

## Configuration Files (User)

### `~/.config/lma/config.json`
User-specific configuration (optional):

```json
{
  "library": {
    "default_path": "~/Desktop/LMA/articles"
  },
  "reader": {
    "cache_size": 15,
    "default_theme": "dark"
  }
}
```

### `~/.config/lma/shortcuts.json`
Custom keyboard shortcuts (optional).

## Temporary Files

### Cache (In-Memory)
- PDF page renders (not stored on disk)
- Thumbnail images (generated on demand)
- Search indices (rebuilt as needed)

## Development Files (Not in Repository)

```
LMA/ (development)
├── .git/                     # Git repository data
├── .gitignore               # Git ignore rules
├── venv/                    # Virtual environment (not committed)
├── __pycache__/             # Python cache (not committed)
├── tests/                   # Test suite (to be added)
│   ├── test_biblio.py
│   ├── test_reader.py
│   └── test_interface.py
├── docs/                    # Generated documentation
│   └── build/
└── dist/                    # Distribution builds (not committed)
```

## Dependencies Graph

```
interface_pro.py
    ├── tkinter
    ├── biblio_improved.py
    │   ├── sqlite3
    │   ├── PyPDF2
    │   └── fuzzywuzzy
    └── lecteur_pdf_pro.py
        ├── tkinter
        ├── PyMuPDF (fitz)
        ├── Pillow (PIL)
        └── biblio_improved.py
```

## Code Organization

### Module Responsibilities

| Module | Responsibility | Dependencies |
|--------|---------------|--------------|
| `interface_pro.py` | GUI & user interaction | tkinter, biblio, lecteur |
| `lecteur_pdf_pro.py` | PDF rendering & annotations | PyMuPDF, PIL, tkinter |
| `biblio_improved.py` | Data management | sqlite3, PyPDF2, fuzzywuzzy |

### Data Flow

```
User Input
    ↓
interface_pro.py (GUI)
    ↓
biblio_improved.py (Data Layer)
    ↓
SQLite Database ↔ File System
    ↓
lecteur_pdf_pro.py (PDF Reader)
    ↓
PyMuPDF (Rendering) ↔ Annotations
```

## Adding New Features

### New Feature Checklist

1. **Core Implementation**
   - [ ] Add code to appropriate module
   - [ ] Follow coding standards
   - [ ] Add docstrings

2. **Testing**
   - [ ] Write unit tests
   - [ ] Test manually
   - [ ] Check performance

3. **Documentation**
   - [ ] Update README if needed
   - [ ] Add to CHANGELOG
   - [ ] Update relevant docs

4. **Integration**
   - [ ] Add to GUI if needed
   - [ ] Add keyboard shortcut
   - [ ] Update config.example.json

## File Naming Conventions

- **Python files**: `lowercase_with_underscores.py`
- **Documentation**: `UPPERCASE.md` for main docs, `lowercase.md` for supplementary
- **Config files**: `lowercase.json` or `lowercase.yaml`
- **Scripts**: `lowercase.sh` or `lowercase.command`

## Best Practices

### Code Organization
1. Group related functions together
2. Keep modules focused and cohesive
3. Use clear, descriptive names
4. Add comments for complex logic

### Documentation
1. Keep README concise, link to details
2. Update CHANGELOG with every release
3. Maintain FAQ with common issues
4. Document breaking changes clearly

### Version Control
1. Commit often with clear messages
2. Use feature branches
3. Tag releases with semantic versions
4. Keep main branch stable

## Future Structure (Planned)

```
LMA/ (future)
├── src/                     # Source code
│   ├── core/               # Core functionality
│   ├── gui/                # GUI components
│   ├── utils/              # Utility functions
│   └── plugins/            # Plugin system
├── tests/                  # Test suite
├── docs/                   # Documentation
│   ├── api/               # API reference
│   ├── tutorials/         # User tutorials
│   └── dev/               # Developer docs
├── resources/              # Icons, themes, etc.
├── locales/                # Translations
└── scripts/                # Utility scripts
```

---

**Last Updated**: 2024-11-22
**Version**: 1.0.0
