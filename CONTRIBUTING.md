# 🤝 Contributing to LMA

Thank you for your interest in contributing to LMA! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive experience for everyone. We expect all contributors to:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- Familiarity with PDF processing and Tkinter
- Understanding of the project structure

### Areas for Contribution

We welcome contributions in:

- **Bug Fixes**: Fix reported issues
- **Features**: Add new functionality
- **Documentation**: Improve guides and docstrings
- **Testing**: Add unit tests and integration tests
- **Performance**: Optimize code and algorithms
- **UI/UX**: Enhance interface and user experience
- **Localization**: Translate to other languages

## 🔧 Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/yourusername/LMA.git
cd LMA
git remote add upstream https://github.com/originalauthor/LMA.git
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

### 3. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

## 🛠️ Making Changes

### Code Organization

```
LMA/
├── interface_pro.py       # Main GUI application
├── lecteur_pdf_pro.py     # PDF reader with advanced features
├── biblio_improved.py     # Library management and database
├── docs/                  # Documentation
├── tests/                 # Test suite
└── utils/                 # Utility functions
```

### Coding Guidelines

#### Python Style

Follow PEP 8 with these specifications:

```python
# Good: Clear, documented, typed
def indexer_article(self, chemin_pdf: Path) -> bool:
    """
    Index a PDF article in the database.
    
    Args:
        chemin_pdf: Path to the PDF file
        
    Returns:
        True if successfully indexed, False otherwise
    """
    if not chemin_pdf.exists():
        return False
    # ... implementation
```

#### Naming Conventions

- **Variables**: `snake_case` (e.g., `nom_fichier`, `cache_intelligent`)
- **Functions**: `snake_case` (e.g., `indexer_article`, `nettoyer_base`)
- **Classes**: `PascalCase` (e.g., `BibliothequeArticles`, `CacheIntelligent`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_CACHE_SIZE`, `DEFAULT_THEME`)

#### Comments

```python
# Good: Explain WHY, not WHAT
# Use LRU cache to avoid re-rendering frequently accessed pages
self.cache = CacheIntelligent(max_size=15)

# Bad: States the obvious
# Create cache
self.cache = CacheIntelligent(max_size=15)
```

#### Docstrings

Use Google-style docstrings:

```python
def rechercher(self, requete: str, limite: int = None) -> List[Dict]:
    """
    Search for articles by title, authors, or content.
    
    Args:
        requete: Search query string
        limite: Maximum number of results to return (optional)
        
    Returns:
        List of dictionaries containing article information
        
    Example:
        >>> biblio = BibliothequeArticles()
        >>> results = biblio.rechercher("quantum", limite=5)
        >>> print(len(results))
        5
    """
```

### UI/UX Guidelines

- **Consistency**: Follow existing color schemes and layouts
- **Accessibility**: Ensure sufficient contrast ratios (WCAG AA)
- **Responsiveness**: Test on different screen sizes
- **Performance**: Keep UI responsive (< 100ms for interactions)
- **Feedback**: Provide clear user feedback for all actions

### Performance Considerations

- **Cache**: Use caching for expensive operations
- **Threading**: Use threads for I/O operations, not CPU-bound tasks
- **Memory**: Be mindful of memory usage for large documents
- **Profiling**: Profile before optimizing

```python
# Good: Non-blocking UI
def operation_longue(self):
    def worker():
        # Expensive operation
        result = traitement_lourd()
        self.root.after(0, lambda: self.afficher_resultat(result))
    
    threading.Thread(target=worker, daemon=True).start()
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_biblio.py

# Run with coverage
python -m pytest --cov=. --cov-report=html
```

### Writing Tests

```python
import unittest
from pathlib import Path
from biblio_improved import BibliothequeArticles

class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.test_dir = Path("test_articles")
        self.test_dir.mkdir(exist_ok=True)
        self.biblio = BibliothequeArticles(str(self.test_dir))
    
    def tearDown(self):
        """Clean up after tests"""
        # Clean up test files
        pass
    
    def test_indexer_article(self):
        """Test article indexing"""
        # Create test PDF
        # Test indexing
        # Assert results
        pass
```

### Test Coverage

Aim for:
- **Core functionality**: 90%+ coverage
- **UI code**: 60%+ coverage
- **Utility functions**: 95%+ coverage

## 📝 Submitting Changes

### Commit Messages

Follow conventional commits:

```bash
# Format: <type>(<scope>): <description>

feat(reader): add thumbnail navigation panel
fix(search): correct fuzzy matching algorithm
docs(readme): update installation instructions
refactor(cache): optimize LRU implementation
test(biblio): add tests for metadata extraction
perf(render): reduce page load time by 50%
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `perf`: Performance improvement
- `test`: Testing
- `chore`: Maintenance

### Pull Request Process

1. **Update Documentation**
   - Update README if needed
   - Add/update docstrings
   - Update CHANGELOG.md

2. **Test Your Changes**
   ```bash
   python -m pytest
   python interface_pro.py  # Manual testing
   ```

3. **Commit and Push**
   ```bash
   git add .
   git commit -m "feat(reader): add thumbnail navigation"
   git push origin feature/your-feature-name
   ```

4. **Create Pull Request**
   - Go to GitHub and create PR
   - Fill out PR template
   - Link related issues
   - Request review

5. **Address Review Comments**
   - Make requested changes
   - Push updates
   - Mark conversations as resolved

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] All tests pass
- [ ] Added new tests
- [ ] Manual testing completed

## Screenshots (if UI changes)
[Add screenshots]

## Checklist
- [ ] Code follows style guidelines
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings
```

## 🐛 Bug Reports

### Before Reporting

1. Check existing issues
2. Update to latest version
3. Try to reproduce consistently

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Screenshots**
If applicable

**Environment:**
- OS: [e.g., macOS 13.0]
- Python: [e.g., 3.11.0]
- LMA version: [e.g., 1.0.0]

**Additional Context**
Any other relevant information
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Problem It Solves**
What problem does this address?

**Proposed Solution**
How would you implement this?

**Alternatives Considered**
What other approaches did you consider?

**Additional Context**
Mockups, examples, etc.
```

## 🎯 Development Priorities

### High Priority
- Bug fixes
- Performance improvements
- Security patches
- Documentation improvements

### Medium Priority
- New features requested by users
- UI/UX enhancements
- Test coverage improvements

### Low Priority
- Code refactoring
- Nice-to-have features
- Experimental features

## 📚 Resources

### Documentation
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)

### Tools
- **Linting**: `pylint`, `flake8`
- **Formatting**: `black`, `autopep8`
- **Testing**: `pytest`, `unittest`
- **Type Checking**: `mypy`

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant documentation

## 📧 Questions?

- Open a [Discussion](https://github.com/yourusername/LMA/discussions)
- Join our community chat
- Email: your-email@example.com

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to LMA! 🚀**

Every contribution, no matter how small, makes a difference.
