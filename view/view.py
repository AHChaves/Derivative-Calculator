import customtkinter as ctk
import sys

sys.path.insert(0, './/controler')

import controler
import entries as etr

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


root = ctk.CTk()
root.geometry("500x400")
root.title("Derivative Calculator")

#Inicio

## Mostragem

Frm_entrada = ctk.CTkFrame(master=root)
Frm_entrada.pack(pady=10, padx=20, fill="both", expand=True)
Frm_entrada.columnconfigure((0,1,2,3), weight=1, pad=2)
Frm_entrada.rowconfigure((0,1,2,3,4,5), weight=0, pad=20)

Frm_mostragem = ctk.CTkFrame(master=Frm_entrada)
Frm_mostragem.grid(row=0, column=0, sticky='nswe', columnspan=4,rowspan=1)

label = ctk.CTkLabel(master=Frm_mostragem, text="Derivative Calculator", font=("Roboto", 24))
label.pack(pady=12, padx=10, fill="x")

function_entry = ctk.CTkEntry(master=Frm_mostragem, placeholder_text="F(x)=", state='disabled')
function_entry.pack(pady=10, padx=10, fill="x")

## Entradas

etr.create_entries()

root.mainloop()
