import tkinter as tk
from tkinter import colorchooser

from zad_gui.tasks import run_standalone

BACKGROUND = "white"


class PaintWindow(tk.Toplevel):
    SIZE = (960, 680)

    def __init__(self, master):
        super().__init__(master)
        self.title("Paint")
        self.color = "black"
        self.last_point = None

        toolbar = tk.Frame(self, padx=6, pady=6)
        toolbar.pack(fill="x")
        tk.Button(toolbar, text="Kolor", command=self.pick_color).pack(side="left")
        self.swatch = tk.Label(toolbar, width=3, bg=self.color, relief="sunken")
        self.swatch.pack(side="left", padx=6)
        tk.Label(toolbar, text="Grubość:").pack(side="left")
        self.width_scale = tk.Scale(toolbar, from_=1, to=30, orient="horizontal")
        self.width_scale.set(3)
        self.width_scale.pack(side="left")
        tk.Button(toolbar, text="Wyczyść", command=self.clear).pack(side="left", padx=6)

        self.canvas = tk.Canvas(self, width=700, height=450, bg=BACKGROUND, cursor="crosshair")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_stroke)

        self.erasing = tk.BooleanVar()
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_checkbutton(label="Gumka", variable=self.erasing)
        # on a Mac the right button is Button-2
        for sequence in ("<Button-2>", "<Button-3>", "<Control-Button-1>"):
            self.canvas.bind(sequence, lambda e: self.menu.tk_popup(e.x_root, e.y_root))

    def pick_color(self):
        color = colorchooser.askcolor(color=self.color, parent=self)[1]
        if color:
            self.color = color
            self.swatch.config(bg=color)
            self.erasing.set(False)

    def clear(self):
        self.canvas.delete("all")

    def end_stroke(self, event):
        self.last_point = None

    def draw(self, event):
        color = BACKGROUND if self.erasing.get() else self.color
        width = self.width_scale.get()
        if self.last_point:
            x, y = self.last_point
            self.canvas.create_line(x, y, event.x, event.y, fill=color, width=width,
                                    capstyle="round", smooth=True)
        else:
            r = width / 2
            self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,
                                    fill=color, outline=color)
        self.last_point = (event.x, event.y)


if __name__ == "__main__":
    run_standalone(PaintWindow)
