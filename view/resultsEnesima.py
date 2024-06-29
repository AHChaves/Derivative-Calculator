import customtkinter as ctk

Rst_function = ctk.CTkLabel
Frame_Intervalos = ctk.CTkFrame
Frame_Raizes = ctk.CTkFrame
fontepadrao = ctk.CTkFont

def Cria_Resultados(frame, fraizes):

    global Rst_functions, Frame_Intervalos, fontepadrao, Frame_Raizes

    fontepadrao = ctk.CTkFont(family="Roboto", size=16) 
    Frame_Intervalos = frame
    Frame_Raizes = fraizes


    lIntervalos = ctk.CTkLabel(master=frame, text="Intervalos", font=("Roboto", 18))
    lIntervalos.pack(pady=10, padx=5)
    
    lRaizes = ctk.CTkLabel(master=fraizes, text="Raizes", font=("Roboto", 18))
    lRaizes.pack(pady=10, padx=5)

def Adiciona_Intervalos(valor):
    
    aux1 = f"{valor[0]:.2f}"
    aux2 = f"{valor[1]:.2f}"

    string = "({0},{1})".format(aux1, aux2)

    Intervalos = ctk.CTkLabel(master=Frame_Intervalos, text= string, font=fontepadrao)
    Intervalos.pack(pady=2, padx=10, anchor='w')

def Adiciona_Raizes(valor):
    #string = "x = {0}".format(valor)

    raizes = ctk.CTkLabel(master=Frame_Raizes, text=valor, font=fontepadrao)
    raizes.pack(pady=2, padx=10, anchor='w')