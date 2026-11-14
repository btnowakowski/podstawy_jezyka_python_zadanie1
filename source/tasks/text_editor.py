import re
import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

from tasks import run_standalone

HIGHLIGHT_TAG = "match"


def count_words(text):
    return len(re.findall(r"\S+", text))


class TextEditorWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.path = None
        self.find_window = None
        self.title("Notatnik")

        self.font = tkfont.Font(family="Courier", size=12)
        self.text = ScrolledText(self, width=70, height=20, wrap="word", font=self.font, undo=True)
        self.text.pack(fill="both", expand=True)
        self.text.tag_config(HIGHLIGHT_TAG, background="yellow", foreground="black")
        self.text.bind("<<Modified>>", self.on_modified)

        self.status = tk.Label(self, text="Słowa: 0", anchor="w", relief="sunken", padx=6)
        self.status.pack(fill="x", side="bottom")

        self.wrap = tk.BooleanVar(value=True)
        self.font_size = tk.IntVar(value=12)
        self.build_menu()

        self.bind_shortcut("n", self.new_file)
        self.bind_shortcut("o", self.open_file)
        self.bind_shortcut("s", self.save_file)
        self.bind_shortcut("f", self.open_find)

    def bind_shortcut(self, key, command):
        # Text already uses Ctrl+N and Ctrl+O, "break" stops that
        def handler(event):
            command()
            return "break"

        for modifier in ("Control", "Command"):
            self.text.bind(f"<{modifier}-{key}>", handler)
            self.bind(f"<{modifier}-{key}>", handler)

    def build_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Nowy", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Otwórz...", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Zapisz", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Zakończ", command=self.destroy)
        menubar.add_cascade(label="Plik", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Szukaj...", accelerator="Ctrl+F", command=self.open_find)
        menubar.add_cascade(label="Edycja", menu=edit_menu)

        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_checkbutton(label="Zawijanie wierszy", variable=self.wrap, command=self.apply_wrap)
        size_menu = tk.Menu(view_menu, tearoff=0)
        for size in (10, 12, 14, 18, 24):
            size_menu.add_radiobutton(label=f"{size} pt", value=size, variable=self.font_size,
                                      command=self.apply_font_size)
        view_menu.add_cascade(label="Rozmiar czcionki", menu=size_menu)
        menubar.add_cascade(label="Widok", menu=view_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="O programie", command=lambda: messagebox.showinfo(
            "O programie", "Notatnik w tkinter", parent=self))
        menubar.add_cascade(label="Pomoc", menu=help_menu)
        self.config(menu=menubar)

    def apply_wrap(self):
        self.text.config(wrap="word" if self.wrap.get() else "none")

    def apply_font_size(self):
        self.font.configure(size=self.font_size.get())

    def on_modified(self, _event=None):
        if self.text.edit_modified():
            words = count_words(self.text.get("1.0", "end-1c"))
            self.status.config(text=f"Słowa: {words}")
            self.text.edit_modified(False)

    def new_file(self):
        if self.text.get("1.0", "end-1c") and not messagebox.askyesno(
                "Nowy", "Odrzucić bieżącą treść?", parent=self):
            return
        self.text.delete("1.0", tk.END)
        self.path = None
        self.title("Notatnik")

    def open_file(self):
        path = filedialog.askopenfilename(
            parent=self, filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie", "*.*")])
        if not path:
            return
        try:
            with open(path, encoding="utf-8") as f:
                data = f.read()
        except (OSError, UnicodeDecodeError) as exc:
            messagebox.showerror("Błąd", f"Nie można otworzyć pliku:\n{exc}", parent=self)
            return
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", data)
        self.path = path
        self.title(f"Notatnik - {path}")

    def save_file(self):
        if not self.path:
            self.path = filedialog.asksaveasfilename(
                parent=self, defaultextension=".txt", filetypes=[("Pliki tekstowe", "*.txt")])
            if not self.path:
                return
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", "end-1c"))
        except OSError as exc:
            messagebox.showerror("Błąd", f"Nie można zapisać pliku:\n{exc}", parent=self)
            return
        self.title(f"Notatnik - {self.path}")

    def open_find(self):
        if self.find_window and self.find_window.winfo_exists():
            self.find_window.lift()
            self.find_entry.focus_set()
            return
        win = self.find_window = tk.Toplevel(self)
        win.title("Szukaj")
        win.transient(self)

        tk.Label(win, text="Szukaj:").grid(row=0, column=0, padx=6, pady=6)
        self.find_entry = tk.Entry(win, width=25)
        self.find_entry.grid(row=0, column=1, padx=6)
        self.match_case = tk.BooleanVar()
        tk.Checkbutton(win, text="Rozróżniaj wielkość liter", variable=self.match_case).grid(
            row=1, column=0, columnspan=2)
        self.find_result = tk.Label(win)
        self.find_result.grid(row=2, column=0, columnspan=2)
        tk.Button(win, text="Znajdź wszystkie", command=self.find_all).grid(row=3, column=0, pady=6)
        tk.Button(win, text="Wyczyść", command=self.clear_highlight).grid(row=3, column=1)

        self.find_entry.bind("<Return>", lambda event: self.find_all())
        win.bind("<Escape>", lambda event: win.destroy())
        win.protocol("WM_DELETE_WINDOW", self.close_find)
        self.find_entry.focus_set()

    def close_find(self):
        self.clear_highlight()
        self.find_window.destroy()

    def find_all(self):
        self.clear_highlight()
        needle = self.find_entry.get()
        if not needle:
            self.find_result.config(text="")
            return
        count = 0
        start = "1.0"
        while True:
            pos = self.text.search(needle, start, stopindex=tk.END, nocase=not self.match_case.get())
            if not pos:
                break
            end = f"{pos}+{len(needle)}c"
            self.text.tag_add(HIGHLIGHT_TAG, pos, end)
            start = end
            count += 1
        if count:
            self.text.see(self.text.tag_ranges(HIGHLIGHT_TAG)[0])
        self.find_result.config(text=f"Znaleziono: {count}")

    def clear_highlight(self):
        self.text.tag_remove(HIGHLIGHT_TAG, "1.0", tk.END)


if __name__ == "__main__":
    run_standalone(TextEditorWindow)
