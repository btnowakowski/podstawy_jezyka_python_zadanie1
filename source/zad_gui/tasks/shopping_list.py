import tkinter as tk

from zad_gui.tasks import run_standalone

PRODUCTS = ("Chleb", "Mleko", "Masło", "Jajka", "Ser", "Jabłka", "Kawa")


class ShoppingListWindow(tk.Toplevel):
    SIZE = (560, 500)

    def __init__(self, master):
        super().__init__(master)
        self.title("Lista zakupów")

        body = tk.Frame(self, padx=10, pady=10)
        body.pack(fill="both", expand=True)

        list_frame = tk.Frame(body)
        list_frame.pack(fill="both", expand=True)
        self.listbox = tk.Listbox(list_frame, selectmode=tk.MULTIPLE, height=8)
        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.listbox.insert(tk.END, *PRODUCTS)

        add_row = tk.Frame(body)
        add_row.pack(fill="x", pady=6)
        self.new_item = tk.Entry(add_row)
        self.new_item.pack(side="left", fill="x", expand=True)
        self.new_item.bind("<Return>", lambda event: self.add_item())
        tk.Button(add_row, text="Dodaj", command=self.add_item).pack(side="left", padx=(6, 0))

        buttons = tk.Frame(body)
        buttons.pack(fill="x")
        tk.Button(buttons, text="Pokaż", command=self.show_selected).pack(side="left")
        tk.Button(buttons, text="Usuń zaznaczone", command=self.delete_selected).pack(side="left", padx=6)
        tk.Button(buttons, text="Wyczyść zaznaczenia",
                  command=lambda: self.listbox.selection_clear(0, tk.END)).pack(side="left")

        self.summary = tk.Label(body, anchor="w", justify="left")
        self.summary.pack(fill="x", pady=(6, 0))

    def add_item(self):
        text = self.new_item.get().strip()
        if text:
            self.listbox.insert(tk.END, text)
            self.new_item.delete(0, tk.END)

    def show_selected(self):
        items = [self.listbox.get(i) for i in self.listbox.curselection()]
        self.summary.config(text="Zaznaczone: " + (", ".join(items) or "(brak)"))

    def delete_selected(self):
        for index in reversed(self.listbox.curselection()):
            self.listbox.delete(index)


if __name__ == "__main__":
    run_standalone(ShoppingListWindow)
