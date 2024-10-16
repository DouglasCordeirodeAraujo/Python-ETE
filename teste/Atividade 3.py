import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Informação", "Divertidamente")

janela = tk.Tk()
janela.title("Interface Gráfica com Imagens")
janela.geometry("800x500")

imagem_logo = tk.PhotoImage(file="divertidamente.png")

rotulo_imagem = tk.Label(janela, image=imagem_logo)

rotulo_imagem.pack(pady=10)

rotulo_texto = tk.Label(janela, text="Quer saber que filme é esse?")
rotulo_texto.pack(pady=10)

imagem_botao = tk.PhotoImage(file="botao.png")

botao_imagem = tk.Button(janela, image=imagem_botao, command=mostrar_mensagem)
botao_imagem.pack(pady=20)

janela.mainloop()