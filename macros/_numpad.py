# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00FFFF, '7', ['7']),
        (0x00FFFF, '8', ['8']),
        (0x00FFFF, '9', ['9']),
        # 2nd row ----------
        (0x00FFFF, '4', ['4']),
        (0x00FFFF, '5', ['5']),
        (0x00FFFF, '6', ['6']),
        # 3rd row ----------
        (0x00FFFF, '1', ['1']),
        (0x00FFFF, '2', ['2']),
        (0x00FFFF, '3', ['3']),
        # 4th row ----------
        (0x00BFFF, '.', [55]),
        (0x00FFFF, '0', ['0']),
        (0x00BFFF, 'ENTER', [40]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
