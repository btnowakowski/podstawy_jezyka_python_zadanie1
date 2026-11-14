import tkinter as tk


def run_standalone(window_cls):
    root = tk.Tk()
    root.withdraw()
    window = window_cls(root)
    window.bind("<Destroy>", lambda e: root.quit() if e.widget is window else None)
    root.mainloop()
