
def Results():
    from view import ctk, Frm_Result

    Rst_title = ctk.CTkLabel(master=Frm_Result, text="Results", font=("Roboto", 24))
    Rst_title.grid(row=0, column=1,sticky="w")

    Rst_function = ctk.CTkLabel(master=Frm_Result, text="F(x) =", font=("Roboto", 16))
    Rst_function.grid(row=1, column=0, sticky="w")

    Rst_function_derivated = ctk.CTkLabel(master=Frm_Result, text="F'(x) = ",font=("Roboto", 16))
    Rst_function_derivated.grid(row=2, column=0, sticky="w")

    Rst_title = ctk.CTkLabel(master=Frm_Result, text="F(a)", font=("Roboto", 18))
    Rst_title.grid(row=3, column=1, sticky='w')

    Rst_Val_X = ctk.CTkLabel(master=Frm_Result, text="Insira o valor de 'x': ", font=("Roboto", 16))
    Rst_Val_X.grid(row=4, column=0, sticky="w")

    Rst_Entry_X = ctk.CTkEntry(master=Frm_Result, width=100)
    Rst_Entry_X.grid(row=4, column=1, sticky="w")

    Rst_Btn_Calcular_X = ctk.CTkButton(master=Frm_Result, text="Calculate", width=100)
    Rst_Btn_Calcular_X.grid(row=4, column=2, sticky='w')

    Rst_F = ctk.CTkLabel(master=Frm_Result, text="f(x) = ", font=("Roboto", 16))
    Rst_F.grid(row=5, column=0, sticky="w")

    Rst_FDerivate = ctk.CTkLabel(master=Frm_Result, text="f'(x) = ", font=("Roboto", 16))
    Rst_FDerivate.grid(row=5, column=1, sticky="w")

    Rst_Point = ctk.CTkLabel(master=Frm_Result, text="P(X,f(x))", font=("Roboto", 16))
    Rst_Point.grid(row=5, column=2, sticky="w")