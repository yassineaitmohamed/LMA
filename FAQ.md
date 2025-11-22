# ❓ Frequently Asked Questions (FAQ)

## General Questions

### What is LMA?

LMA (Library Management Application) is a desktop application designed for researchers, PhD students, and academics to manage, search, and read their PDF library efficiently. It features an intelligent caching system, advanced PDF reader, and comprehensive annotation capabilities.

### Who is LMA for?

LMA is ideal for:
- **Researchers** managing large collections of academic papers
- **PhD Students** organizing literature for their thesis
- **Academics** preparing course materials
- **Anyone** who reads and annotates many PDF documents

### Is LMA free?

Yes! LMA is open-source software released under the MIT License. You can use, modify, and distribute it freely.

### What platforms does LMA support?

LMA supports:
- **macOS** 10.15+ (optimized for Apple Silicon M1/M2/M3)
- **Linux** (Ubuntu 20.04+, Fedora 35+, and other distributions)
- **Windows** 10+ (with minor adjustments)

## Installation & Setup

### How do I install LMA?

See our detailed [Installation Guide](INSTALL.md). Quick summary:

```bash
git clone https://github.com/yourusername/LMA.git
cd LMA
pip3 install -r requirements.txt
python3 install.sh
```

### What are the system requirements?

- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (4GB+ recommended)
- **Storage**: 100MB for app + space for PDFs
- **Display**: 1280x800 minimum (1920x1080+ recommended)

### Where should I put my PDF files?

By default, place your PDFs in `~/Desktop/LMA/articles/`. You can also configure a custom path in the settings.

### How do I name my PDFs for best results?

Use one of these formats:
- `Author_Year_Title.pdf` (e.g., `Smith_2023_Machine_Learning.pdf`)
- `Year_Author_Title.pdf` (e.g., `2023_Smith_Machine_Learning.pdf`)
- `Title_Year_Author.pdf` (e.g., `Machine_Learning_2023_Smith.pdf`)

### Do I need to manually index PDFs?

No, but it helps. LMA can auto-index on startup, or you can click the "🔄 Index" button to index all PDFs at once.

## Features & Usage

### How does the search work?

LMA searches across:
- Document titles
- Author names
- Full text content
- Annotations and notes

It uses fuzzy matching to find relevant results even with typos.

### What annotation types are supported?

LMA supports:
- **Highlights** with multiple colors
- **Text notes** with timestamps
- **Bookmarks** for quick navigation
- **Comments** on specific sections

### How fast is the PDF reader?

Performance benchmarks (MacBook Pro 2023):
- **Page load**: < 10ms (cached), ~50ms (uncached)
- **Transitions**: < 10ms (5x faster than standard viewers)
- **Cache hit rate**: 90%+ for sequential reading

### Can I export my annotations?

Yes! Export to:
- **Markdown** (.md)
- **Plain text** (.txt)
- **JSON** (.json)
- **BibTeX** (.bib)
- **PDF** with embedded annotations

### Does LMA work offline?

Yes! LMA is a fully offline application. No internet connection required.

### Can I customize the interface?

Yes! You can:
- Switch between dark and light themes
- Adjust zoom levels
- Configure keyboard shortcuts
- Customize colors and fonts (via config file)

## Technical Questions

### How does the caching system work?

LMA uses an intelligent LRU (Least Recently Used) cache:
- Stores 15 most recent pages by default
- Preloads ±2 pages in background
- Automatically manages memory
- 90%+ hit rate for sequential reading

### Where is my data stored?

- **Database**: `~/Desktop/LMA/data/articles.db` (SQLite)
- **Annotations**: `<pdf_name>.annotations.json` (next to PDF)
- **Config**: `~/.config/lma/config.json`
- **Cache**: In-memory only (cleared on exit)

### Is my data private?

Yes! All data is stored locally on your computer. LMA does not:
- Connect to external servers
- Track your usage
- Upload your documents
- Share any information

### Can I use LMA with cloud storage?

Yes! You can:
- Point LMA to a Dropbox/Google Drive folder
- Use symbolic links to cloud folders
- Keep database local, PDFs in cloud

### How much storage does LMA use?

- **Application**: ~50MB
- **Database**: ~1-10MB per 1000 articles
- **Annotations**: ~1-100KB per PDF
- **Cache**: 100-300MB RAM (not stored)

## Performance & Optimization

### Why is my application slow?

Common causes:
1. **Low RAM**: Close other applications
2. **Large PDFs**: Reduce cache size
3. **HDD**: Move to SSD for better performance
4. **Old Python**: Update to Python 3.11+

### How can I improve performance?

1. Increase cache size (16GB+ RAM systems)
2. Disable preloading on slower systems
3. Use SSD for storage
4. Close thumbnails panel when not needed
5. Reduce number of open applications

### Can I customize cache size?

Yes! Edit `lecteur_pdf_pro.py`:

```python
self.cache = CacheIntelligent(max_size=20)  # Default is 15
```

