import sys
import customtkinter as ctk
from entries import EntryWithLimitation

sys.path.insert(0, '../controler')
import controler as ctr

def Enesima_Panel(frame):

    CharList = ["x", "X", "+", "-", "^"]

    frame.columnconfigure((0,1), weight=1, pad=10)
    frame.rowconfigure((0,1,2), weight=0, pad=10)

    Titulo = ctk.CTkLabel(master=frame, text="Trabalho 2", font= ("Roboto", 24))
    Titulo.grid(row=0, column=0, columnspan=2, sticky='nswe')

    function_entry = EntryWithLimitation(frame, CharList)
    function_entry.bind("<Return>", lambda event = None: ctr.Achar_Intervalos(function_entry.get()))
    function_entry.pack(pady=10, padx=10, fill="x")

    Btn_Calculate = ctk.CTkButton(master=frame, text="Calculate", 
                                  width=90, height=30, 
                                  font=("Roboto", 16), 
                                  command=lambda: ctr.Achar_Intervalos(function_entry.get()))
    Btn_Calculate.pack(pady=10, padx=10, fill="x")


