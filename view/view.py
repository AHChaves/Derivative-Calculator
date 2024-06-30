import customtkinter as ctk
import sys
import os

# Caminho absoluto da pasta model
model_path = os.path.abspath('../model')
# Caminho absoluto da pasta view
view_path = os.path.abspath('.')

# Adicione os diretórios ao sys.path
sys.path.insert(0, model_path)
sys.path.insert(0, view_path)

# Verifique se os caminhos estão corretos
print(f"Model Path: {model_path}")
print(f"View Path: {view_path}")
print("Sys Path:")
for path in sys.path:
    print(path)

# Tente importar os módulos
try:
    import calc as calc
    import resultados as rst
    import resultsNewton as rstN
    import customtkinter as ctk
    import derivada as dv
    import newton as nw
    import enesima as en
    import resultsEnesima as rstE
    print("Importações realizadas com sucesso.")
except ModuleNotFoundError as e:
    print(f"Erro ao importar: {e}")

# Resto do seu código aqui

    import customtkinter as ctk
    import derivada as dv
    import newton as nw
    import enesima as en

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("425x525")
root.title("Derivative Calculator")
root.resizable(True, False)
root.minsize(425,525)

Frame = ctk.CTkFrame(master=root)
Frame.pack(fill="both", expand=True)

def Frame_Cleaner(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
    
def Go_back():
    Frame_Cleaner(Frame)
    Painel_principal()

def Create_Button(row, column, columnspan = 1):
    Btn_Back = ctk.CTkButton(master=Frame, 
                             text="Voltar", 
                             width= 60, 
                             height= 20,
                             font=("Roboto", 14),
                             command= Go_back)
    Btn_Back.grid(row = row, column = column, columnspan= columnspan, pady=12)

def Open_Derivada():
    Frame_Cleaner(Frame)
    dv.derivada(Frame)
    Create_Button(2, 0)

def Open_Raizes():
    Frame_Cleaner(Frame)
    nw.Raizes_Panel(Frame)
    Create_Button(3, 0, 2)

def Open_Enesima():
    Frame_Cleaner(Frame)
    en.Enesima_Panel(Frame)
    Create_Button(5, 0, 2)

def Painel_principal():

    Title = ctk.CTkLabel(master=Frame, text="Opções", font=("Roboto", 18))
    Title.pack(pady=12, padx=10, fill="x")

    button_calc_derivada = ctk.CTkButton(master=Frame, text="Trabalho 1", width=120, height=30,
                                          font=("Roboto",16), command= Open_Derivada)
    button_calc_derivada.pack(pady=12, padx=10)

    button_calc_raizes = ctk.CTkButton(master=Frame, text="Trabalho 2", width=120, height=30,
                                          font=("Roboto",16), command= Open_Raizes)
    button_calc_raizes.pack(pady=12, padx=10)

    button_calc_enesima = ctk.CTkButton(master=Frame, text="Trabalho 3", width=120, height=30,
                                          font=("Roboto",16), command= Open_Enesima)
    button_calc_enesima.pack(pady=12, padx=10)

Painel_principal()

root.mainloop()