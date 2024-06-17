# MACROPAD Hotkeys: LabVIEW

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'LabVIEW', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00FFFF, 'Clean', [Keycode.CONTROL, 'u']),
        (0xFF1818, 'ZOut', [Keycode.CONTROL, '-']),
        (0xFF1818, 'ZIn', [Keycode.CONTROL, '=']),
        # 2nd row ----------
        (0x00FFFF, 'FixWire', [Keycode.CONTROL, 'b']),
        (0xFF1818, '-', [Keycode.ALT, 11, 12, 6]),
        (0xFF1818, '-', [Keycode.CONTROL, '0']),
        # 3rd row ----------
        (0x00FFFF, '-', [Keycode.ALT, 11, 12, 6]),
        (0xFF1818, '-', [Keycode.ALT, 11, 7, 6]),
        (0xFF1818, '-', [Keycode.ALT, 11, 7, 6]),
        # 4th row ----------
        (0x00FFFF, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                           'www.adafruit.com\n']),   # Adafruit in new window
        (0x00FFFF, '-', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                            'www.digikey.com\n']),   # Digi-Key in new window
        (0xFF1818, 'ZAct', [Keycode.CONTROL, '0']),
        # Encoder button ---
        (0xFF1818, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
