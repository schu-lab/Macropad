# MACROPAD Hotkeys: Excel

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'MS Excel', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00FFFF, 'FixCol', [Keycode.CONTROL, 'a', Keycode.CONTROL, 'a',
                               Keycode.ALT, 11, 18, 12]),
        (0x22FFFF, 'ZIn', [Keycode.CONTROL, Keycode.ALT, '=']),
        (0x22FFFF, 'ZOut', [Keycode.CONTROL, Keycode.ALT, '-']),
        # 2nd row ----------
        (0x00FFFF, 'AddRow', [Keycode.ALT, 11, 12, 21]),
        (0xFFFFFF, '-', [Keycode.ALT, 11, 12, 6]),
        (0xFA3A3A, 'DelRow', [Keycode.ALT, 11, 7, 21]),
        # 3rd row ----------
        (0x00FFFF, 'AddCol', [Keycode.ALT, 11, 12, 6]),
        (0xFFFFFF, '-', [Keycode.ALT, 11, 7, 6]),
        (0xFA3A3A, 'DelCol', [Keycode.ALT, 11, 7, 6]),
        # 4th row ----------
        (0x00FFFF, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0xFFFFFF, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0xFA3A3A, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
