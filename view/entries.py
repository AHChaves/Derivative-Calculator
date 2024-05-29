import sys

sys.path.insert(0, './controler')
import controler as ctr


def create_entries():
    from view import ctk, Frm_entrada, text_result

    Btn_clear = ctk.CTkButton(master=Frm_entrada, text="Clear", width=90, height=30, font=("Roboto", 16), command= lambda:ctr.num("Clear", text_result))
    Btn_clear.grid(column=0, row=1)

    Btn_Division = ctk.CTkButton(master=Frm_entrada, text="/", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("/", text_result))
    Btn_Division.grid(column=1, row=1)

    Btn_Multiply = ctk.CTkButton(master=Frm_entrada, text="*", width=90, height=30, font=("Roboto", 16), command=lambda:ctr.num("*", text_result))
    Btn_Multiply.grid(column=2, row=1)

    Btn_Minus = ctk.CTkButton(master=Frm_entrada, text="-", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("-", text_result))
    Btn_Minus.grid(column=3, row=1)

    Btn_Seven = ctk.CTkButton(master=Frm_entrada, text="7", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("7", text_result))
    Btn_Seven.grid(column=0, row=2)

    Btn_Eight = ctk.CTkButton(master=Frm_entrada, text="8", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("8", text_result))
    Btn_Eight.grid(column=1, row=2)

    Btn_Nine = ctk.CTkButton(master=Frm_entrada, text="9", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("9", text_result))
    Btn_Nine.grid(column=2, row=2)

    Btn_Plus = ctk.CTkButton(master=Frm_entrada, text="+", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("+", text_result))
    Btn_Plus.grid(column=3, row=2)

    Btn_Four = ctk.CTkButton(master=Frm_entrada, text="4", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("4", text_result))
    Btn_Four.grid(column=0, row=3)

    Btn_Five = ctk.CTkButton(master=Frm_entrada, text="5", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("5", text_result))
    Btn_Five.grid(column=1, row=3)

    Btn_Six = ctk.CTkButton(master=Frm_entrada, text="6", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("6", text_result))
    Btn_Six.grid(column=2, row=3)

    Btn_Dot = ctk.CTkButton(master=Frm_entrada, text=".", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num(".", text_result))
    Btn_Dot.grid(column=3, row=3)

    Btn_One = ctk.CTkButton(master=Frm_entrada, text="1", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("1", text_result))
    Btn_One.grid(column=0, row=4)

    Btn_Two = ctk.CTkButton(master=Frm_entrada, text="2", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("2", text_result))
    Btn_Two.grid(column=1, row=4)

    Btn_Three = ctk.CTkButton(master=Frm_entrada, text="3", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("3", text_result))
    Btn_Three.grid(column=2, row=4)

    Btn_Pow = ctk.CTkButton(master=Frm_entrada, text="^", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("^", text_result))
    Btn_Pow.grid(column=3, row=4)

    Btn_Zero = ctk.CTkButton(master=Frm_entrada, text="0", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("0", text_result))
    Btn_Zero.grid(column=0, row=5)

    Btn_X = ctk.CTkButton(master=Frm_entrada, text="X", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("x", text_result))
    Btn_X.grid(column=1, row=5,)

    Btn_Calculate = ctk.CTkButton(master=Frm_entrada, text="Del", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("del"))
    Btn_Calculate.grid(column=2,row=5)
    Btn_Calculate = ctk.CTkButton(master=Frm_entrada, text="Calculate", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("calculate"))
    Btn_Calculate.grid(column=3,row=5)


