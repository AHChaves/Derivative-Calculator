import sys
import customtkinter as ctk
import resultsEnesima as rstE

sys.path.insert(0, '../controler')
import controler as ctr

class EntryWithLimitation(ctk.CTkEntry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        text_checker = master.register(self.isValid)
        self.configure(validate="key", validatecommand=(text_checker, "%P"))

    def isValid(self, text):
        # Verifica se os caracteres estao na whitelist
        #for char in text:
        if  str.isdigit(text) or text == "":
            return True
        else:
            return False

def Enesima_Panel(frame):
    frame.columnconfigure((0,1), weight=1, pad=10)
    frame.rowconfigure((0,1,2,3,5), weight=0, pad=10)

    Titulo = ctk.CTkLabel(master=frame, text="Trabalho 3", font= ("Roboto", 24))
    Titulo.grid(row=0, column=0, columnspan=2, sticky='nswe')

    N_entry = EntryWithLimitation(frame)
    N_entry.configure(width=200)
    K_entry = EntryWithLimitation(frame)
    K_entry.configure(width=200)

    N_Label = ctk.CTkLabel(frame, text="Valor de N ", font=("Roboto", 16))
    N_Label.grid(row = 1, column=0, sticky='w')
    K_Label = ctk.CTkLabel(frame, text="Valor de K ", font=("Roboto", 16))
    K_Label.grid(row = 2, column=0, sticky='w')

    N_entry.bind("<Return>", lambda event = None: ctr.Achar_Enesima(N_entry.get(), K_entry.get()))
    N_entry.grid(row = 1, column=1, sticky='w')
    K_entry.bind("<Return>", lambda event = None: ctr.Achar_Enesima(N_entry.get(), K_entry.get()))
    K_entry.grid(row = 2, column=1, sticky='w')

    Btn_Calculate = ctk.CTkButton(master=frame, text="Calculate", 
                                  width=90, height=30, 
                                  font=("Roboto", 16), 
                                  command=lambda: ctr.Achar_Enesima(N_entry.get(), K_entry.get()))
    Btn_Calculate.grid(row = 3, column=0, columnspan=2) 

    rstE.GetFrame(frame)