# 🚀 Publishing LMA to GitHub

Complete guide to publish your LMA repository on GitHub.

## Prerequisites

- [x] GitHub account created
- [x] Git installed on your computer
- [x] All project files ready

## Step-by-Step Guide

### 1. Create GitHub Repository

#### Via GitHub Website

1. Go to [github.com](https://github.com)
2. Click the **"+"** icon → **"New repository"**
3. Fill in the details:
   - **Repository name**: `LMA`
   - **Description**: `Library Management Application - Professional PDF library manager for academic research`
   - **Visibility**: Choose **Public** (recommended for open source)
   - **Initialize**: ☐ Don't check any boxes (we'll push existing code)
4. Click **"Create repository"**

#### Important Settings

After creating the repository:

1. **Go to Settings → General**
   - Set default branch to `main`
   - Enable Issues
   - Enable Discussions (recommended)

2. **Add Topics** (helps discovery):
   - `pdf-reader`
   - `library-management`
   - `academic-tools`
   - `python`
   - `tkinter`
   - `research-tools`
   - `annotation`
   - `macos`

3. **Update Repository Details**:
   - Website: Add your project website if any
   - Add relevant tags

### 2. Prepare Your Local Repository

```bash
# Navigate to your project directory
cd ~/Desktop/LMA

# If not already a git repository, initialize it
git init

# Create .gitignore if not exists
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/

# Virtual Environment
venv/
env/

# IDE
.vscode/
.idea/
*.swp
.DS_Store

# LMA Specific
data/
articles/
*.db
*.db-journal
*.annotations.json

# Logs
*.log
.cache/
EOF

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: LMA v1.0.0

- Complete library management system
- Advanced PDF reader with caching
- Annotation support
- Full documentation
- Installation scripts"

# Rename branch to main (if needed)
git branch -M main
```

### 3. Connect to GitHub

```bash
# Add GitHub remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/LMA.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main
```

### 4. Set Up GitHub Pages (Optional)

To create a project website:

1. Go to **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** → **/docs** (if you have a docs folder)
4. Click **Save**

Your site will be at: `https://YOUR-USERNAME.github.io/LMA/`

### 5. Create Release Tags

```bash
# Create and push first release tag
git tag -a v1.0.0 -m "Release v1.0.0 - Initial public release"
git push origin v1.0.0
```

On GitHub:
1. Go to **Releases → Create a new release**
2. Choose tag: `v1.0.0`
3. Release title: `LMA v1.0.0 - Initial Release`
4. Description: Copy from CHANGELOG.md
5. Attach files (optional): ZIP of project
6. Click **Publish release**

### 6. Set Up Branch Protection (Recommended)

1. Go to **Settings → Branches**
2. Add rule for `main` branch:
   - ☑ Require pull request reviews
   - ☑ Require status checks to pass
   - ☑ Include administrators

### 7. Add Repository Metadata

#### Create CITATION.cff

```bash
cat > CITATION.cff << 'EOF'
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
  - family-names: "Your Last Name"
    given-names: "Your First Name"
    orcid: "https://orcid.org/YOUR-ORCID-ID"
title: "LMA - Library Management Application"
version: 1.0.0
date-released: 2024-11-22
url: "https://github.com/YOUR-USERNAME/LMA"
license: MIT
EOF

git add CITATION.cff
git commit -m "Add citation metadata"
git push
```

#### Create FUNDING.yml (if you want donations)

```bash
mkdir -p .github
cat > .github/FUNDING.yml << 'EOF'
# Funding options (uncomment and add your accounts)
# github: [YOUR-GITHUB-USERNAME]
# patreon: YOUR-PATREON
# ko_fi: YOUR-KOFI
custom: ["https://paypal.me/YOUR-PAYPAL"]
EOF

git add .github/FUNDING.yml
git commit -m "Add funding options"
git push
```

### 8. Configure Issue Templates

```bash
mkdir -p .github/ISSUE_TEMPLATE

# Bug report template
cat > .github/ISSUE_TEMPLATE/bug_report.md << 'EOF'
---
name: Bug Report
about: Report a bug to help us improve
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
 - OS: [e.g., macOS 13.0]
 - Python: [e.g., 3.11.0]
 - LMA version: [e.g., 1.0.0]

**Additional context**
Any other information about the problem.
EOF

# Feature request template
cat > .github/ISSUE_TEMPLATE/feature_request.md << 'EOF'
---
name: Feature Request
about: Suggest a new feature
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

**Is your feature related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Other solutions you've considered.

**Additional context**
Any other context or screenshots.
EOF

git add .github/
git commit -m "Add issue templates"
git push
```

### 9. Add Badges to README

Add these badges to the top of your README.md:

```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/release/YOUR-USERNAME/LMA.svg)](https://github.com/YOUR-USERNAME/LMA/releases/)
[![GitHub stars](https://img.shields.io/github/stars/YOUR-USERNAME/LMA.svg)](https://github.com/YOUR-USERNAME/LMA/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/YOUR-USERNAME/LMA.svg)](https://github.com/YOUR-USERNAME/LMA/network)
[![GitHub issues](https://img.shields.io/github/issues/YOUR-USERNAME/LMA.svg)](https://github.com/YOUR-USERNAME/LMA/issues)
```

