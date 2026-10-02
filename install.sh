#!/bin/bash

RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
CYAN='\033[1;36m'
MAGENTA='\033[1;35m'
WHITE='\033[1;37m'
RESET='\033[0m'

clear
echo -e "${MAGENTA}"
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗   ██╗██████╗
║   ████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║   ██║██╔══██╗
║   ██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║   ██║██████╔╝
║   ██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║   ██║██╔══██╗
║   ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ╚██████╔╝██║  ██║
║   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝
║                                                               ║
║           TOOLS SERBA GUNA — INSTALLER v3.0                   ║
║      Support: Termux / Kali / NetHunter / Debian              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
echo -e "${RESET}"

IS_TERMUX=false
IS_LINUX=false
IS_ARCH=false
PKG_MGR=""

if [ -d "/data/data/com.termux" ] || [ -n "$TERMUX_VERSION" ]; then
    IS_TERMUX=true
    PKG_MGR="pkg"
elif [ -f /etc/os-release ]; then
    IS_LINUX=true
    . /etc/os-release
    if echo "$ID $ID_LIKE" | grep -qi "arch"; then
        IS_ARCH=true
        PKG_MGR="pacman"
    elif command -v apt &> /dev/null; then
        PKG_MGR="apt"
    elif command -v dnf &> /dev/null; then
        PKG_MGR="dnf"
    elif command -v yum &> /dev/null; then
        PKG_MGR="yum"
    fi
fi

echo -e "${CYAN}[*] Deteksi Environment:${RESET}"
if [ "$IS_TERMUX" = true ]; then
    echo -e "${GREEN}    OK Termux (Android) - Mode: No Venv${RESET}"
elif [ "$IS_LINUX" = true ]; then
    echo -e "${GREEN}    OK Linux: $PRETTY_NAME - Mode: Venv Required${RESET}"
    if [ "$IS_ARCH" = true ]; then
        echo -e "${GREEN}    OK Arch-based${RESET}"
    fi
fi

echo ""
ARCH=$(uname -m)
echo -e "${CYAN}[*] Arsitektur: $ARCH${RESET}"

