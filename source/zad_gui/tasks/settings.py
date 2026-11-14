import tkinter as tk
import tkinter.font as tkfont
from tkinter import colorchooser, messagebox, ttk

from zad_gui.tasks import run_standalone


class SettingsWindow(tk.Toplevel):
    SIZE = (600, 440)

    def __init__(self, master):
        super().__init__(master)
        self.title("Ustawienia")
        self.applied = {}
        self.background = "#f0f0f0"

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        appearance = ttk.Frame(notebook, padding=12)
        notebook.add(appearance, text="Wygląd")
        ttk.Label(appearance, text="Rozmiar czcionki:").pack(anchor="w")
        self.font_size = tk.IntVar(value=12)
        tk.Scale(appearance, from_=8, to=32, orient="horizontal", variable=self.font_size).pack(fill="x")
        ttk.Button(appearance, text="Wybierz kolor tła", command=self.pick_color).pack(pady=8)
        self.color_label = ttk.Label(appearance, text=f"Tło: {self.background}")
        self.color_label.pack()
        # the settings only change this preview, not the fonts of the whole app
        self.preview_font = tkfont.Font(size=12)
        self.preview = tk.Label(appearance, text="Przykładowy tekst", font=self.preview_font,
                                bg=self.background, width=24, pady=12)
        self.preview.pack(pady=10)

        account = ttk.Frame(notebook, padding=12)
        notebook.add(account, text="Konto")
        ttk.Label(account, text="Nazwa użytkownika:").pack(anchor="w")
        self.username = tk.StringVar()
        ttk.Entry(account, textvariable=self.username).pack(fill="x", pady=(0, 8))
        ttk.Label(account, text="Wiek:").pack(anchor="w")
        self.age = tk.IntVar(value=18)
        ttk.Spinbox(account, from_=0, to=120, textvariable=self.age, width=6).pack(anchor="w")

        notifications = ttk.Frame(notebook, padding=12)
        notebook.add(notifications, text="Powiadomienia")
        self.channels = {"E-mail": tk.BooleanVar(value=True), "SMS": tk.BooleanVar(),
                         "Push": tk.BooleanVar()}
        for name, var in self.channels.items():
            ttk.Checkbutton(notifications, text=name, variable=var).pack(anchor="w")

        buttons = ttk.Frame(self)
        buttons.pack(fill="x", padx=10, pady=(0, 10))
        ttk.Button(buttons, text="Anuluj", command=self.destroy).pack(side="right")
        ttk.Button(buttons, text="Zastosuj", command=self.apply).pack(side="right", padx=6)

    def pick_color(self):
        color = colorchooser.askcolor(color=self.background, title="Kolor tła", parent=self)[1]
        if color:
            self.background = color
            self.color_label.config(text=f"Tło: {color}")

    def apply(self):
        try:
            age = self.age.get()
        except tk.TclError:
            age = None
        self.applied = {
            "font_size": self.font_size.get(),
            "background": self.background,
            "username": self.username.get(),
            "age": age,
            "notifications": [name for name, var in self.channels.items() if var.get()],
        }
        self.preview_font.configure(size=self.font_size.get())
        self.preview.config(bg=self.background)
        summary = (
            f"Czcionka: {self.applied['font_size']}\n"
            f"Tło: {self.applied['background']}\n"
            f"Użytkownik: {self.applied['username']}\n"
            f"Wiek: {self.applied['age']}\n"
            f"Powiadomienia: {', '.join(self.applied['notifications']) or 'brak'}"
        )
        messagebox.showinfo("Zastosowano ustawienia", summary, parent=self)


if __name__ == "__main__":
    run_standalone(SettingsWindow)
