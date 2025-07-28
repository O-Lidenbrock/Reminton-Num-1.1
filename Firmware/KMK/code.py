import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC


# Pinout
COL1 = board.D1
COL2 = board.D0
COL3 = board.D2
COL4 = board.D21
COL5 = board.D20
COL6 = board.D19
COL7 = board.D18
COL8 = board.D15
COL9 = board.D14
COL10 = board.D16
COL11 = board.D3
COL12 = board.D4
COL13 = board.D10


ROW1 = board.D5
ROW2 = board.D6
ROW3 = board.D7
ROW4 = board.D8
ROW5 = board.D9

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# # Add the macro extension
# macros = Macros()
# keyboard.modules.append(macros)

# Define your pins here!
keyboard.col_pins = (COL1, COL2, COL3, COL4, COL5, COL6, COL7, COL8, COL9, COL10, COL11, COL12, COL13)
keyboard.row_pins = (ROW1, ROW2, ROW3, ROW4, ROW5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW 

keyboard.keymap = [
    [KC.GRAVE, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET,
    KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SEMICOLON, KC.QUOTE,
    KC.LSHIFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.DEL, KC.ESC,
    KC.LCTRL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.RCTRL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.BACKSPACE, KC.BACKSLASH, KC.UP]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
