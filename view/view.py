import customtkinter as ctk
import resultados as rst
import entries as etr

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("400x480")
root.title("Derivative Calculator")
root.resizable(True, False)

# Inicializa os frames
Frm_Geral = ctk.CTkFrame(master=root)
Frm_Geral.pack(fill="both", expand=True)
Frm_Geral.columnconfigure((0), weight=1)
Frm_Geral.rowconfigure((0,1), weight=0)

Frm_entrada = ctk.CTkFrame(master=Frm_Geral)
Frm_entrada.grid(row=0, column=0, sticky='nswe')

Frm_mostragem = ctk.CTkFrame(master=Frm_entrada)
Frm_mostragem.pack(pady=12, padx=10, fill="both")

etr.create_entries(Frm_mostragem)

Frm_Result = ctk.CTkFrame(master=Frm_Geral)
Frm_Result.grid(row=1, column=0, sticky='nswe')

rst.Results(Frm_Result)

root.mainloop()
