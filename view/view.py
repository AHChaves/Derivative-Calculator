import customtkinter as ctk
import derivada as dv
import enesima as en

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("400x525")
root.title("Derivative Calculator")
root.resizable(True, False)
root.minsize(400,480)

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

def Open_Enesima():
    Frame_Cleaner(Frame)
    en.Enesima_Panel(Frame)
    Create_Button(2, 0, 2)

def Painel_principal():

    Title = ctk.CTkLabel(master=Frame, text="Opções", font=("Roboto", 18))
    Title.pack(pady=12, padx=10, fill="x")

    button_calc_derivada = ctk.CTkButton(master=Frame, text="Trabalho 1", width=120, height=30,
                                          font=("Roboto",16), command= Open_Derivada)
    button_calc_derivada.pack(pady=12, padx=10)

    button_calc_enesima = ctk.CTkButton(master=Frame, text="Trabalho 2", width=120, height=30,
                                          font=("Roboto",16), command= Open_Enesima)
    button_calc_enesima.pack(pady=12, padx=10)

Painel_principal()

root.mainloop()