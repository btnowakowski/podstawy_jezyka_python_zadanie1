import tkinter as tk
from tkinter import ttk

from zad_gui.tasks import run_standalone

CONVERSIONS = {
    "km -> mile": lambda x: x * 0.621371,
    "°C -> °F": lambda x: x * 9 / 5 + 32,
    "kg -> funty": lambda x: x * 2.204623,
}


class ConverterWindow(tk.Toplevel):
    SIZE = (500, 300)

    def __init__(self, master):
        super().__init__(master)
        self.title("Konwerter jednostek")

        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack(expand=True)
        self.kind = tk.StringVar(value=next(iter(CONVERSIONS)))
        self.value = tk.StringVar()

        ttk.Combobox(frame, textvariable=self.kind, values=list(CONVERSIONS),
                     state="readonly", width=15).grid(row=0, column=0, columnspan=2, pady=4)
        tk.Label(frame, text="Wartość:").grid(row=1, column=0)
        tk.Entry(frame, textvariable=self.value, width=15).grid(row=1, column=1, pady=4)
        self.result = tk.Label(frame, width=30)
        self.result.grid(row=2, column=0, columnspan=2, pady=8)

        self.value.trace_add("write", self.convert)
        self.kind.trace_add("write", self.convert)

    def convert(self, *_):
        raw = self.value.get().strip().replace(",", ".")
        if not raw:
            self.result.config(text="", fg="black")
            return
        try:
            number = float(raw)
        except ValueError:
            self.result.config(text="Niepoprawna liczba", fg="red")
            return
        converted = CONVERSIONS[self.kind.get()](number)
        self.result.config(text=f"Wynik: {converted:.2f}", fg="black")


if __name__ == "__main__":
    run_standalone(ConverterWindow)
