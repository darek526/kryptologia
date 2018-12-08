import tkinter as tk
from tkinter import filedialog as fd


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("Szyfr Feistela")

        # tworzenie menu

        self.menu = tk.Menu(self.window)

        submenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Operacje", menu=submenu)

        submenu.add_command(label="Otwórz", command=self.open_file)
        submenu.add_command(label="Zapisz", command=self.save_file)
        submenu.add_command(label="Szyfruj ", command=self.open_file)
        submenu.add_command(label="Deszyfruj ", command=self.open_file)

        self.window.config(menu=self.menu, width=50, height=30)

        # dodawanie kontrolki typu Text i paska przewijania

        self.text = tk.Text(self.window)

        self.sb_text = tk.Scrollbar(self.window)
        self.sb_text.place(in_=self.text, relx=1., rely=0, relheight=1.)
        self.sb_text.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.sb_text.set)

        self.text.place(x=0, y=0, relwidth=1, relheight=1, width=- 18)

        self.window.mainloop()

    def open_file(self):
        filename = fd.askopenfilename(filetypes=[("Plik tekstowy", "*.txt")])  # wywołanie okna dialogowego open file

        if filename:
            with open(filename, "r", -1, "utf-8") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy", "*.txt")],
                                        defaultextension="*.txt")  # wywołanie okna dialogowego save file

        if filename:
            with open(filename, "w", -1, "utf-8") as file:
                file.write(self.text.get(1.0, tk.END))


apl = Application()