import tkinter as tk
from tkinter import ttk
from windows import dpi_awareness
from settings_scales import SettingsPage

# Miglioramento scritte
dpi_awareness()


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Scales app")
        self.geometry("850x700")

        # Frame finestra
        self.window = ttk.Frame(self)
        self.window.pack(fill="both", expand=True)

        # Creazione schermata
        self.workpage = None

        # Inizializzazione workpage
        self.switch_frame(SettingsPage)

        # Chiusura programma
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def switch_frame(self, Page, **kwargs):
        """Creazione WorkPage e distruzione SettingPage"""
        if (self.workpage):
            self.workpage.pack_forget()
            self.workpage.destroy()
        self.workpage = Page(self, self.window, **kwargs)
        self.workpage.pack(fill="both", expand=True)

    def on_closing(self):
        """Gestione evento chiusura finestra"""
        self.quit()
        self.destroy()

# Program Main
app = App()
app.focus_set()
app.mainloop()
