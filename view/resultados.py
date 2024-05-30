import customtkinter as ctk


def Results(panel):

    Rst_title = ctk.CTkLabel(master=panel, text="Results", font=("Roboto", 24))
    Rst_title.grid(row=0, column=1,sticky="w")

    Rst_function = ctk.CTkLabel(master=panel, text="F(x) =", font=("Roboto", 16))
    Rst_function.grid(row=1, column=0, sticky="w")

    Rst_function_derivated = ctk.CTkLabel(master=panel, text="F'(x) = ",font=("Roboto", 16))
    Rst_function_derivated.grid(row=2, column=0, sticky="w")

    Rst_title_FA = ctk.CTkLabel(master=panel, text="F(a)", font=("Roboto", 18))
    Rst_title_FA.grid(row=3, column=1, sticky='w')

    Rst_Val_X = ctk.CTkLabel(master=panel, text="Insira o valor de 'x': ", font=("Roboto", 16))
    Rst_Val_X.grid(row=4, column=0, sticky="w")

    Rst_Entry_X = ctk.CTkEntry(master=panel, width=100)
    Rst_Entry_X.grid(row=4, column=1, sticky="w")

    Rst_Btn_Calcular_X = ctk.CTkButton(master=panel, text="Calculate", width=100)
    Rst_Btn_Calcular_X.grid(row=4, column=2, sticky='w')

    Rst_F = ctk.CTkLabel(master=panel, text="f(x) = ", font=("Roboto", 16))
    Rst_F.grid(row=5, column=0, sticky="w")

    Rst_FDerivate = ctk.CTkLabel(master=panel, text="f'(x) = ", font=("Roboto", 16))
    Rst_FDerivate.grid(row=5, column=1, sticky="w")

    Rst_Point = ctk.CTkLabel(master=panel, text="P(X,f(x))", font=("Roboto", 16))
    Rst_Point.grid(row=5, column=2, sticky="w")

    Rst_title_Tg = ctk.CTkLabel(master=panel, text="Reta Tangente", font=("Roboto", 18))
    Rst_title_Tg.grid(row=6, column=1, sticky='w')

    Rst_tg = ctk.CTkLabel(master=panel, text="y = ", font=("Roboto", 16))
    Rst_tg.grid(row=7, column=0, sticky="w")
