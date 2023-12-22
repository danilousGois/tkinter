import tkinter as tk

projetos = []

# Criar a janela principal
janela = tk.Tk()
janela.title("Menu com 4 Botões")

# Criar os botões
botao1 = tk.Button(janela, text="Botão 1")
botao2 = tk.Button(janela, text="Botão 2")
botao3 = tk.Button(janela, text="Botão 3")
botao4 = tk.Button(janela, text="Botão 4")

# Posicionar os botões na janela
botao1.pack(pady=10)
botao2.pack(pady=10)
botao3.pack(pady=10)
botao4.pack(pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()