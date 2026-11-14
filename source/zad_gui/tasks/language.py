import tkinter as tk

from zad_gui.tasks import run_standalone

LANGUAGES = ("Python", "Java", "C++")


class LanguageWindow(tk.Toplevel):
    SIZE = (440, 320)

    def __init__(self, master):
        super().__init__(master)
        self.title("Wybór języka")

        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack(expand=True)
        self.choice = tk.StringVar(value=LANGUAGES[0])
        for name in LANGUAGES:
            tk.Radiobutton(frame, text=name, value=name, variable=self.choice).pack(anchor="w")
        tk.Button(frame, text="Pokaż wybór", command=self.show).pack(pady=8)
        self.result = tk.Label(frame)
        self.result.pack()

    def show(self):
        self.result.config(text=f"Wybrano: {self.choice.get()}")


if __name__ == "__main__":
    run_standalone(LanguageWindow)
