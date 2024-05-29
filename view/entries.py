import sys

sys.path.insert(0, './/controler')
import controler as ctr


def create_entries():
    from view import ctk, Frm_entrada

    Btn_clear = ctk.CTkButton(master=Frm_entrada, text="Clear", width=90, height=30, font=("Roboto", 16), command=ctr.Clear)
    Btn_clear.grid(column=0, row=1)

    Btn_Division = ctk.CTkButton(master=Frm_entrada, text="/", width=90, height=30, font=("Roboto", 16), command=ctr.Division)
    Btn_Division.grid(column=1, row=1)

    Btn_Multiply = ctk.CTkButton(master=Frm_entrada, text="*", width=90, height=30, font=("Roboto", 16), command=ctr.Multiply)
    Btn_Multiply.grid(column=2, row=1)

    Btn_Minus = ctk.CTkButton(master=Frm_entrada, text="-", width=90, height=30, font=("Roboto", 16), command=ctr.Minus)
    Btn_Minus.grid(column=3, row=1)

    Btn_Seven = ctk.CTkButton(master=Frm_entrada, text="7", width=90, height=30, font=("Roboto", 16), command=ctr.Seven)
    Btn_Seven.grid(column=0, row=2)

    Btn_Eight = ctk.CTkButton(master=Frm_entrada, text="8", width=90, height=30, font=("Roboto", 16), command=ctr.Eight)
    Btn_Eight.grid(column=1, row=2)

    Btn_Nine = ctk.CTkButton(master=Frm_entrada, text="9", width=90, height=30, font=("Roboto", 16), command=ctr.Nine)
    Btn_Nine.grid(column=2, row=2)

    Btn_Plus = ctk.CTkButton(master=Frm_entrada, text="+", width=90, height=30, font=("Roboto", 16), command=ctr.Plus)
    Btn_Plus.grid(column=3, row=2)

    Btn_Four = ctk.CTkButton(master=Frm_entrada, text="4", width=90, height=30, font=("Roboto", 16), command=ctr.Four)
    Btn_Four.grid(column=0, row=3)

    Btn_Five = ctk.CTkButton(master=Frm_entrada, text="5", width=90, height=30, font=("Roboto", 16), command=ctr.Five)
    Btn_Five.grid(column=1, row=3)

    Btn_Six = ctk.CTkButton(master=Frm_entrada, text="6", width=90, height=30, font=("Roboto", 16), command=ctr.Six)
    Btn_Six.grid(column=2, row=3)

    Btn_Dot = ctk.CTkButton(master=Frm_entrada, text=".", width=90, height=30, font=("Roboto", 16), command=ctr.Dot)
    Btn_Dot.grid(column=3, row=3)

    Btn_One = ctk.CTkButton(master=Frm_entrada, text="1", width=90, height=30, font=("Roboto", 16), command=ctr.One)
    Btn_One.grid(column=0, row=4)

    Btn_Two = ctk.CTkButton(master=Frm_entrada, text="2", width=90, height=30, font=("Roboto", 16), command=ctr.Two)
    Btn_Two.grid(column=1, row=4)

    Btn_Three = ctk.CTkButton(master=Frm_entrada, text="3", width=90, height=30, font=("Roboto", 16), command=ctr.Three)
    Btn_Three.grid(column=2, row=4)

    Btn_Pow = ctk.CTkButton(master=Frm_entrada, text="^", width=90, height=30, font=("Roboto", 16), command=ctr.Potence)
    Btn_Pow.grid(column=3, row=4)

    Btn_Zero = ctk.CTkButton(master=Frm_entrada, text="0", width=90, height=30, font=("Roboto", 16), command=ctr.Zero)
    Btn_Zero.grid(column=0, row=5)

    Btn_X = ctk.CTkButton(master=Frm_entrada, text="X", width=90, height=30, font=("Roboto", 16), command=ctr.X)
    Btn_X.grid(column=1, row=5,)

    Btn_Calculate = ctk.CTkButton(master=Frm_entrada, text="Del", width=90, height=30, font=("Roboto", 16), command=ctr.Delete)
    Btn_Calculate.grid(column=2,row=5)
    Btn_Calculate = ctk.CTkButton(master=Frm_entrada, text="Calculate", width=90, height=30, font=("Roboto", 16), command=ctr.calculator)
    Btn_Calculate.grid(column=3,row=5)


