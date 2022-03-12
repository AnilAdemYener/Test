#!/usr/bin/env python3
from enum import Enum
import sys
import os

class CONSTANTS(Enum):
    EXTENSION = 'qcow2'
    SIZE = 30
    MEMORY = 2048 

class QEMU:
    def __init__(self, name):
        self.name=name
        self.relative_drive_path = '{name}.{extension}'.format(name=name, extension=CONSTANTS.EXTENSION.value)
        self.absolute_drive_path = os.path.join(os.getcwd(), self.relative_drive_path)
        pass

    def create_img(self, size='30G'):
        os.system("""
            qemu-img create -f {extension} {name}.{extension} {size}G 
        """.format(
            name=self.name,
            extension=CONSTANTS.EXTENSION.value,
            size=CONSTANTS.SIZE.value
        ))

    def execute_img(self, cdrom_path=None):
        command = """
            qemu-system-x86_64 \
              -device intel-hda -device hda-duplex \
              -cpu host \
              -enable-kvm \
              -smp 2 \
              -m {memory} \
              -net user \
              -nic user \
              -drive file={drive_path},media=disk \
        """.format(
            memory=CONSTANTS.MEMORY.value,
            drive_path=self.absolute_drive_path,
        )
        if cdrom_path:
            print('CDROM IS NOT EMPTY: {}'.format(cdrom_path))
            command += """
                -cdrom {cdrom_path} \
            """.format(cdrom_path=cdrom_path)
        else: print('CDROM IS EMPTY')
        print(command)
        os.system(command)

if __name__ == '__main__':
    qemu = QEMU(name=sys.argv[2])
    if sys.argv[1] == 'create':
        qemu.create_img()
    elif sys.argv[1] == 'execute':
        arg_cdrom_path = None
        if '--cdrom' in sys.argv:
            arg_cdrom_path = sys.argv[4]
        qemu.execute_img(cdrom_path=arg_cdrom_path)
