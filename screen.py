#!/usr/bin/env python3
import os

cmds = [
    'xrandr --newmode "1600x900_60.00"  119.00  1600 1696 1864 2128  900 901 904 932  -HSync +Vsync',
    'xrandr --addmode Virtual1 "1600x900_60.00"',
    'xrandr --output Virtual1 --mode "1600x900_60.00"'
]

for cmd in cmds
    os.system(cmd)
