
import customtkinter as ctk
import resultados as rst
import entries as etr

# Inicializa os frames
def derivada(frame):
    frame.columnconfigure((0), weight=1)
    frame.rowconfigure((0,1,2), weight=0)

    Frm_entrada = ctk.CTkFrame(master=frame)
    Frm_entrada.grid(row=0, column=0, sticky='nswe')

    Frm_mostragem = ctk.CTkFrame(master=Frm_entrada)
    Frm_mostragem.pack(pady=12, padx=10, fill="both")

    etr.create_entries(Frm_mostragem)

    Frm_Result = ctk.CTkFrame(master=frame)
    Frm_Result.grid(row=1, column=0, sticky='nswe')

    rst.Results(Frm_Result)


