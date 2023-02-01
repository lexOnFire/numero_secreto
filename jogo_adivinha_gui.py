from tkinter import Tk
import tkinter as tk
import tkinter.messagebox as mb
import customtkinter as ct
import random
import time
tempo_inicial = time.time() 
    
def jogar():
    
    #isso aqui é temporario
    numero_aleatorio = random.randint(1,50)
    #funçao para escrever os numeros
    def numero():
        vencedor()
        caixa_ferramenta()
        
        if numero_digitado <= numero_aleatorio:
            lbl_numero.configure(text="o numero é maior")
            caixa_texto.delete(0,tk.END)
        else:
            lbl_numero.configure(text="o numero é menor")
            caixa_texto.delete(0,tk.END)
    #funçao para definir a dificuldade facil
    def dificuldade_facil():
        global Numero_aleatorio
        
        Numero_aleatorio = random.randint(1,50)
        caixa_medio.configure(state="Disabled")
        caixa_dificil.configure(state="Disabled")
        
        dificuldade_facil()
       
    #funçao para definir a dificuldade medio
    def dificuldade_medio():
        global numero_aleatorio
        
        if caixa_facil:
            caixa_facil.configure(state="Disabled")

        numero_aleatorio = random.randint(1,100)
        
        caixa_dificil.configure(state="Disabled")
        caixa_facil.deselect(True)
    #funçao para definir a dificuldade dificil   
    def dificuldade_dificil():
        global numero_aleatorio
        if caixa_facil:
            caixa_facil.configure(state="Disabled")
            caixa_facil.deselect(True)
        numero_aleatorio = random.randint(1,1000)
        caixa_facil.configure(state="Disabled")
        caixa_medio.configure(state="Disabled")
    #funçao para ganhador    
    def vencedor():
        global numero_digitado
        
        numero_digitado = int(caixa_texto.get())
        
        
        if numero_digitado == numero_aleatorio:
            lbl_n_aleatorio.configure(text=f"{numero_aleatorio}")
            caixa_texto.delete(0,tk.END)
            mensagem =  mb.askyesno("Venceu", "Parabens voce Venceu!\n Deseja continuar?")
            
            
            if mensagem:
                janela.destroy()
                
                janela.mainloop()
                jogar()
            else:
                janela.destroy()
                
            return numero_digitado   
    # funçao para tempo        
    def tempo():
        
        while True:
            tempo_final = time.time()
            total_tempo = tempo_final - tempo_inicial
            segundo = int(total_tempo)       
            janela.update()

            if vencedor == True:               
                break 
        tempo()       
    #funçao para todos objtos da janela(lbl, entry, btn, etc)
    def caixa_ferramenta():
        global caixa_texto
        global lbl_numero
        global caixa_facil
        global caixa_medio
        global caixa_dificil
        global lbl_n_aleatorio
        global lbl_time
        
        lbl_n_aleatorio = ct.CTkLabel(janela,text="???",font=("Numero 10 Clean", 45))  
        lbl_n_aleatorio.place(relx=0.4,rely=0.3)
        
        caixa_facil = ct.CTkCheckBox(janela, width=80, height=20, text="FACIL", command=dificuldade_facil)
        caixa_facil.place(relx=0,rely=0.7)
        caixa_facil.configure(state="disabled")
        caixa_facil.select(True)
        
        caixa_medio = ct.CTkCheckBox(janela, width=80, height=20, text="MÉDIO", command=dificuldade_medio)
        caixa_medio.place(relx=0,rely=0.8)
        
        caixa_dificil = ct.CTkCheckBox(janela, width=80, height=20, text="DIFICIL", command=dificuldade_dificil)
        caixa_dificil.place(relx=0,rely=0.9)
        
        lbl_numero = tk.Label(janela, width=20, height=1, font=("Javanica Free Trial", 15), fg="#32a8a6",bg="#21211b")
        lbl_numero.place(relx=0.2,rely=0.5)
        
        lbl_text = tk.Label(janela, width=30, height=5, font=("Masque", 12), fg="#32a8a6",bg="#21211b", text="Bem Vindo ao numero magico,\nvoce consegue adivinhar\n qual é o numero?")
        lbl_text.place(relx=0.01,rely=0)
        
        lbl_text_time = tk.Label(janela, width=1, height=1, font=("Masque", 12), fg="#32a8a6",bg="#21211b")
        lbl_text_time.place(relx=0.01,rely=0)
        
        lbl_time = tk.Label(janela, width=10,height=1, bg="#21211b", text="00:00",font=("Helvetica",10),fg="#32a8a6")
        lbl_time.place(relx=0.7,y=143)
        
        caixa_texto = ct.CTkEntry(janela)   
        caixa_texto.place(relx=0.3,rely=0.6)
        
        btn_enviar =  ct.CTkButton(janela,text="Enviar",command=numero)
        btn_enviar.place(relx=0.3,rely=0.8)
        
        return caixa_ferramenta
    #funçao para janela
    def janela_main():
        global janela
        janela = ct.CTk()
        janela.title("Adivinha numero")
        janela.geometry("300x300")
    
        ct.set_appearance_mode("dark-blue")
        ct.set_default_color_theme("green")    
    janela_main()
    caixa_ferramenta()
    janela.mainloop()    
jogar()