if [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
    GECKO_ARCH="linux-aarch64"
    echo -e "${GREEN}[OK] ARM64${RESET}"
elif [ "$ARCH" = "armv7l" ] || [ "$ARCH" = "armv8l" ]; then
    GECKO_ARCH="linux-armv7l"
    echo -e "${GREEN}[OK] ARMv7${RESET}"
elif [ "$ARCH" = "x86_64" ] || [ "$ARCH" = "amd64" ]; then
    GECKO_ARCH="linux64"
    echo -e "${GREEN}[OK] x86_64${RESET}"
else
    GECKO_ARCH="linux64"
    echo -e "${GREEN}[OK] $ARCH${RESET}"
fi

if [ "$EUID" -eq 0 ]; then
    SUDO=""
    echo -e "${YELLOW}[i] Running as root${RESET}"
elif command -v sudo &> /dev/null; then
    SUDO="sudo"
else
    SUDO=""
    echo -e "${YELLOW}[i] Tanpa sudo${RESET}"
fi

if [ "$IS_LINUX" = true ]; then
    echo ""
    echo -e "${CYAN}[*] Checking virtual environment (Linux mode)...${RESET}"
    echo ""

    if [ -z "$VIRTUAL_ENV" ]; then
        echo -e "${RED}╔═══════════════════════════════════════════════════════════════╗${RESET}"
        echo -e "${RED}║                                                               ║${RESET}"
        echo -e "${RED}║   VIRTUAL ENVIRONMENT BELUM AKTIF!                            ║${RESET}"
        echo -e "${RED}║                                                               ║${RESET}"
        echo -e "${YELLOW}║   Di Linux, installer WAJIB pakai venv.                       ║${RESET}"
        echo -e "${YELLOW}║                                                               ║${RESET}"
        echo -e "${YELLOW}║   CARA AKTIFIN VENV:                                          ║${RESET}"
        echo -e "${YELLOW}║                                                               ║${RESET}"
        echo -e "${WHITE}║   1. Buat venv:                                               ║${RESET}"
        echo -e "${WHITE}║      python3 -m venv venv                                     ║${RESET}"
        echo -e "${WHITE}║                                                               ║${RESET}"
        echo -e "${WHITE}║   2. Aktifin venv:                                            ║${RESET}"
        echo -e "${WHITE}║      source venv/bin/activate                                 ║${RESET}"
        echo -e "${WHITE}║                                                               ║${RESET}"
        echo -e "${WHITE}║   3. Baru jalanin installer:                                  ║${RESET}"
        echo -e "${WHITE}║      bash install.sh                                          ║${RESET}"
        echo -e "${RED}║                                                               ║${RESET}"
        echo -e "${GREEN}║   Setelah aktifin venv, coba lagi ya!                         ║${RESET}"
        echo -e "${RED}║                                                               ║${RESET}"
        echo -e "${RED}╚═══════════════════════════════════════════════════════════════╝${RESET}"
        echo ""
        exit 1
    else
        echo -e "${GREEN}[OK] Venv aktif: $VIRTUAL_ENV${RESET}"
        echo -e "${GREEN}[OK] Python: $(which python3)${RESET}"
        PYVER=$(python3 --version 2>&1 | awk '{print $2}')
        echo -e "${GREEN}[OK] Versi: $PYVER${RESET}"
    fi
else
    echo ""
    echo -e "${GREEN}[OK] Termux mode - Skip venv check${RESET}"
    echo -e "${GREEN}[OK] Python: $(which python 2>/dev/null || which python3)${RESET}"
fi

echo ""
echo -e "${CYAN}[*] Update package list...${RESET}"

if [ "$IS_TERMUX" = true ]; then
    pkg update -y 2>/dev/null || true
elif [ "$IS_ARCH" = true ]; then
    $SUDO pacman -Sy --noconfirm 2>/dev/null || true
elif [ "$PKG_MGR" = "apt" ]; then
    $SUDO apt update -qq 2>/dev/null || true
elif [ "$PKG_MGR" = "dnf" ]; then
    $SUDO dnf check-update 2>/dev/null || true
fi

echo ""
echo -e "${CYAN}[*] Install system dependencies...${RESET}"

if [ "$IS_TERMUX" = true ]; then
    for pkg in python python-pip git wget curl openssl libffi clang; do
        if ! dpkg -l 2>/dev/null | grep -q "^ii  $pkg"; then
            echo -e "${YELLOW}[->] pkg install $pkg${RESET}"
            pkg install -y "$pkg" 2>/dev/null || true
        fi
    done
elif [ "$IS_ARCH" = true ]; then
    for pkg in python python-pip git wget curl openssl libffi base-devel; do
        if ! pacman -Q "$pkg" &> /dev/null; then
            echo -e "${YELLOW}[->] pacman install $pkg${RESET}"
            $SUDO pacman -S --noconfirm "$pkg" 2>/dev/null || true
        fi
    done
elif [ "$PKG_MGR" = "apt" ]; then
    for pkg in python3 python3-pip python3-venv git wget curl build-essential libffi-dev libssl-dev; do
        if ! dpkg -l 2>/dev/null | grep -q "^ii  $pkg"; then
            echo -e "${YELLOW}[->] apt install $pkg${RESET}"
            $SUDO apt install -y "$pkg" 2>/dev/null || true
        fi
    done
fi

echo ""
echo -e "${CYAN}[*] Upgrade pip...${RESET}"

if [ "$IS_TERMUX" = true ]; then
    pip install --upgrade pip setuptools wheel --quiet 2>&1 | tail -1
else
    pip3 install --upgrade pip setuptools wheel --quiet 2>&1 | tail -1
fi

echo ""
echo -e "${CYAN}[*] Install Python dependencies...${RESET}"

PACKAGES=(
    "requests"
    "rich"
    "beautifulsoup4"
    "PySocks"
    "selenium"
    "lxml"
    "html5lib"
    "google-generativeai"
    "python-dotenv"
)

for pkg in "${PACKAGES[@]}"; do
    echo -e "${YELLOW}[->] $pkg${RESET}"
    pip install "$pkg" --quiet 2>&1 | tail -1
done

echo -e "${GREEN}[OK] Semua dependencies keinstall${RESET}"

echo ""
read -p "$(echo -e ${YELLOW}"[?] Install Tor + proxychains? (y/n): "${RESET})" -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ "$IS_TERMUX" = true ]; then
        pkg install -y tor 2>/dev/null || true
        pkg install -y proxychains-ng 2>/dev/null || true
    elif [ "$IS_ARCH" = true ]; then
        $SUDO pacman -S --noconfirm tor proxychains-ng 2>/dev/null || true
    elif [ "$PKG_MGR" = "apt" ]; then
        $SUDO apt install -y tor proxychains4 2>/dev/null || $SUDO apt install -y tor proxychains-ng 2>/dev/null || true
    fi

    if command -v proxychains4 &> /dev/null; then
        echo -e "${GREEN}[OK] Tor + proxychains4${RESET}"
    elif command -v proxychains &> /dev/null; then
        echo -e "${GREEN}[OK] Tor + proxychains${RESET}"
    else
        echo -e "${YELLOW}[!] Tor/proxychains gagal, skip${RESET}"
    fi
fi

echo ""
echo -e "${GREEN}"

if [ "$IS_TERMUX" = true ]; then
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   INSTALLATION COMPLETE! (Termux Mode)                        ║
║                                                               ║
║   CARA PAKE:                                                  ║
║                                                               ║
║   Jalanin tools:                                              ║
║       python main.py                                          ║
║                                                               ║
║   Kalau mau pake Tor:                                         ║
║       tor &                                                   ║
║       proxychains4 python main.py                             ║
║                                                               ║
║   NOTE:                                                       ║
║   Termux gak butuh venv, langsung aja!                        ║
║                                                               ║
║   Selamat menggunakan!                                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
else
cat << "EOF"
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   INSTALLATION COMPLETE! (Linux Mode)                         ║
║                                                               ║
║   CARA PAKE:                                                  ║
║                                                               ║
║   1. Aktifin venv dulu:                                       ║
║      source venv/bin/activate                                 ║
║                                                               ║
║   2. Jalanin tools:                                           ║
║      python main.py                                           ║
║                                                               ║
║   3. Kalau mau pake Tor:                                      ║
║      sudo service tor start                                   ║
║      proxychains4 python main.py                              ║
║                                                               ║
║   JANGAN LUPA:                                                ║
║   Setiap buka terminal baru, aktifin venv dulu!               ║
║                                                               ║
║   Selamat menggunakan!                                        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
EOF
fi

echo -e "${RESET}"

exit 0
