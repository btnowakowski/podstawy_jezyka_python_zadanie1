import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

from tasks import run_standalone


class NotepadFilesWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.path = None
        self.title("Notatnik")

        body = tk.Frame(self, padx=10, pady=10)
        body.pack(fill="both", expand=True)
        tk.Label(body, text="Tytuł:").pack(anchor="w")
        self.title_entry = tk.Entry(body)
        self.title_entry.pack(fill="x", pady=(0, 6))
        self.text = ScrolledText(body, width=60, height=15, wrap="word")
        self.text.pack(fill="both", expand=True)

        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Nowy", accelerator="Ctrl+N", command=self.new_file)
        file_menu.add_command(label="Otwórz...", accelerator="Ctrl+O", command=self.open_file)
        file_menu.add_command(label="Zapisz", accelerator="Ctrl+S", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Zakończ", command=self.destroy)
        menubar.add_cascade(label="Plik", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="O programie", command=self.show_about)
        menubar.add_cascade(label="Pomoc", menu=help_menu)
        self.config(menu=menubar)

        self.bind_shortcut("n", self.new_file)
        self.bind_shortcut("o", self.open_file)
        self.bind_shortcut("s", self.save_file)

    def bind_shortcut(self, key, command):
        # Text already uses Ctrl+N and Ctrl+O, "break" stops that
        def handler(event):
            command()
            return "break"

        for widget in (self.title_entry, self.text):
            for modifier in ("Control", "Command"):
                widget.bind(f"<{modifier}-{key}>", handler)

    def show_about(self):
        messagebox.showinfo("O programie", "Notatnik w tkinter", parent=self)

    def new_file(self):
        has_content = self.text.get("1.0", "end-1c") or self.title_entry.get()
        if has_content and not messagebox.askyesno("Nowy", "Odrzucić bieżącą treść?", parent=self):
            return
        self.title_entry.delete(0, tk.END)
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
        note_title, _, body = data.partition("\n")
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, note_title)
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", body)
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
                f.write(self.title_entry.get() + "\n" + self.text.get("1.0", "end-1c"))
        except OSError as exc:
            messagebox.showerror("Błąd", f"Nie można zapisać pliku:\n{exc}", parent=self)
            return
        self.title(f"Notatnik - {self.path}")


if __name__ == "__main__":
    run_standalone(NotepadFilesWindow)
