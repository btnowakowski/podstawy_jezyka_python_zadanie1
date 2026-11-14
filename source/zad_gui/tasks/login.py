import tkinter as tk
from tkinter import messagebox

from zad_gui.tasks import run_standalone


class LoginWindow(tk.Toplevel):
    SIZE = (460, 280)

    def __init__(self, master):
        super().__init__(master)
        self.title("Logowanie")
        self.resizable(False, False)

        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack(expand=True)
        tk.Label(frame, text="Login:").grid(row=0, column=0, sticky="e", pady=4)
        self.login_entry = tk.Entry(frame, width=25)
        self.login_entry.grid(row=0, column=1, pady=4)
        tk.Label(frame, text="Hasło:").grid(row=1, column=0, sticky="e", pady=4)
        self.password_entry = tk.Entry(frame, width=25, show="*")
        self.password_entry.grid(row=1, column=1, pady=4)
        tk.Button(frame, text="Zaloguj", command=self.submit).grid(
            row=2, column=0, columnspan=2, pady=(10, 0))

        self.bind("<Return>", lambda event: self.submit())
        self.login_entry.focus_set()

    def submit(self):
        login = self.login_entry.get().strip()
        password = self.password_entry.get()
        if not login or not password:
            messagebox.showerror("Błąd", "Wypełnij pola Login i Hasło.", parent=self)
            return
        messagebox.showinfo("Dane logowania", f"Login: {login}\nHasło: {password}", parent=self)


if __name__ == "__main__":
    run_standalone(LoginWindow)
