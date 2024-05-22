
def create_entries():
    from view import ctk, Frm_entrada
    Btn_clear = ctk.CTkButton(master=Frm_entrada, text="Clear", width=100, height=30, font=("Roboto", 16))
    Btn_clear.grid(column=0, row=1)

    Btn_Division = ctk.CTkButton(master=Frm_entrada, text="/", width=100, height=30, font=("Roboto", 16))
    Btn_Division.grid(column=1, row=1)

    Btn_Multiply = ctk.CTkButton(master=Frm_entrada, text="*", width=100, height=30, font=("Roboto", 16))
    Btn_Multiply.grid(column=2, row=1)

    Btn_Minus = ctk.CTkButton(master=Frm_entrada, text="-", width=100, height=30, font=("Roboto", 16))
    Btn_Minus.grid(column=3, row=1)

    Btn_Seven = ctk.CTkButton(master=Frm_entrada, text="7", width=100, height=30, font=("Roboto", 16))
    Btn_Seven.grid(column=0, row=2)

    Btn_Eight = ctk.CTkButton(master=Frm_entrada, text="8", width=100, height=30, font=("Roboto", 16))
    Btn_Eight.grid(column=1, row=2)

    Btn_Nine = ctk.CTkButton(master=Frm_entrada, text="9", width=100, height=30, font=("Roboto", 16))
    Btn_Nine.grid(column=2, row=2)

    Btn_Plus = ctk.CTkButton(master=Frm_entrada, text="+", width=100, height=30, font=("Roboto", 16))
    Btn_Plus.grid(column=3, row=2)

    Btn_Four = ctk.CTkButton(master=Frm_entrada, text="4", width=100, height=30, font=("Roboto", 16))
    Btn_Four.grid(column=0, row=3)

    Btn_Five = ctk.CTkButton(master=Frm_entrada, text="5", width=100, height=30, font=("Roboto", 16))
    Btn_Five.grid(column=1, row=3)

    Btn_Six = ctk.CTkButton(master=Frm_entrada, text="6", width=100, height=30, font=("Roboto", 16))
    Btn_Six.grid(column=2, row=3)

    Btn_Dot = ctk.CTkButton(master=Frm_entrada, text=".", width=100, height=30, font=("Roboto", 16))
    Btn_Dot.grid(column=3, row=3)

    Btn_One = ctk.CTkButton(master=Frm_entrada, text="1", width=100, height=30, font=("Roboto", 16))
    Btn_One.grid(column=0, row=4)

    Btn_Two = ctk.CTkButton(master=Frm_entrada, text="2", width=100, height=30, font=("Roboto", 16))
    Btn_Two.grid(column=1, row=4)

    Btn_Three = ctk.CTkButton(master=Frm_entrada, text="3", width=100, height=30, font=("Roboto", 16))
    Btn_Three.grid(column=2, row=4)

    Btn_Pow = ctk.CTkButton(master=Frm_entrada, text="^", width=100, height=30, font=("Roboto", 16))
    Btn_Pow.grid(column=3, row=4)

    Btn_Zero = ctk.CTkButton(master=Frm_entrada, text="0", width=100, height=30, font=("Roboto", 16))
    Btn_Zero.grid(column=0, row=5)

    Btn_X = ctk.CTkButton(master=Frm_entrada, text="X", width=100, height=30, font=("Roboto", 16))
    Btn_X.grid(column=1, row=5)

    Btn_Calculate = ctk.CTkButton(master=Frm_entrada, text="Calculate", width=215, height=30, font=("Roboto", 16))
    Btn_Calculate.grid(column=2, columnspan= 2,row=5)

