import tkinter as tk
from tkinter import messagebox

from zad_gui.tasks import run_standalone

LEVELS = ("Początkujący", "Średniozaawansowany", "Zaawansowany")
INTERESTS = ("Web", "AI", "Data Science")
LANGUAGES = ("Python", "JavaScript", "Java", "C++", "Go", "Rust")


class SurveyWindow(tk.Toplevel):
    SIZE = (680, 740)

    def __init__(self, master):
        super().__init__(master)
        self.title("Ankieta")
        pack_opts = {"padx": 10, "pady": 5, "fill": "x"}

        group = tk.LabelFrame(self, text="Imię i nazwisko")
        group.pack(**pack_opts)
        self.name_entry = tk.Entry(group)
        self.name_entry.pack(fill="x", padx=6, pady=6)

        group = tk.LabelFrame(self, text="Poziom")
        group.pack(**pack_opts)
        self.level = tk.StringVar(value=LEVELS[0])
        for level in LEVELS:
            tk.Radiobutton(group, text=level, value=level, variable=self.level).pack(side="left", padx=6)

        group = tk.LabelFrame(self, text="Zainteresowania")
        group.pack(**pack_opts)
        self.interests = {name: tk.BooleanVar() for name in INTERESTS}
        for name, var in self.interests.items():
            tk.Checkbutton(group, text=name, variable=var).pack(side="left", padx=6)

        group = tk.LabelFrame(self, text="Ulubione języki")
        group.pack(**pack_opts)
        self.languages = tk.Listbox(group, selectmode=tk.MULTIPLE, height=len(LANGUAGES),
                                    exportselection=False)
        self.languages.pack(fill="x", padx=6, pady=6)
        self.languages.insert(tk.END, *LANGUAGES)

        group = tk.LabelFrame(self, text="Uwagi")
        group.pack(**pack_opts)
        self.comments = tk.Text(group, width=50, height=4)
        self.comments.pack(fill="x", padx=6, pady=6)

        tk.Button(self, text="Wyślij", command=self.submit).pack(pady=8)

    def submit(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Uwaga", "Podaj imię i nazwisko.", parent=self)
            return
        interests = ", ".join(n for n, var in self.interests.items() if var.get())
        languages = ", ".join(self.languages.get(i) for i in self.languages.curselection())
        summary = (
            f"Imię: {name}\n"
            f"Poziom: {self.level.get()}\n"
            f"Zainteresowania: {interests}\n"
            f"Ulubione języki: {languages}\n"
            f"Uwagi: {self.comments.get('1.0', 'end-1c').strip()}"
        )
        window = tk.Toplevel(self)
        window.title("Podsumowanie")
        tk.Label(window, text=summary, justify="left", anchor="w", padx=16, pady=16).pack()
        tk.Button(window, text="Zamknij", command=window.destroy).pack(pady=(0, 10))


if __name__ == "__main__":
    run_standalone(SurveyWindow)
