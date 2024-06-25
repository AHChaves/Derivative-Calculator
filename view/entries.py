import sys
import customtkinter as ctk
import popUp as pop
sys.path.insert(0, './controler')
import controler as ctr

class EntryWithLimitation(ctk.CTkEntry):
    def __init__(self, master, charlist, **kw):
        super().__init__(master, **kw)
        self.charlist = charlist

        text_checker = master.register(self.isValid)
        self.configure(validate="key", validatecommand=(text_checker, "%P"))

    def isValid(self, text):
        
        # Verifica se os caracteres estao na whitelist
        for char in text:
            if char not in self.charlist and not char.isdigit():
                return False
                
        # Verifica se há letras repetidas consecutivamente
        for i in range(len(text)-1):

            Sequntial =  text[i].lower().isalpha() and text[i].lower() == text[i + 1].lower()

            if Sequntial:
                return False
            
            numberAfterX = text[i].lower() == 'x' and (text[i+1].isnumeric() or text[i+1] not in self.charlist)

            if numberAfterX:
                return False
                
            if text[i].lower() != 'x' and text[i+1] == '^':
                return False

            if text[i] == '^' and text[i+1].lower() == 'x':
                return False

            if text[i] in '+-^' and text[i+1] in '+-^':
                return False

        return True

def create_entries(panel):
    CharList = ["x", "X", "+", "-", "^"]

    info = pop.PopUp(panel)

    Btn_info = ctk.CTkButton(master=panel, 
                             text="info", 
                             width= 40, 
                             height= 20, 
                             font=("Roboto", 14),
                             command= lambda: info.__init__(panel))
    Btn_info.pack(pady=10, padx=10, side='right')
    
    label = ctk.CTkLabel(master=panel, text="Derivative Calculator", font=("Roboto", 24))
    label.pack(pady=12, padx=10, fill="x")


    function_entry = EntryWithLimitation(panel, CharList)
    function_entry.bind("<Return>", lambda event = None: ctr.calculator(function_entry.get()))
    function_entry.pack(pady=10, padx=10, fill="x")

    Btn_Calculate = ctk.CTkButton(master=panel, text="Calculate", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.calculator(function_entry.get()))
    Btn_Calculate.pack(pady=10, padx=10, fill="x")
