# MACROPAD Hotkeys: Confluence

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Confluence', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x181868, '-', [Keycode.CONTROL, 'a', Keycode.CONTROL, 'a',
                               Keycode.ALT, 11, 18, 12]),
        (0x181868, '-', [Keycode.COMMAND, ']']),
        (0x181868, '-', [Keycode.SHIFT, ' ']),
        # 2nd row ----------
        (0x181868, '-', [Keycode.ALT, 11, 12, 21]),
        (0x181868, '-', [Keycode.ALT, 11, 12, 6]),
        (0x181868, '-', [Keycode.ALT, 11, 7, 21]),
        # 3rd row ----------
        (0x181868, '-', [Keycode.ALT, 11, 12, 6]),
        (0x181868, '-', [Keycode.ALT, 11, 7, 6]),
        (0x181868, '-', [Keycode.ALT, 11, 7, 6]),
        # 4th row ----------
        (0x181868, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0x181868, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0x181868, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x181868, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
