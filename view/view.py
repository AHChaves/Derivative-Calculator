from tkinter import StringVar
import customtkinter as ctk
import resultados as rst
import entries as etr

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x380")
root.title("Derivative Calculator")
root.resizable(False, False)

# Inicializa os frames
Frm_Geral = ctk.CTkFrame(master=root)
Frm_Geral.pack(fill="both", expand=True)
Frm_Geral.columnconfigure((0, 1), weight=1, uniform='a')
Frm_Geral.rowconfigure((0), weight=1)

Frm_entrada = ctk.CTkFrame(master=Frm_Geral)
Frm_entrada.grid(row=0, column=0, sticky='nswe')
Frm_entrada.columnconfigure((0, 1, 2, 3), weight=1, pad=5)
Frm_entrada.rowconfigure((0, 1, 2, 3, 4, 5), weight=0, pad=20)

Frm_mostragem = ctk.CTkFrame(master=Frm_entrada)
Frm_mostragem.grid(row=0, column=0, sticky='nswe', columnspan=4, rowspan=1)

etr.create_entries(Frm_mostragem)

Frm_Result = ctk.CTkFrame(master=Frm_Geral)
Frm_Result.grid(row=0, column=1, sticky='nswe', padx=10)
Frm_Result.columnconfigure((0, 1, 2), weight=0, uniform='a')
Frm_Result.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=0, pad=10)

rst.Results()

root.mainloop()