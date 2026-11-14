import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

from tasks import run_standalone


class NotepadWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Notatnik")

        body = tk.Frame(self, padx=10, pady=10)
        body.pack(fill="both", expand=True)
        tk.Label(body, text="Tytuł:").pack(anchor="w")
        self.title_entry = tk.Entry(body)
        self.title_entry.pack(fill="x", pady=(0, 6))
        tk.Label(body, text="Treść:").pack(anchor="w")
        self.text = ScrolledText(body, width=60, height=15, wrap="word")
        self.text.pack(fill="both", expand=True)

        buttons = tk.Frame(body)
        buttons.pack(pady=(8, 0))
        tk.Button(buttons, text="Zapisz", command=self.save).pack(side="left", padx=4)
        tk.Button(buttons, text="Wyczyść", command=self.clear).pack(side="left", padx=4)

    def save(self):
        print(f"Tytuł: {self.title_entry.get()}")
        print(f"Treść: {self.text.get('1.0', 'end-1c')}")

    def clear(self):
        if messagebox.askyesno("Potwierdzenie", "Czy na pewno wyczyścić notatkę?", parent=self):
            self.title_entry.delete(0, tk.END)
            self.text.delete("1.0", tk.END)


if __name__ == "__main__":
    run_standalone(NotepadWindow)
