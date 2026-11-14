import tkinter as tk
from tkinter import ttk

from tasks.consents import ConsentsWindow
from tasks.converter import ConverterWindow
from tasks.language import LanguageWindow
from tasks.login import LoginWindow
from tasks.notepad import NotepadWindow
from tasks.notepad_files import NotepadFilesWindow
from tasks.paint import PaintWindow
from tasks.settings import SettingsWindow
from tasks.shopping_list import ShoppingListWindow
from tasks.students import StudentsWindow
from tasks.survey import SurveyWindow
from tasks.text_editor import TextEditorWindow
from tasks.timer import TimerWindow

LEVELS = [
    ("Poziom 1 - Podstawowe widgety", [
        ("1. Formularz logowania", LoginWindow),
        ("2. Zgody użytkownika", ConsentsWindow),
    ]),
    ("Poziom 2 - Wybory i interakcje", [
        ("3. Wybór języka programowania", LanguageWindow),
        ("4. Lista zakupów", ShoppingListWindow),
    ]),
    ("Poziom 3 - Łączenie widgetów", [
        ("5. Notatnik z polem Text", NotepadWindow),
        ("6. Formularz ankiety", SurveyWindow),
    ]),
    ("Poziom 4 - Elementy aplikacji okienkowych", [
        ("7. Menu i pliki", NotepadFilesWindow),
        ("8. Konwerter jednostek", ConverterWindow),
        ("9. Lista studentów", StudentsWindow),
        ("10. Ustawienia w zakładkach", SettingsWindow),
    ]),
    ("Poziom 5 - Czas i rysowanie", [
        ("11. Minutnik", TimerWindow),
        ("12. Paint", PaintWindow),
        ("13. Projekt własny - edytor tekstu", TextEditorWindow),
    ]),
]


class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter - zadania")
        self.resizable(False, False)

        for heading, tasks in LEVELS:
            group = ttk.LabelFrame(self, text=heading, padding=8)
            group.pack(fill="x", padx=12, pady=6)
            for label, window_cls in tasks:
                ttk.Button(group, text=label, width=40,
                           command=lambda cls=window_cls: self.open_task(cls)).pack(pady=2)

    def open_task(self, window_cls):
        window_cls(self)


if __name__ == "__main__":
    Launcher().mainloop()
