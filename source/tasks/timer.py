import tkinter as tk
from tkinter import messagebox, ttk

from tasks import run_standalone


class TimerWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Minutnik")
        self.total = 0
        self.remaining = 0
        self.job = None

        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack()
        row = tk.Frame(frame)
        row.pack()
        tk.Label(row, text="Sekundy:").pack(side="left")
        self.seconds = tk.IntVar(value=10)
        ttk.Spinbox(row, from_=1, to=3600, textvariable=self.seconds, width=6).pack(side="left", padx=6)

        self.bar = ttk.Progressbar(frame, length=280, mode="determinate")
        self.bar.pack(pady=10)
        self.status = tk.Label(frame)
        self.status.pack()

        buttons = tk.Frame(frame)
        buttons.pack(pady=(8, 0))
        tk.Button(buttons, text="Start", command=self.start).pack(side="left", padx=3)
        tk.Button(buttons, text="Pauza", command=self.pause).pack(side="left", padx=3)
        tk.Button(buttons, text="Reset", command=self.reset).pack(side="left", padx=3)
        self.bind("<Destroy>", lambda e: self.pause() if e.widget is self else None)

    def start(self):
        if self.job is not None:
            return
        if self.remaining <= 0:
            try:
                self.total = self.remaining = int(self.seconds.get())
            except (tk.TclError, ValueError):
                messagebox.showerror("Błąd", "Podaj liczbę sekund.", parent=self)
                return
            if self.total <= 0:
                messagebox.showerror("Błąd", "Liczba sekund musi być dodatnia.", parent=self)
                return
            self.bar.config(maximum=self.total, value=0)
        self.tick()

    def tick(self):
        self.status.config(text=f"Pozostało: {self.remaining} s")
        self.bar.config(value=self.total - self.remaining)
        if self.remaining <= 0:
            self.job = None
            messagebox.showinfo("Minutnik", "Czas minął!", parent=self)
            return
        self.remaining -= 1
        self.job = self.after(1000, self.tick)

    def pause(self):
        if self.job is not None:
            self.after_cancel(self.job)
            self.job = None

    def reset(self):
        self.pause()
        self.remaining = 0
        self.bar.config(value=0)
        self.status.config(text="")


if __name__ == "__main__":
    run_standalone(TimerWindow)
