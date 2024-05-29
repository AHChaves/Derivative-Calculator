import sys

sys.path.insert(0, './controler')
import controler as ctr


def create_entries():
    from view import ctk, Frm_entrada, function_entry

    Btn_clear = ctk.CTkButton(master=Frm_entrada, text="Clear", width=90, height=30, font=("Roboto", 16), command= lambda:ctr.clear(function_entry))
    Btn_clear.grid(column=0, row=1)

    Btn_Calculate = ctk.CTkButton(master=Frm_entrada, text="Calculate", width=90, height=30, font=("Roboto", 16), command=lambda: ctr.num("calculate"))
    Btn_Calculate.grid(column=3,row=5)


