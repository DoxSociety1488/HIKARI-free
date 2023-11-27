# Хуйня не нужная, лучше залетай в тгк t.me/projecthikari
import ctypes
def disable_resize_and_maximize():

    GWL_STYLE = -16
    WS_SIZEBOX = 0x00040000
    WS_MAXIMIZEBOX = 0x00010000


    hwnd = ctypes.windll.kernel32.GetConsoleWindow()


    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

    style = style & ~WS_SIZEBOX
    style = style & ~WS_MAXIMIZEBOX

    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
