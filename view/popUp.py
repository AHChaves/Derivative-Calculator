import customtkinter as ctk

class PopUp(ctk.CTkToplevel):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.geometry('300x300')
        self.resizable(False, False)
        self.state('normal')

        self.Content()

    def Content(self):

        textinfo = "Para informar uma função clique na primeira caixa de entrada e entre no seguinte padrão: ax^n+bx^t+c, sendo x a incognita, a, b, c os coeficientes e (n, t) as potências"
        font=("Roboto", 16)


        frame = ctk.CTkFrame(master=self)
        frame.pack(pady = 12, padx=10, expand=True, fill='both')

        info = ctk.CTkLabel(master= frame, 
                            text=textinfo, 
                            wraplength=250,
                            font=font)
        info.pack(pady = 12, padx=10)

        close = ctk.CTkButton(master=frame, text="Close", font=font, command=self.destroy)
        close.pack(pady = 12, padx=10)
    


    
