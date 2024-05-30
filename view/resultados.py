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
    Rst_title.grid(row=0, column=1,sticky="w", )

    Rst_function = ctk.CTkLabel(master=panel, text="f(x) =", font=fontepadrao)
    Rst_function.grid(row=1, column=0, sticky="w", padx=10)

    Rst_function_derivated = ctk.CTkLabel(master=panel, text="f'(x) = ",font=fontepadrao)
    Rst_function_derivated.grid(row=2, column=0, sticky="w", padx=10)

    # Valores Funcionais

    Rst_title_FA = ctk.CTkLabel(master=panel, text="F(a)", font=("Roboto", 18))
    Rst_title_FA.grid(row=3, column=1, sticky='w')

    Rst_Val_X = ctk.CTkLabel(master=panel, text="Insira o valor de 'x': ", font=fontepadrao)
    Rst_Val_X.grid(row=4, column=0, sticky="w", padx=10)

    Rst_Entry_X = ctk.CTkEntry(master=panel, width=100)
    Rst_Entry_X.grid(row=4, column=1, sticky="w", padx=10)

    Rst_Btn_Calcular_X = ctk.CTkButton(master=panel, text="Calculate", width=80, command= lambda: ctr.ValorX(Rst_Entry_X.get()))
    Rst_Btn_Calcular_X.grid(row=4, column=2, sticky='w')

    Rst_F = ctk.CTkLabel(master=panel, text="f(x) = ", font=fontepadrao)
    Rst_F.grid(row=5, column=0, sticky="w", padx=10)

    Rst_FDerivate = ctk.CTkLabel(master=panel, text="f'(x) = ", font=fontepadrao)
    Rst_FDerivate.grid(row=5, column=1, sticky="w")

    Rst_Point = ctk.CTkLabel(master=panel, text="P(X,f(x))", font=fontepadrao)
    Rst_Point.grid(row=5, column=2, sticky="w")

    # Reta tangente

    Rst_title_Tg = ctk.CTkLabel(master=panel, text="Reta Tangente", font=("Roboto", 18))
    Rst_title_Tg.grid(row=6, column=1, sticky='w')

    Rst_tg = ctk.CTkLabel(master=panel, text="y = ", font=fontepadrao)
    Rst_tg.grid(row=7, column=0, sticky="w", padx=10)

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

