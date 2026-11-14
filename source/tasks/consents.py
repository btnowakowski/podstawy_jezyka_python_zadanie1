import tkinter as tk
from tkinter import messagebox

from tasks import run_standalone

TERMS = "Akceptacja regulaminu"


class ConsentsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Zgody użytkownika")

        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack()
        tk.Label(frame, text="Imię:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(frame, width=25)
        self.name_entry.grid(row=0, column=1, pady=4)

        self.consents = {
            "Newsletter": tk.BooleanVar(),
            TERMS: tk.BooleanVar(),
            "Udział w testach beta": tk.BooleanVar(),
        }
        for row, (label, var) in enumerate(self.consents.items(), start=1):
            tk.Checkbutton(frame, text=label, variable=var).grid(
                row=row, column=0, columnspan=2, sticky="w")
        tk.Button(frame, text="Zapisz", command=self.save).grid(
            row=4, column=0, columnspan=2, pady=(10, 0))

    def save(self):
        if not self.consents[TERMS].get():
            messagebox.showwarning("Uwaga", "Musisz zaakceptować regulamin.", parent=self)
            return
        accepted = [label for label, var in self.consents.items() if var.get()]
        print(f"Imię: {self.name_entry.get().strip()}")
        print("Zgody:", ", ".join(accepted))


if __name__ == "__main__":
    run_standalone(ConsentsWindow)
