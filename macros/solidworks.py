# MACROPAD Hotkeys: Solidworks

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Solidworks', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x18FF18, '-', [Keycode.CONTROL, 'a', Keycode.CONTROL, 'a',
                               Keycode.ALT, 11, 18, 12]),
        (0x18FF18, '-', [Keycode.COMMAND, ']']),
        (0x18FF18, '-', [Keycode.SHIFT, ' ']),
        # 218FF18 ----------
        (0x18FF18, '-', [Keycode.ALT, 11, 12, 21]),
        (0x18FF18, '-', [Keycode.ALT, 11, 12, 6]),
        (0x18FF18, '-', [Keycode.ALT, 11, 7, 21]),
        # 318FF18 ----------
        (0x18FF18, '-', [Keycode.ALT, 11, 12, 6]),
        (0x18FF18, '-', [Keycode.ALT, 11, 7, 6]),
        (0x18FF18, '-', [Keycode.ALT, 11, 7, 6]),
        # 418FF18 ----------
        (0x18FF18, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0x18FF18, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0x18FF18, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']), # Hack-a-Day in new win
        # Encoder button ---
        (0x18FF18, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
