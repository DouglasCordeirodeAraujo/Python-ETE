import tkinter as tk

janela = tk.Tk()
janela.title("Interface Gráfica com Tkinter")
janela.geometry("300x200")

rotulo = tk.Label(janela, text="Olá Mundo")

rotulo.pack()

janela.mainloop()