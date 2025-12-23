# 🚀 LMA - Literature Management Assistant

**Professional PDF Library Manager for Academic Research**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)]()
[![Stars](https://img.shields.io/github/stars/yassineaitmohamed/LMA?style=social)](https://github.com/yassineaitmohamed/LMA/stargazers)

LMA is a powerful desktop application designed for researchers, PhD students, and academics to efficiently manage, search, and read their PDF library. Built with performance and usability in mind, it features an intelligent caching system, ultra-fast PDF reader, and comprehensive annotation capabilities.

---

## 📸 Screenshots

### 🗂️ Main Interface - Library Management
<img src="docs/screenshots/main_interface.png" alt="LMA Main Interface" width="800"/>

*Organize your research library with folders (articles, scripts, data)*

### 📁 File Organization
<img src="docs/screenshots/folders.png" alt="Folder Structure" width="800"/>

*Three main folders: articles (PDFs), scripts (Python files), data (database)*

### 📄 Scripts Overview
<img src="docs/screenshots/scripts.png" alt="Python Scripts" width="800"/>

*Core Python files: interface_pro.py, biblio_improved.py, lecteurpdf_fast.py, lecteurpdf.py*

---

## ✨ Key Features

### 📚 Library Management
- **Automatic Indexing**: Scan and index PDF files with metadata extraction
- **Smart Search**: Full-text fuzzy search across titles, authors, keywords, and content
- **Reading Status**: Track articles with "To Read" tags and filters
- **Auto-Cleanup**: Automatically removes database entries for deleted files
- **Multiple Formats**: Support for various PDF naming conventions
- **Hash-Based Detection**: Prevents duplicate entries

### 🚀 Ultra-Fast PDF Reader
- **Intelligent Caching**: LRU cache with 15 pages + preloading (±2 pages)
- **< 10ms Page Transitions**: 5x faster than standard PDF viewers
- **Advanced Annotations**: Multi-color highlighting, notes, bookmarks, favorites
- **Search with Counter**: Instant full-text search with result navigation
- **Thumbnail Navigation**: Dynamic thumbnail panel for quick page jumps
- **Dual Theme**: Professional dark/light modes (Oxford/UdeS colors)
- **20+ Keyboard Shortcuts**: Power user workflow optimization

### 🤖 AI Tools Integration
- **Smart Summary**: AI-powered article summarization
- **Key Points Extraction**: Extract main concepts and findings
- **Content Analysis**: Analyze document structure and topics
- **Citation Generator**: Export in multiple formats (Markdown, TXT, JSON, BibTeX)

### 🎨 Modern User Interface
- **Clean Design**: Professional, distraction-free interface
- **Oxford/UdeS Themes**: Academic color schemes (dark/light)
- **Responsive Layout**: Optimized for 13"+ displays
- **Performance Stats**: Real-time cache hit rate and search metrics
- **Miniature Preview**: Visual page navigation

---

## 📋 System Requirements

### Minimum Requirements
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: 500MB for application + space for your PDFs
- **Display**: 1400x900 minimum resolution

### Supported Operating Systems
- ✅ **macOS**: 10.14+ (Mojave and later)
- ✅ **Linux**: Ubuntu 20.04+, Debian 10+, Fedora 32+
- ✅ **Windows**: 10/11 (with Python 3.8+)

### Dependencies
- PyMuPDF (fitz) - Fast PDF rendering
- PyPDF2 - PDF metadata extraction
- fuzzywuzzy - Fuzzy string matching
- python-Levenshtein - Fast string comparison
- Pillow (PIL) - Image processing
- tkinter - GUI framework (usually included with Python)

---

## 🔧 Complete Installation Guide

### Step 1: Install Python

#### macOS
```bash
# Check if Python is installed
python3 --version

# If not installed, install via Homebrew
brew install python3

# Or download from python.org
# https://www.python.org/downloads/
```

#### Linux (Ubuntu/Debian)
```bash
# Update package list
sudo apt update

# Install Python and tkinter
sudo apt install python3 python3-pip python3-tk

# Verify installation
python3 --version
pip3 --version
```

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer and **CHECK "Add Python to PATH"**
3. Verify in Command Prompt:
   ```cmd
   python --version
   pip --version
   ```

---

### Step 2: Clone or Download LMA

#### Option A: Clone with Git (Recommended)

```bash
# Install git if not already installed
# macOS: brew install git
# Linux: sudo apt install git
# Windows: download from git-scm.com

# Clone the repository
cd ~/Desktop
git clone https://github.com/yassineaitmohamed/LMA.git
cd LMA
```

#### Option B: Download ZIP

1. Go to https://github.com/yassineaitmohamed/LMA
2. Click **Code** → **Download ZIP**
3. Extract to Desktop → `LMA` folder

---

### Step 3: Install Python Dependencies

```bash
# Navigate to LMA directory
cd ~/Desktop/LMA

# Install all dependencies at once
pip3 install -r requirements.txt

# Or install manually one by one
pip3 install PyMuPDF
pip3 install PyPDF2
pip3 install fuzzywuzzy
pip3 install python-Levenshtein
pip3 install Pillow
```

**For Windows users:**
```cmd
cd %USERPROFILE%\Desktop\LMA
pip install -r requirements.txt
```

**If you get permission errors:**
```bash
# Install for current user only
pip3 install --user -r requirements.txt
```

---

### Step 4: Create Directory Structure

LMA needs this folder structure on your Desktop:

```
~/Desktop/LMA/
├── articles/          # Place your PDF files here
├── data/              # Database (auto-created)
└── scripts/           # Python application files
    ├── interface_pro.py
    ├── biblio_improved.py
    ├── lecteurpdf_fast.py
    └── lecteurpdf.py
```

**Create the directories:**

#### macOS / Linux
```bash
cd ~/Desktop/LMA
mkdir -p articles data scripts

# Move Python files to scripts folder
mv *.py scripts/ 2>/dev/null || true

# Or copy if you want to keep originals
cp interface_pro.py biblio_improved.py lecteurpdf_fast.py lecteurpdf.py scripts/
```

#### Windows
```cmd
cd %USERPROFILE%\Desktop\LMA
mkdir articles
mkdir data
mkdir scripts

rem Move Python files
move *.py scripts\
```

---

### Step 5: Add Your PDF Files

Copy your research papers to the articles folder:

```bash
# Copy individual PDFs
cp ~/Documents/research_paper.pdf ~/Desktop/LMA/articles/

# Copy entire folder
cp -r ~/Documents/Research/*.pdf ~/Desktop/LMA/articles/

# Or simply drag and drop PDFs into the articles folder
```

**Tip**: You can organize PDFs in subfolders:
```
articles/
├── Machine_Learning/
├── Mathematics/
└── Biology/
```

LMA will scan all subfolders automatically!

---

### Step 6: Launch LMA

#### macOS / Linux
```bash
cd ~/Desktop/LMA/scripts
python3 interface_pro.py
```

#### Windows
```cmd
cd %USERPROFILE%\Desktop\LMA\scripts
python interface_pro.py
```

**First launch will:**
1. Create the database (`data/articles.db`)
2. Open the main LMA window
3. Show an empty library (click 🔄 to scan PDFs)

---

### Step 7: Index Your PDF Library

1. Click the **🔄 Refresh** button in the toolbar
2. LMA will scan all PDFs in the `articles/` folder
3. Wait for indexing to complete (shows progress)
4. Your articles will appear in the list!

**What gets indexed:**
- Filename and full path
- Title, authors, year (extracted from filename)
- Keywords and content (extracted from PDF)
- File hash (for duplicate detection)

---

## 🚀 Quick Start Guide

### First Time Setup (5 Minutes)

1. **Launch LMA**
   ```bash
   cd ~/Desktop/LMA/scripts
   python3 interface_pro.py
   ```

2. **Index Your PDFs**
   - Click **🔄 Refresh** button
   - Wait for scan to complete

3. **Search for Articles**
   - Type in the search bar
   - Try searching by:
     - Author name: `Smith`
     - Year: `2023`
     - Keywords: `machine learning`
     - Title: `neural networks`

4. **Open a PDF**
   - Double-click any article
   - Ultra-fast PDF reader opens instantly

5. **Mark as "To Read"**
   - Select an article
   - Click **📕 Mark to Read**
   - Filter by reading status

---

## 📖 Usage Guide

### Library Management

#### Searching
- **Fuzzy Search**: Type partial words, typos work!
- **Search in**: Filenames, titles, authors, keywords, content
- **Real-time**: Results update as you type

#### Filtering
- **All Articles**: Show entire library
- **To Read**: Show only unread articles
- **Read**: Show finished articles (coming soon)

#### Organizing
- **Mark to Read**: Flag important papers
- **Auto-Cleanup**: Removes entries for deleted PDFs
- **Refresh**: Re-scan library for new files

### PDF Reading

#### Navigation
- **Arrow Keys**: `←` `→` Previous/Next page
- **Page Up/Down**: Jump multiple pages
- **Home/End**: First/Last page
- **Mouse**: Click page thumbnails

#### View Controls
- **Zoom**: `Ctrl/Cmd +` `-` `0`
- **Fullscreen**: `F11`
- **Thumbnails**: `Ctrl/Cmd M`

#### Annotations
- **Highlight**: Select text → Choose color
- **Notes**: `Ctrl/Cmd N` → Add note
- **Bookmarks**: `Ctrl/Cmd B` → Mark page
- **Export**: `Ctrl/Cmd E` → Save annotations

#### Search in PDF
- **Find**: `Ctrl/Cmd F`
- **Next Result**: `F3` or `Enter`
- **Previous**: `Shift F3`

#### AI Tools
- **Summarize**: Generate article summary
- **Extract Key Points**: Get main findings
- **Analyze**: Content structure analysis
- **Export Citations**: Multiple formats

---

## ⌨️ Complete Keyboard Shortcuts

### Main Window
| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd F` | Focus search box |
| `Ctrl/Cmd R` | Refresh library |
| `Ctrl/Cmd T` | Toggle dark/light theme |
| `Enter` | Open selected article |
| `Delete` | Remove selected entry |
| `Ctrl/Cmd Q` | Quit application |

### PDF Reader - Navigation
| Shortcut | Action |
|----------|--------|
| `→` or `Space` | Next page |
| `←` or `Shift Space` | Previous page |
| `Page Down` | Jump 5 pages forward |
| `Page Up` | Jump 5 pages back |
| `Home` | First page |
| `End` | Last page |
| `G` | Go to page number |

### PDF Reader - View
| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd +` | Zoom in |
| `Ctrl/Cmd -` | Zoom out |
| `Ctrl/Cmd 0` | Reset zoom (100%) |
| `F11` | Toggle fullscreen |
| `Ctrl/Cmd M` | Show/hide thumbnails |

### PDF Reader - Features
| Shortcut | Action |
|----------|--------|
| `Ctrl/Cmd F` | Search in document |
| `F3` | Next search result |
| `Shift F3` | Previous search result |
| `Ctrl/Cmd N` | Add note |
| `Ctrl/Cmd B` | Toggle bookmark |
| `Ctrl/Cmd H` | Toggle highlights |
| `Ctrl/Cmd S` | Save annotations |
| `Ctrl/Cmd E` | Export annotations |
| `Ctrl/Cmd T` | Toggle theme |
| `Ctrl/Cmd W` | Close PDF |
| `Esc` | Exit fullscreen/Close |

---

## 🎨 Customization

### Themes

LMA includes professional color schemes:

**Dark Themes:**
- 🎓 **Oxford Dark**: Classic academic style (#002147)
- 🟢 **UdeS Dark**: University of Sherbrooke green (#00a650)

**Light Themes:**
- ☀️ **Clean Beige**: Comfortable daytime reading (#f5f5dc)
- 📄 **Professional**: Crisp and modern

Toggle theme: Click theme button or press `Ctrl/Cmd T`

### Custom Configuration

Create `config.json` in the LMA folder:

```json
{
  "library_path": "~/Desktop/LMA/articles",
  "database_path": "~/Desktop/LMA/data/articles.db",
  "theme": "dark",
  "cache_size": 15,
  "preload_pages": 2,
  "default_zoom": 1.0,
  "auto_cleanup": true
}
```

### Cache Settings

Edit `lecteurpdf_fast.py`:

```python
# Adjust cache size (default: 15 pages)
self.cache = CacheIntelligent(max_size=20)

# Adjust preloading (default: ±2 pages)
self.preload_distance = 3
```

---

## 🐛 Troubleshooting

### Application Won't Start

**Problem**: `ModuleNotFoundError` or import errors

**Solution**:
```bash
# Verify Python version (need 3.8+)
python3 --version

# Reinstall dependencies
pip3 install --upgrade -r requirements.txt

# Try installing each package separately
pip3 install PyMuPDF PyPDF2 fuzzywuzzy python-Levenshtein Pillow
```

### PDFs Not Showing

**Problem**: Library appears empty after clicking Refresh

**Solutions**:
1. Check PDFs are in `~/Desktop/LMA/articles/`
2. Verify file permissions: `ls -la ~/Desktop/LMA/articles/`
3. Check console for error messages
4. Try manual cleanup: Click **🧹 Clean Database**

### Slow Performance

**Problem**: PDF loading or search is slow

**Solutions**:
- Close other resource-intensive applications
- Reduce cache size in settings
- Update to latest version: `git pull origin main`
- Check available disk space: `df -h`
- On macOS: Check Activity Monitor for memory pressure

### Database Errors

**Problem**: SQLite errors or corrupted database

**Solution**:
```bash
# Backup first
cp ~/Desktop/LMA/data/articles.db ~/Desktop/articles_backup.db

# Delete and rebuild
rm ~/Desktop/LMA/data/articles.db

# Restart LMA - database will be recreated
# Then click Refresh to re-index PDFs
```

### macOS Permission Issues

**Problem**: "Operation not permitted" or access denied

**Solution**:
1. Open **System Preferences** → **Security & Privacy**
2. Click **Privacy** tab
3. Select **Full Disk Access**
4. Click **+** and add Terminal.app
5. Restart Terminal and try again

### Linux tkinter Not Found

**Problem**: `ModuleNotFoundError: No module named 'tkinter'`

**Solution**:
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

### Windows Path Issues

**Problem**: Can't find files or folders

**Solution**:
```cmd
# Use absolute paths
cd C:\Users\YourUsername\Desktop\LMA\scripts
python interface_pro.py

# Or set environment variable
set PYTHONPATH=C:\Users\YourUsername\Desktop\LMA\scripts
```

---

## 📊 Performance Optimization

### Cache Statistics

LMA displays real-time performance metrics:
- **Cache Hit Rate**: Should be 85%+ for sequential reading
- **Average Load Time**: < 100ms per page
- **Search Speed**: < 50ms for 1000+ documents

### Optimization Tips

1. **SSD vs HDD**: Use SSD for better performance
2. **Memory**: 8GB+ RAM recommended for large libraries
3. **PDF Size**: Keep individual PDFs under 50MB when possible
4. **Indexing**: Index once, search many times (fast!)
5. **Cache Size**: Increase for more RAM (15-30 pages optimal)

---

## 🎯 PDF Naming Best Practices

For optimal metadata extraction, name your PDFs consistently:

### Recommended Formats

1. **Author_Year_Title.pdf**
   ```
   Smith_2023_Machine_Learning_Survey.pdf
   Jones_2024_Deep_Neural_Networks.pdf
   ```

2. **Year_Author_Title.pdf**
   ```
   2023_Smith_Machine_Learning_Survey.pdf
   2024_Jones_Deep_Neural_Networks.pdf
   ```

3. **Title_Year_Author.pdf**
   ```
   Machine_Learning_Survey_2023_Smith.pdf
   Deep_Neural_Networks_2024_Jones.pdf
   ```

### Tips
- Use underscores `_` not spaces (better compatibility)
- Include year for easy chronological sorting
- Keep author last name only
- Avoid special characters: `/ \ : * ? " < > |`

---

## 🔧 Advanced Configuration

### Custom Paths

Edit `biblio_improved.py` to change default locations:

```python
# Line ~30
base_dir = Path.home() / "Desktop" / "LMA"  # Default

# Change to custom location
base_dir = Path("/path/to/your/research/library")
```

### Multiple Libraries

You can run multiple LMA instances with different libraries:

```bash
# Instance 1: Main research
cd ~/Desktop/LMA-Research/scripts
python3 interface_pro.py

# Instance 2: Teaching materials
cd ~/Desktop/LMA-Teaching/scripts
python3 interface_pro.py
```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- How to submit bug reports
- Feature request process
- Pull request workflow

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Make your changes
4. Test thoroughly
5. Commit with clear message
   ```bash
   git commit -m "Add amazing feature: description"
   ```
6. Push and create Pull Request

---

## 📝 Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

### Current Version: 1.0.0
- ✅ Core library management
- ✅ Ultra-fast PDF reader
- ✅ Advanced search and filtering
- ✅ Annotations system
- ✅ Dark/Light themes
- ✅ Cross-platform support

### Upcoming: 1.1.0
- 🔜 Windows native support
- 🔜 Cloud sync (Google Drive, Dropbox)
- 🔜 Export to BibTeX
- 🔜 Enhanced AI features
- 🔜 Multi-language UI

---

## 🆘 Getting Help

### Documentation
- 📖 [Installation Guide](INSTALLATION.md) - Detailed setup instructions
- 🚀 [Quick Start](QUICKSTART.md) - Get started in 5 minutes
- ❓ [FAQ](FAQ.md) - Frequently asked questions
- 🤝 [Contributing](CONTRIBUTING.md) - How to contribute

### Community & Support
- 💬 [GitHub Discussions](https://github.com/yassineaitmohamed/LMA/discussions) - Ask questions
- 🐛 [Issue Tracker](https://github.com/yassineaitmohamed/LMA/issues) - Report bugs
- 📧 [Contact Author](https://github.com/yassineaitmohamed) - Direct contact

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR**: You can freely use, modify, and distribute this software, even for commercial purposes, as long as you include the original copyright notice.

---

## 👨‍💻 Author

**Yassine Ait Mohamed**
- 🎓 PhD Student in Mathematics
- 🏛️ University of Sherbrooke
- 🌐 GitHub: [@yassineaitmohamed](https://github.com/yassineaitmohamed)
- 📧 Contact: [via GitHub](https://github.com/yassineaitmohamed)

---

## 🙏 Acknowledgments

### Technology Stack
- 🐍 **Python** - Programming language
- 🖼️ **Tkinter** - GUI framework
- 📄 **PyMuPDF (fitz)** - Fast PDF rendering
- 📚 **PyPDF2** - PDF metadata extraction
- 🔍 **fuzzywuzzy** - Fuzzy string matching
- 🖼️ **Pillow** - Image processing

### Inspiration
- Academic researchers worldwide 🌍
- The open-source community ❤️
- University of Sherbrooke 🎓
- PhD students' workflow needs

### Special Thanks
- Contributors and testers
- Everyone who starred the repo ⭐
- The Python community
- Academia for continuous inspiration

---

## 🌟 Star History

If you find LMA useful, please consider:
- ⭐ **Star the repository**
- 🍴 **Fork and contribute**
- 📢 **Share with colleagues**
- 💬 **Provide feedback**

---

**Made with ❤️ for researchers and academics**

*Empowering research through better literature management*
