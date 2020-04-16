#!/bin/sh

# ubuntu xenial (16.04) - post install
#
# maybe it's useless for your ubuntu
# but i think it's quite useful for me

# update system
sudo apt update && sudo apt -y upgrade

# install restricted extras
sudo apt -y install ubuntu-restricted-extras

# install apps
sudo apt -y install vlc tlp tlp-rdw bleachbit unity-tweak-tools

# start tlp
sudo tlp start

# minimise on click
gsettings set org.compiz.unityshell:/org/compiz/profiles/unity/plugins/unityshell/ launcher-minimize-window true

# remove amazon shitty stuff
sudo apt -y purge ubuntu-web-launchers
sudo apt -y purge ubuntu-webapps-common
sudo rm /usr/share/applications/ubuntu-amazon-default.desktop
sudo rm /usr/share/unity-webapps/userscripts/unity-webapps-amazon/Amazon.user.js
sudo rm /usr/share/unity-webapps/userscripts/unity-webapps-amazon/manifest.json


# brave browser
sudo apt -y install apt-transport-https curl
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt -y install brave-browser

# install keepassxc
sudo add-apt-repository ppa:phoerious/keepassxc
sudo apt update
sudo apt -y install keepassxc