### Does LMA support large PDF files?

Yes! LMA efficiently handles:
- Documents with 1000+ pages
- Files larger than 100MB
- Scanned documents (with OCR)
- Complex layouts

## Troubleshooting

### LMA won't start. What should I do?

1. Check Python version: `python3 --version` (need 3.8+)
2. Verify dependencies: `pip3 list | grep -E "(PyMuPDF|PIL|fuzzywuzzy)"`
3. Check error messages in terminal
4. Try reinstalling: `pip3 install -r requirements.txt --upgrade`

### "Module not found" error

```bash
pip3 install PyMuPDF PyPDF2 Pillow fuzzywuzzy python-Levenshtein
```

On macOS, you may need:
```bash
pip3 install --break-system-packages PyMuPDF PyPDF2 Pillow fuzzywuzzy
```

### Database is corrupted

```bash
# Backup existing database
cp ~/Desktop/LMA/data/articles.db ~/Desktop/LMA/data/articles.db.backup

# Reset database
rm ~/Desktop/LMA/data/articles.db

# Re-index
cd ~/Desktop/LMA/scripts
python3 biblio_improved.py --indexer
```

### Annotations not saving

1. Check file permissions on PDF directory
2. Verify `.annotations.json` files can be created
3. Try manual save: Ctrl+S
4. Check disk space

### Search returns no results

1. Click "🔄 Index" to re-index
2. Check if PDFs are in correct folder
3. Try broader search terms
4. Use "🧹 Clean" to remove orphaned entries

### Display issues on HiDPI screens

Set environment variable:
```bash
export GDK_SCALE=2
python3 interface_pro.py
```

## Feature Requests

### Will LMA support mobile devices?

A mobile companion app is on our roadmap! Follow our [GitHub repository](https://github.com/yourusername/LMA) for updates.

### Can you add OCR support?

OCR for scanned PDFs is planned for a future release. You can track progress in our [roadmap](docs/ROADMAP.md).

### Will there be a web version?

Yes! A web interface for remote access is in development. Expected release: Q2 2025.

### Can LMA integrate with reference managers?

Integration with Zotero, Mendeley, and other reference managers is planned. See our [roadmap](docs/ROADMAP.md).

### Will LMA support e-books (EPUB, MOBI)?

E-book support is under consideration. Please upvote this feature request on GitHub if interested!

## Data & Privacy

### Can I export my entire library?

Yes! Use the database export function:
```bash
cd ~/Desktop/LMA/scripts
python3 biblio_improved.py --export library.json
```

### How do I backup my data?

Backup these directories:
```bash
cp -r ~/Desktop/LMA/data ~/Desktop/LMA_backup/
cp -r ~/Desktop/LMA/articles/*.annotations.json ~/Desktop/LMA_backup/annotations/
```

### Can I sync across multiple computers?

Currently, you need to manually sync the database and annotations. Cloud sync is planned for a future release.

### What happens to my annotations if I move/rename PDFs?

Annotations are stored in `.annotations.json` files. If you move/rename the PDF, you'll need to also move/rename the corresponding annotation file.

## Contributing

### How can I contribute?

See our [Contributing Guide](CONTRIBUTING.md). Ways to contribute:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation
- Translate to other languages

### I found a bug. Where do I report it?

Please report bugs on our [GitHub Issues](https://github.com/yourusername/LMA/issues) page. Include:
- Operating system and version
- Python version
- Error message (full traceback)
- Steps to reproduce

### Can I request a feature?

Absolutely! Submit feature requests on [GitHub Discussions](https://github.com/yourusername/LMA/discussions). Please explain:
- What problem it solves
- How it would work
- Why it would be useful

## Support

### Where can I get help?

- **Documentation**: Check [docs/](docs/) folder
- **FAQ**: This document
- **Issues**: [GitHub Issues](https://github.com/yourusername/LMA/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/LMA/discussions)

### Is there a user community?

Join our community:
- GitHub Discussions (Q&A, feature requests)
- Discord server (coming soon!)
- Reddit: r/LMA (planned)

### How do I stay updated?

- **Star** the repository on GitHub
- **Watch** for releases and updates
- Follow development in GitHub Discussions
- Subscribe to our newsletter (coming soon!)

## Licensing

### Can I use LMA commercially?

Yes! LMA is licensed under MIT License, which allows commercial use.

### Can I modify the code?

Yes! You're free to modify LMA for your needs. If you make improvements, consider contributing back to the project!

### Can I distribute modified versions?

Yes, as long as you include the original MIT License and give credit to the original authors.

## Additional Resources

- [Installation Guide](INSTALL.md)
- [User Manual](docs/USER_MANUAL.md)
- [Keyboard Shortcuts](SHORTCUTS.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

---

**Still have questions?**

Open a discussion on [GitHub](https://github.com/yourusername/LMA/discussions) or submit an issue!

**Last Updated**: 2024-11-22
