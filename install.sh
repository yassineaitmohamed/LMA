#!/bin/bash

###############################################################################
# LMA (Library Management Application) - Installation Script
# 
# This script automates the installation of LMA on macOS and Linux systems.
# It will:
#   1. Check system requirements
#   2. Install Python dependencies
#   3. Create directory structure
#   4. Set up the application
#   5. Create desktop shortcuts (optional)
#
# Usage:
#   chmod +x install.sh
#   ./install.sh
###############################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
INSTALL_DIR="$HOME/Desktop/LMA"
REQUIRED_PYTHON_VERSION="3.8"

###############################################################################
# Helper Functions
###############################################################################

print_header() {
    echo -e "${BLUE}"
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║                                                            ║"
    echo "║     LMA - Library Management Application Installer         ║"
    echo "║                                                            ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_step() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

print_info() {
    echo -e "${BLUE}[i]${NC} $1"
}

###############################################################################
# Check Requirements
###############################################################################

check_python() {
    print_info "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
        PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
        
        if [ "$PYTHON_MAJOR" -ge 3 ] && [ "$PYTHON_MINOR" -ge 8 ]; then
            print_step "Python $PYTHON_VERSION found"
            return 0
        else
            print_error "Python $PYTHON_VERSION is too old. Need Python 3.8+"
            return 1
        fi
    else
        print_error "Python 3 not found"
        return 1
    fi
}

check_pip() {
    print_info "Checking pip installation..."
    
    if command -v pip3 &> /dev/null; then
        print_step "pip3 found"
        return 0
    else
        print_warning "pip3 not found. Attempting to install..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            python3 -m ensurepip --upgrade
        else
            sudo apt-get install -y python3-pip || sudo dnf install -y python3-pip
        fi
        return 0
    fi
}

check_tkinter() {
    print_info "Checking tkinter installation..."
    
    if python3 -c "import tkinter" 2>/dev/null; then
        print_step "tkinter found"
        return 0
    else
        print_warning "tkinter not found. Installing..."
        
        if [[ "$OSTYPE" == "darwin"* ]]; then
            print_info "tkinter should be included with Python on macOS"
        elif [[ -f /etc/debian_version ]]; then
            sudo apt-get update
            sudo apt-get install -y python3-tk
        elif [[ -f /etc/redhat-release ]]; then
            sudo dnf install -y python3-tkinter
        else
            print_error "Could not install tkinter automatically"
            print_info "Please install tkinter manually for your system"
            return 1
        fi
        return 0
    fi
}

###############################################################################
# Installation Functions
###############################################################################

create_directories() {
    print_info "Creating directory structure..."
    
    mkdir -p "$INSTALL_DIR/articles"
    mkdir -p "$INSTALL_DIR/data"
    mkdir -p "$INSTALL_DIR/scripts"
    mkdir -p "$INSTALL_DIR/docs"
    
    print_step "Directories created at $INSTALL_DIR"
}

install_dependencies() {
    print_info "Installing Python dependencies..."
    
    if [ -f "requirements.txt" ]; then
        # Try normal pip install first
        if pip3 install -r requirements.txt --quiet; then
            print_step "Dependencies installed successfully"
        else
            # On macOS, may need --break-system-packages
            print_warning "Retrying with --break-system-packages flag..."
            if pip3 install -r requirements.txt --break-system-packages --quiet; then
                print_step "Dependencies installed successfully"
            else
                print_error "Failed to install dependencies"
                return 1
            fi
        fi
    else
        print_warning "requirements.txt not found. Installing core dependencies..."
        pip3 install PyMuPDF PyPDF2 Pillow fuzzywuzzy python-Levenshtein --quiet --break-system-packages || \
        pip3 install PyMuPDF PyPDF2 Pillow fuzzywuzzy python-Levenshtein --quiet
        print_step "Core dependencies installed"
    fi
}

copy_files() {
    print_info "Copying application files..."
    
    # Copy Python scripts
    if [ -f "interface_pro.py" ]; then
        cp interface_pro.py "$INSTALL_DIR/scripts/"
        print_step "Copied interface_pro.py"
    fi
    
    if [ -f "lecteur_pdf_pro.py" ]; then
        cp lecteur_pdf_pro.py "$INSTALL_DIR/scripts/"
        print_step "Copied lecteur_pdf_pro.py"
    fi
    
    if [ -f "biblio_improved.py" ]; then
        cp biblio_improved.py "$INSTALL_DIR/scripts/"
        print_step "Copied biblio_improved.py"
    fi
    
    # Copy documentation
    [ -f "README.md" ] && cp README.md "$INSTALL_DIR/docs/"
    [ -f "INSTALL.md" ] && cp INSTALL.md "$INSTALL_DIR/docs/"
    [ -f "CHANGELOG.md" ] && cp CHANGELOG.md "$INSTALL_DIR/docs/"
    
    # Make scripts executable
    chmod +x "$INSTALL_DIR/scripts/"*.py
    
    print_step "Application files copied and made executable"
}

create_launcher() {
    print_info "Creating launcher scripts..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS launcher
        cat > "$INSTALL_DIR/LMA.command" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")/scripts"
python3 interface_pro.py
EOF
        chmod +x "$INSTALL_DIR/LMA.command"
        print_step "macOS launcher created: $INSTALL_DIR/LMA.command"
        
    else
        # Linux desktop entry
        cat > "$HOME/.local/share/applications/lma.desktop" << EOF
[Desktop Entry]
Name=LMA
Comment=Library Management Application
Exec=python3 $INSTALL_DIR/scripts/interface_pro.py
Icon=folder
Terminal=false
Type=Application
Categories=Office;Education;
EOF
        print_step "Linux desktop entry created"
    fi
}

verify_installation() {
    print_info "Verifying installation..."
    
    # Check if all files exist
    local all_good=true
    
    [ ! -f "$INSTALL_DIR/scripts/interface_pro.py" ] && print_error "interface_pro.py not found" && all_good=false
    [ ! -f "$INSTALL_DIR/scripts/lecteur_pdf_pro.py" ] && print_error "lecteur_pdf_pro.py not found" && all_good=false
    [ ! -f "$INSTALL_DIR/scripts/biblio_improved.py" ] && print_error "biblio_improved.py not found" && all_good=false
    
    # Test dependencies
    if ! python3 -c "import fitz, PIL, fuzzywuzzy" 2>/dev/null; then
        print_error "Some dependencies are missing"
        all_good=false
    fi
    
    if [ "$all_good" = true ]; then
        print_step "Installation verified successfully"
        return 0
    else
        print_error "Installation verification failed"
        return 1
    fi
}

###############################################################################
# Main Installation
###############################################################################

main() {
    print_header
    
    echo -e "${BLUE}This script will install LMA to: $INSTALL_DIR${NC}"
    echo -e "${YELLOW}Press Enter to continue or Ctrl+C to cancel...${NC}"
    read
    
    echo ""
    print_info "Starting installation..."
    echo ""
    
    # Check requirements
    if ! check_python; then
        print_error "Python 3.8+ is required. Please install it first."
        exit 1
    fi
    
    check_pip || exit 1
    check_tkinter || exit 1
    
    echo ""
    
    # Install
    create_directories || exit 1
    install_dependencies || exit 1
    copy_files || exit 1
    create_launcher || exit 1
    
    echo ""
    
    # Verify
    if verify_installation; then
        echo ""
        echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
        echo -e "${GREEN}║                                                            ║${NC}"
        echo -e "${GREEN}║     ✅  Installation completed successfully!               ║${NC}"
        echo -e "${GREEN}║                                                            ║${NC}"
        echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
        echo ""
        echo -e "${BLUE}Next steps:${NC}"
        echo -e "  1. Add your PDF files to: ${GREEN}$INSTALL_DIR/articles/${NC}"
        echo -e "  2. Launch LMA:"
        
        if [[ "$OSTYPE" == "darwin"* ]]; then
            echo -e "     ${YELLOW}Double-click: $INSTALL_DIR/LMA.command${NC}"
        else
            echo -e "     ${YELLOW}python3 $INSTALL_DIR/scripts/interface_pro.py${NC}"
        fi
        
        echo -e "  3. Click '🔄 Index' to index your PDFs"
        echo ""
        echo -e "${BLUE}Documentation: $INSTALL_DIR/docs/${NC}"
        echo ""
        
        # Ask if user wants to launch now
        echo -e "${YELLOW}Would you like to launch LMA now? (y/n)${NC}"
        read -r response
        if [[ "$response" =~ ^[Yy]$ ]]; then
            cd "$INSTALL_DIR/scripts"
            python3 interface_pro.py &
            print_info "LMA launched!"
        fi
        
    else
        print_error "Installation completed with errors"
        echo -e "${YELLOW}Please check the error messages above and try again${NC}"
        exit 1
    fi
}

# Run main installation
main