### 10. Enable GitHub Discussions

1. Go to **Settings → Features**
2. Enable **Discussions**
3. Create categories:
   - General
   - Q&A
   - Ideas
   - Show and Tell

### 11. Add Code of Conduct

```bash
# Use GitHub's template
# Go to repository → Insights → Community → Add → Code of Conduct
# Choose "Contributor Covenant"
```

Or create manually:

```bash
cat > CODE_OF_CONDUCT.md << 'EOF'
# Contributor Covenant Code of Conduct

## Our Pledge
We pledge to make participation in our project a harassment-free experience for everyone.

## Our Standards
Examples of behavior that contributes to a positive environment:
* Using welcoming and inclusive language
* Being respectful of differing viewpoints
* Accepting constructive criticism gracefully
* Focusing on what is best for the community

## Enforcement
Instances of abusive behavior may be reported to [your-email@example.com].

## Attribution
This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/).
EOF

git add CODE_OF_CONDUCT.md
git commit -m "Add Code of Conduct"
git push
```

### 12. Set Up GitHub Actions (CI/CD)

```bash
mkdir -p .github/workflows

cat > .github/workflows/tests.yml << 'EOF'
name: Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest]
        python-version: ['3.8', '3.9', '3.10', '3.11']

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    
    - name: Test imports
      run: |
        python -c "import biblio_improved"
        python -c "import interface_pro"
EOF

git add .github/workflows/
git commit -m "Add GitHub Actions CI"
git push
```

### 13. Add Screenshots

```bash
mkdir -p docs/screenshots

# Add your screenshots to this folder
# Then reference them in README.md:
# ![Main Interface](docs/screenshots/main_interface.png)
```

## Post-Publication Checklist

### Immediate Tasks

- [ ] Verify all files uploaded correctly
- [ ] Check README renders properly
- [ ] Test installation from GitHub
- [ ] Create first release (v1.0.0)
- [ ] Write release notes

### Marketing

- [ ] Share on social media (Twitter, LinkedIn, Reddit)
- [ ] Post on relevant forums
- [ ] Submit to awesome lists:
  - [awesome-python](https://github.com/vinta/awesome-python)
  - [awesome-python-applications](https://github.com/mahmoud/awesome-python-applications)
- [ ] Write blog post about the project
- [ ] Create demo video
- [ ] Submit to Product Hunt (optional)

### Community Building

- [ ] Respond to issues promptly
- [ ] Welcome first-time contributors
- [ ] Create good first issue labels
- [ ] Set up Discord/Slack (optional)
- [ ] Create project roadmap

### Documentation

- [ ] Add usage examples
- [ ] Create video tutorials
- [ ] Write blog posts
- [ ] Update FAQ regularly

### Maintenance

- [ ] Monitor issues and discussions
- [ ] Review and merge pull requests
- [ ] Update dependencies regularly
- [ ] Create releases for bug fixes
- [ ] Keep CHANGELOG updated

## Useful GitHub Commands

### Updating Your Repository

```bash
# After making local changes
git add .
git commit -m "Descriptive message"
git push

# Create a new release
git tag -a v1.0.1 -m "Bug fix release"
git push origin v1.0.1

# Update from GitHub
git pull origin main
```

### Managing Branches

```bash
# Create feature branch
git checkout -b feature/new-feature

# Push feature branch
git push -u origin feature/new-feature

# Merge back to main
git checkout main
git merge feature/new-feature
git push
```

### Handling Pull Requests

```bash
# Fetch PR to test locally
git fetch origin pull/ID/head:pr-ID
git checkout pr-ID

# If good, merge
git checkout main
git merge pr-ID
git push
```

## Troubleshooting

### Large Files

If you accidentally committed large files:

```bash
# Install git-lfs
brew install git-lfs  # macOS
# or: sudo apt install git-lfs  # Linux

# Track large files
git lfs track "*.pdf"
git add .gitattributes
git commit -m "Add git-lfs tracking"
```

### Remove Sensitive Data

If you committed sensitive data:

```bash
# Remove file from history
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch PATH/TO/FILE" \
  --prune-empty --tag-name-filter cat -- --all

# Force push
git push origin --force --all
```

**Better**: Use environment variables for secrets!

## Getting Help

- **GitHub Docs**: [docs.github.com](https://docs.github.com)
- **Git Docs**: [git-scm.com/doc](https://git-scm.com/doc)
- **GitHub Community**: [github.community](https://github.community)

---

**Congratulations! Your project is now on GitHub! 🎉**

Remember:
- Keep your repository active
- Respond to community feedback
- Regular updates maintain interest
- Good documentation attracts contributors

**Next Steps**: Check out GitHub's guide on [building community](https://docs.github.com/en/communities)
