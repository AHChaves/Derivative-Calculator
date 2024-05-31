import customtkinter as ctk
import sys

sys.path.insert(0, './controler')
import controler as ctr

Rst_function = ctk.CTkLabel
Rst_function_derivated = ctk.CTkLabel
Rst_F = ctk.CTkLabel
Rst_FDerivate = ctk.CTkLabel
Rst_Point = ctk.CTkLabel
Rst_tg = ctk.CTkLabel

def Results(panel):

    global Rst_function, Rst_function_derivated
    global Rst_F, Rst_FDerivate, Rst_Point, Rst_tg

    fontepadrao = ctk.CTkFont(family="Roboto", size=16)

    # Resultados basicos

    Rst_title = ctk.CTkLabel(master=panel, text="Results", font=("Roboto", 24))
    Rst_title.pack(pady=5, padx=10, fill="x")

    Rst_function = ctk.CTkLabel(master=panel, text="f(x) =", font=fontepadrao)
    Rst_function.pack(pady=2, padx=10, anchor='w')

    Rst_function_derivated = ctk.CTkLabel(master=panel, text="f'(x) = ",font=fontepadrao)
    Rst_function_derivated.pack(pady=2, padx=10, anchor='w')

    # Valores Funcionais


    Rst_title_FA = ctk.CTkLabel(master=panel, text="F(a)", font=("Roboto", 18))
    Rst_title_FA.pack(pady=5, padx=10)

    EntradaFuncional = ctk.CTkFrame(master=panel)
    EntradaFuncional.pack(pady=2, padx=10, fill='x')
    
    Rst_Val_X = ctk.CTkLabel(master=EntradaFuncional, text="Insira o valor de 'x': ", font=fontepadrao)
    Rst_Val_X.pack(pady=5, padx=5, side="left", expand=True)

    Rst_Entry_X = ctk.CTkEntry(master=EntradaFuncional, width=100)
    Rst_Entry_X.bind("<Return>", lambda event = None: ctr.ValorX(Rst_Entry_X.get()))
    Rst_Entry_X.pack(pady=5, padx=5, side="left", anchor='center', fill='x', expand=True)

    Rst_Btn_Calcular_X = ctk.CTkButton(master=EntradaFuncional, text="Calculate", width=80, command= lambda: ctr.ValorX(Rst_Entry_X.get()))
    Rst_Btn_Calcular_X.pack(pady=5, padx=5, side="left", anchor='e', expand=True)

    Rst_EntradaFuncional = ctk.CTkFrame(master=panel)
    Rst_EntradaFuncional.pack(pady=2, padx=10, fill='x')

    Rst_F = ctk.CTkLabel(master=Rst_EntradaFuncional, text="f(x) = ", font=fontepadrao)
    Rst_F.pack(pady=5, padx=5, side="left")

    Rst_FDerivate = ctk.CTkLabel(master=Rst_EntradaFuncional, text="f'(x) = ", font=fontepadrao)
    Rst_FDerivate.pack(pady=5, padx=5, side="left")

    Rst_Point = ctk.CTkLabel(master=Rst_EntradaFuncional, text="P(X,f(x))", font=fontepadrao)
    Rst_Point.pack(pady=5, padx=5, side="left")

    # Reta tangente

    Rst_title_Tg = ctk.CTkLabel(master=panel, text="Reta Tangente", font=("Roboto", 18))
    Rst_title_Tg.pack(pady=5, padx=10)

    Rst_tg = ctk.CTkLabel(master=panel, text="y = ", font=fontepadrao)
    Rst_tg.pack(pady=5, padx=10, anchor='w')

def SetResults(funcao, derivada):

    global Rst_function, Rst_function_derivated

    Rst_function.configure(text=funcao)
    Rst_function_derivated.configure(text=derivada)

def SetFuncional(funcao, derivada, ponto, tangente):

    global Rst_F, Rst_FDerivate, Rst_Point, Rst_tg

    Rst_F.configure(text=funcao)
    Rst_FDerivate.configure(text=derivada)
    Rst_Point.configure(text=ponto)
    Rst_tg.configure(text=tangente)

