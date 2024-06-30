import sys
import customtkinter as ctk
import resultsNewton as rstN
from entries import EntryWithLimitation

sys.path.insert(0, '../controler')
import controler as ctr

def Raizes_Panel(frame):

    CharList = ["x", "X", "+", "-", "^"]

    frame.columnconfigure((0,1), weight=1, pad=10)
    frame.rowconfigure((0,1,2,3), weight=0, pad=10)

    Titulo = ctk.CTkLabel(master=frame, text="Trabalho 2", font= ("Roboto", 24))
    Titulo.grid(row=0, column=0, columnspan=2, sticky='nswe')

    function_entry = EntryWithLimitation(frame, CharList)
    function_entry.configure(width=200)
    function_entry.bind("<Return>", lambda event = None: ctr.Achar_Intervalos(function_entry.get()))
    function_entry.grid(row = 1, column=0)

    Btn_Calculate = ctk.CTkButton(master=frame, text="Calculate", 
                                  width=90, height=30, 
                                  font=("Roboto", 16), 
                                  command=lambda: ctr.Achar_Intervalos(function_entry.get()))
    Btn_Calculate.grid(row = 1, column=1)

    Frame_Results = ctk.CTkFrame(master=frame)
    Frame_Results.grid(row=2, column=0, sticky='nswe')
    Frame_Raizes = ctk.CTkFrame(master=frame)
    Frame_Raizes.grid(row=2, column=1, sticky='nswe')
    rstN.Cria_Resultados(Frame_Results, Frame_Raizes)
