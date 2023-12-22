import tkinter as tk
from tkinter import messagebox

def enviar_formulario():
    nome = entry_nome.get()
    orcamento = entry_orcamento.get()
    genero = entry_genero.get()
    qtd_episodios = entry_qtd_episodios.get()
    qtd_temporadas = entry_qtd_temporadas.get()
    duracao_total = entry_duracao_total.get()

    # Aqui você pode realizar ações com os dados do formulário
    # Neste exemplo, apenas exibimos uma caixa de mensagem com os dados
    mensagem = (
        f"Nome: {nome}\n"
        f"Orçamento: {orcamento}\n"
        f"Gênero: {genero}\n"
        f"Quantidade de Episódios: {qtd_episodios}\n"
        f"Quantidade de Temporadas: {qtd_temporadas}\n"
        f"Duração Total: {duracao_total}"
    )
    messagebox.showinfo("Formulário Enviado", mensagem)

# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário de Série")

# Criar os widgets do formulário
label_nome = tk.Label(janela, text="Nome:")
entry_nome = tk.Entry(janela)

label_orcamento = tk.Label(janela, text="Orçamento:")
entry_orcamento = tk.Entry(janela)

label_genero = tk.Label(janela, text="Gênero:")
entry_genero = tk.Entry(janela)

label_qtd_episodios = tk.Label(janela, text="Quantidade de Episódios:")
entry_qtd_episodios = tk.Entry(janela)

label_qtd_temporadas = tk.Label(janela, text="Quantidade de Temporadas:")
entry_qtd_temporadas = tk.Entry(janela)

label_duracao_total = tk.Label(janela, text="Duração Total:")
entry_duracao_total = tk.Entry(janela)

botao_enviar = tk.Button(janela, text="Enviar", command=enviar_formulario)

# Posicionar os widgets na janela
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_orcamento.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_orcamento.grid(row=1, column=1, padx=10, pady=10)

label_genero.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_genero.grid(row=2, column=1, padx=10, pady=10)

label_qtd_episodios.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
entry_qtd_episodios.grid(row=3, column=1, padx=10, pady=10)

label_qtd_temporadas.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
entry_qtd_temporadas.grid(row=4, column=1, padx=10, pady=10)

label_duracao_total.grid(row=5, column=0, padx=10, pady=10, sticky=tk.W)
entry_duracao_total.grid(row=5, column=1, padx=10, pady=10)

botao_enviar.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()