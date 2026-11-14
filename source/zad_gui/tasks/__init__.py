import tkinter as tk


def show_centered(window):
    # size comes from the window's SIZE, but never smaller than its content needs
    window.update_idletasks()
    width = max(window.SIZE[0], window.winfo_reqwidth())
    height = max(window.SIZE[1], window.winfo_reqheight())
    # leave room for the menu bar and dock on small screens
    width = min(width, window.winfo_screenwidth() - 40)
    height = min(height, window.winfo_screenheight() - 120)
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.lift()
    # topmost for a moment so the window really comes to the front, then back to normal
    window.attributes("-topmost", True)
    window.after(300, lambda: window.attributes("-topmost", False))
    window.focus_force()


def run_standalone(window_cls):
    root = tk.Tk()
    root.withdraw()
    window = window_cls(root)
    show_centered(window)
    window.bind("<Destroy>", lambda e: root.quit() if e.widget is window else None)
    root.mainloop()
