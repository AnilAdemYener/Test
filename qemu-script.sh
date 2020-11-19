#!/bin/sh

qemu-system-x86_64 \
  -enable-kvm \
  -m 1024 \
  -net user,smb=/home/admarmn/Belgeler/VMShare/ \
  -nic user \
  -drive file=/home/admarmn/Belgeler/win8.1-qemu/windows8-1.qcow2,media=disk \
  -cdrom /home/admarmn/Masaüstü/Win8.1_Turkish_x64.iso \

# INSTALLATION COMMAND
#qemu-img create -f qcow2 windows8-1.qcow2 20G

# DISABLED
#-nic user,model=virtio \
#-drive file=/home/admarmn/Belgeler/win8.1-qemu/windows8-1.qcow2,media=disk,if=virtio \
