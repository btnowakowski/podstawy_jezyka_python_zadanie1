import tkinter as tk
from tkinter import messagebox, ttk

from zad_gui.tasks import run_standalone

COLUMNS = ("Imię", "Nazwisko", "Ocena")


def parse_grade(text):
    try:
        grade = float(text.replace(",", "."))
    except ValueError:
        return None
    return grade if 2 <= grade <= 5 else None


class StudentsWindow(tk.Toplevel):
    SIZE = (720, 500)

    def __init__(self, master):
        super().__init__(master)
        self.title("Lista studentów")

        form = tk.Frame(self, padx=10, pady=8)
        form.pack(fill="x")
        self.fields = []
        for i, column in enumerate(COLUMNS):
            tk.Label(form, text=column).grid(row=0, column=i * 2, padx=(0, 2))
            entry = tk.Entry(form, width=12)
            entry.grid(row=0, column=i * 2 + 1, padx=(0, 8))
            self.fields.append(entry)
        tk.Button(form, text="Dodaj", command=self.add_student).grid(row=0, column=6)
        tk.Button(form, text="Usuń", command=self.delete_selected).grid(row=0, column=7, padx=6)

        table = tk.Frame(self)
        table.pack(fill="both", expand=True, padx=10)
        self.tree = ttk.Treeview(table, columns=COLUMNS, show="headings", selectmode="extended")
        for column in COLUMNS:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=120, anchor="center" if column == "Ocena" else "w")
        scrollbar = ttk.Scrollbar(table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.tree.bind("<Double-1>", self.edit_student)

        self.average = tk.Label(self, pady=8)
        self.average.pack()

        self.tree.insert("", tk.END, values=("Anna", "Kowalska", "4.5"))
        self.tree.insert("", tk.END, values=("Jan", "Nowak", "3.5"))
        self.update_average()

    def update_average(self):
        grades = [float(self.tree.set(row, "Ocena")) for row in self.tree.get_children()]
        if grades:
            self.average.config(text=f"Średnia ocen: {sum(grades) / len(grades):.2f}")
        else:
            self.average.config(text="Średnia ocen: -")

    def add_student(self):
        first, last, raw_grade = (entry.get().strip() for entry in self.fields)
        grade = parse_grade(raw_grade)
        if not first or not last or grade is None:
            messagebox.showerror("Błąd", "Podaj imię, nazwisko i ocenę (2-5).", parent=self)
            return
        self.tree.insert("", tk.END, values=(first, last, f"{grade:g}"))
        for entry in self.fields:
            entry.delete(0, tk.END)
        self.update_average()

    def delete_selected(self):
        for row in self.tree.selection():
            self.tree.delete(row)
        self.update_average()

    def edit_student(self, event):
        row = self.tree.identify_row(event.y)
        if not row:
            return
        dialog = tk.Toplevel(self)
        dialog.title("Edycja")
        dialog.transient(self)
        entries = []
        for i, (column, value) in enumerate(zip(COLUMNS, self.tree.item(row, "values"))):
            tk.Label(dialog, text=column).grid(row=i, column=0, padx=8, pady=4)
            entry = tk.Entry(dialog)
            entry.insert(0, value)
            entry.grid(row=i, column=1, padx=8)
            entries.append(entry)

        def apply():
            first, last, raw_grade = (entry.get().strip() for entry in entries)
            grade = parse_grade(raw_grade)
            if not first or not last or grade is None:
                messagebox.showerror("Błąd", "Niepoprawne dane.", parent=dialog)
                return
            self.tree.item(row, values=(first, last, f"{grade:g}"))
            self.update_average()
            dialog.destroy()

        tk.Button(dialog, text="Zapisz", command=apply).grid(row=3, column=0, columnspan=2, pady=8)


if __name__ == "__main__":
    run_standalone(StudentsWindow)
