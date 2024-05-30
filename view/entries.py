import sys
import customtkinter as ctk
sys.path.insert(0, './controler')
import controler as ctr

class EntryWithLimitation(ctk.CTkEntry):
    def __init__(self, master, charlist, **kw):
        super().__init__(master, **kw)
        self.charlist = charlist

        text_checker = master.register(self.isValid)
        self.configure(validate="key", validatecommand=(text_checker, "%P"))

    def isValid(self, text):
        # Verifica se o texto contém caracteres proibidos
        if any(char in text for char in self.charlist):
            return False

        # Verifica se há letras repetidas consecutivamente
        for i in range(len(text) - 1):
            if text[i].isalpha() and text[i] == text[i + 1]:
                return False

        return True

def create_entries(panel):
    CharList = ["(", ")", "[", "]", "*", "/", ".", ",", "{", "}", "~", "?", ";", "´", "´", "%", "$", "#", "@", "'", '"', '|']

    label = ctk.CTkLabel(master=panel, text="Derivative Calculator", font=("Roboto", 24))
    label.pack(pady=12, padx=10, fill="x")

    function_entry = EntryWithLimitation(panel, CharList)
    function_entry.pack(pady=10, padx=10, fill="x")

    Btn_Calculate = ctk.CTkButton(master=panel, text="Calculate", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.calculator(function_entry.get()))
    Btn_Calculate.pack(pady=10, padx=10, fill="x")
