# MACROPAD Hotkeys example: BLANK

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'WIN', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', [Keycode.CONTROL, 'x']),
        (0x000000, '', [Keycode.CONTROL, 'c']),
        (0x000000, '', [Keycode.CONTROL, 'v']),
        # 2nd row ----------
        (0x000000, '', [Keycode.CONTROL, 'z']),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []), 
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l']) #Lock Windows
    ]
}
