#!/bin/sh

# get up to date
sudo dnf -y upgrade 

# enable rpmfusion free/nonfree
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm 

sudo dnf install -y rpmfusion-free-release-tainted 
sudo dnf install -y libdvdcss 

sudo dnf install -y rpmfusion-nonfree-release-tainted 
sudo dnf install -y *-firmware 

sudo dnf -y groupupdate core

sudo dnf -y groupupdate multimedia --setop="install_weak_deps=False" --exclude=PackageKit-gstreamer-plugin 

sudo dnf -y groupupdate sound-and-video 

# install apps via terminal
sudo dnf install -y gnome-tweak-tool 

sudo dnf install gstreamer1-{plugin-crystalhd,ffmpeg,plugins-{good,ugly,bad{,-free,-nonfree,-freeworld,-extras}{,-extras}}} libmpg123 lame-libs --setopt=strict=0 -y 

sudo dnf -y install unzip p7zip p7zip-plugins unrar 

sudo dnf -y install gparted 

sudo dnf copr enable dawid/better_fonts 
sudo dnf install -y fontconfig-enhanced-defaults fontconfig-font-replacements
