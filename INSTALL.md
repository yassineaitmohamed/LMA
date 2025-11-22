# 📦 Installation Guide

Complete installation instructions for LMA (Library Management Application).

## 📋 Prerequisites

### System Requirements

- **Operating System**: macOS 10.15+, Linux (Ubuntu 20.04+, Fedora 35+), Windows 10+ (with minor adjustments)
- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (4GB+ recommended)
- **Display**: 1280x800 minimum (1920x1080+ recommended)
- **Storage**: 100MB for application + space for your PDF library

### Check Python Version

```bash
python3 --version
# Should show: Python 3.8.x or higher
```

If Python is not installed or version is too old:

**macOS:**
```bash
# Using Homebrew
brew install python@3.11
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install python3 python3-pip python3-tkinter
```

## 🚀 Quick Install

### Method 1: Automated (Recommended)

```bash
# Download and run install script
curl -o install.sh https://raw.githubusercontent.com/yourusername/LMA/main/install.sh
chmod +x install.sh
./install.sh
```

### Method 2: Manual Installation

#### Step 1: Clone Repository

```bash
cd ~/Desktop
git clone https://github.com/yourusername/LMA.git
cd LMA
```

#### Step 2: Install Python Dependencies

**Option A: Using pip (recommended)**

```bash
pip3 install -r requirements.txt
```

**Option B: Using system package manager (Linux)**

```bash
# Ubuntu/Debian
sudo apt install python3-pymupdf python3-pil python3-fuzzywuzzy

# Fedora
sudo dnf install python3-PyMuPDF python3-pillow python3-fuzzywuzzy
```

**macOS Note:** You may need to use `--break-system-packages` flag:

```bash
pip3 install -r requirements.txt --break-system-packages
```

#### Step 3: Create Directory Structure

```bash
# Create required directories
mkdir -p ~/Desktop/LMA/articles
mkdir -p ~/Desktop/LMA/data
mkdir -p ~/Desktop/LMA/scripts

# Copy application files
cp *.py ~/Desktop/LMA/scripts/
```

#### Step 4: Make Scripts Executable

```bash
chmod +x ~/Desktop/LMA/scripts/*.py
```

## ✅ Verify Installation

### Test Basic Functionality

```bash
cd ~/Desktop/LMA/scripts

# Test library module
python3 biblio_improved.py --help

# Test main interface
python3 interface_pro.py
```

You should see the LMA application window open.

### Check Dependencies

```bash
python3 -c "import fitz; import PIL; import fuzzywuzzy; print('✅ All dependencies OK')"
```

If you see "✅ All dependencies OK", installation is successful!

## 🎯 Post-Installation Setup

### 1. Add Your PDFs

```bash
# Copy or move your PDFs to the articles folder
cp /path/to/your/pdfs/*.pdf ~/Desktop/LMA/articles/

# Or create symbolic link to existing folder
ln -s /path/to/your/pdf/library ~/Desktop/LMA/articles
```

### 2. Initial Indexing

Launch LMA and click "🔄 Index" button, or use command line:

```bash
cd ~/Desktop/LMA/scripts
python3 biblio_improved.py --indexer
```

### 3. (Optional) Create Desktop Shortcut

**macOS:**

Create `LMA.command` file:

```bash
cat > ~/Desktop/LMA.command << 'EOF'
#!/bin/bash
cd ~/Desktop/LMA/scripts
python3 interface_pro.py
EOF

chmod +x ~/Desktop/LMA.command
```

**Linux:**

Create desktop entry:

```bash
cat > ~/.local/share/applications/lma.desktop << 'EOF'
[Desktop Entry]
Name=LMA
Comment=Library Management Application
Exec=python3 /home/$USER/Desktop/LMA/scripts/interface_pro.py
Icon=folder
Terminal=false
Type=Application
Categories=Office;Education;
EOF
```

## 🔧 Troubleshooting

### Common Issues

#### 1. "ModuleNotFoundError: No module named 'fitz'"

**Solution:**
```bash
pip3 install PyMuPDF --upgrade
```

#### 2. "Permission denied" errors

**Solution:**
```bash
chmod +x ~/Desktop/LMA/scripts/*.py
```

#### 3. "tkinter not found" (Linux)

**Solution:**
```bash
# Ubuntu/Debian
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

#### 4. Slow performance on Linux

**Solution:** Install Cairo backend for better rendering:
```bash
sudo apt install python3-cairo  # Ubuntu/Debian
sudo dnf install python3-cairo  # Fedora
```

#### 5. Display issues on HiDPI screens

**Solution:** Set environment variable before launch:
```bash
export GDK_SCALE=2
python3 interface_pro.py
```

### Database Issues

If you encounter database corruption:

```bash
# Backup existing database
cp ~/Desktop/LMA/data/articles.db ~/Desktop/LMA/data/articles.db.backup

# Reset database
rm ~/Desktop/LMA/data/articles.db

# Re-index
cd ~/Desktop/LMA/scripts
python3 biblio_improved.py --indexer
```

### Performance Optimization

#### Increase Cache Size

Edit `lecteur_pdf_pro.py`:

```python
# Find this line (around line 39)
self.cache = CacheIntelligent(max_size=10)

# Change to:
self.cache = CacheIntelligent(max_size=20)  # For machines with 16GB+ RAM
```

#### Disable Preloading (for slower systems)

Edit `lecteur_pdf_pro.py`:

```python
# Find preloading section and comment out
# self.precharger_pages_voisines()
```

## 📊 Verifying System Performance

Run benchmark:

```bash
cd ~/Desktop/LMA/scripts
python3 << 'EOF'
import time
import fitz

# Test PDF rendering speed
doc = fitz.open()
page = doc.new_page()
page.insert_text((50, 50), "Test")

start = time.time()
pix = page.get_pixmap()
elapsed = (time.time() - start) * 1000

print(f"Page render time: {elapsed:.2f}ms")
if elapsed < 20:
    print("✅ Excellent performance")
elif elapsed < 50:
    print("✅ Good performance")
else:
    print("⚠️ Consider optimization")
EOF
```

## 🎓 Next Steps

1. **Organize PDFs**: Follow naming convention (Author_Year_Title.pdf)
2. **Index Library**: Click "🔄 Index" in the application
3. **Learn Shortcuts**: Press `?` in PDF reader for help
4. **Customize Themes**: Use "🎨 Theme" button to switch modes
5. **Read Documentation**: Check `docs/` folder for advanced features

## 💡 Tips for Best Experience

1. **Naming Convention**: Use consistent PDF naming for better metadata extraction
2. **Regular Cleanup**: Use "🧹 Clean" button monthly to maintain database
3. **Backup**: Regularly backup `~/Desktop/LMA/data/` folder
4. **Performance**: Close other applications for best PDF reading experience
5. **Updates**: Pull latest changes regularly with `git pull`

## 🐛 Getting Help

If you encounter issues not covered here:

1. Check [GitHub Issues](https://github.com/yourusername/LMA/issues)
2. Read [Troubleshooting Guide](docs/troubleshooting.md)
3. Ask in [Discussions](https://github.com/yourusername/LMA/discussions)
4. Submit a bug report with:
   - Operating system and version
   - Python version
   - Error message (full traceback)
   - Steps to reproduce

## 🔄 Updating LMA

```bash
cd ~/Desktop/LMA
git pull origin main
pip3 install -r requirements.txt --upgrade
```

---

**Installation complete! 🎉**

Launch LMA with:
```bash
cd ~/Desktop/LMA/scripts
python3 interface_pro.py
```
