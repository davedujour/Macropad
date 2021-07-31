# MACROPAD Hotkeys example: Google Chrome web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Chrome', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x500000, 'Plex', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'app.plex.tv\n']), #Plex in new tab
        # 2nd row ----------
        (0x202000, '- Size', [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x202000, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x500000, 'YT', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'www.youtube.com\n']), #YouTube in new tab
        # 3rd row ----------
        (0x444444, 'Next', [Keycode.CONTROL, Keycode.TAB]),
        (0x444444, 'Prev ', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),   
        (0x500000, 'D+', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'www.disneyplus.com\n']), #Disney+ in new tab
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x500000, 'HBO', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'www.hbomax.com\n']), #HBOMax in new tab
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l']) #Lock Windows
    ]
}
