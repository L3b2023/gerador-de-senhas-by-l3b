import tkinter as tk
from tkinter import messagebox, ttk
import random
import string
from datetime import datetime

def gerar_senha(tamanho, caracteres):
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def salvar_senha(nome, senha, data_hora):
    with open("senhas.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Senha: {senha}\n")
        arquivo.write(f"Data e Hora de Criação: {data_hora}\n")
        arquivo.write("-" * 30 + "\n")

def exibir_senha_gerada(senha):
    janela_senha = tk.Toplevel(root)
    janela_senha.title("Senha Gerada")
    janela_senha.geometry("400x200")

    tk.Label(janela_senha, text="Sua senha gerada é:", font=("Arial", 16)).pack(pady=10)
    tk.Label(janela_senha, text=senha, font=("Arial", 16), fg="blue").pack(pady=10)

    def fechar_janela_senha():
        janela_senha.destroy()

    tk.Button(janela_senha, text="Fechar", command=fechar_janela_senha, font=("Arial", 14)).pack(pady=10)

def abrir_janela_puxar_senha():
    janela_puxar_senha = tk.Toplevel(root)
    janela_puxar_senha.title("Puxar Senha")
    janela_puxar_senha.geometry("400x200")

    tk.Label(janela_puxar_senha, text="Digite o nome da senha:", font=("Arial", 16)).pack(pady=10)

    nome_puxar_senha_var = tk.StringVar()
    nome_puxar_senha_entry = tk.Entry(janela_puxar_senha, textvariable=nome_puxar_senha_var, font=("Arial", 14))
    nome_puxar_senha_entry.pack()

    def puxar_senha():
        nome_senha = nome_puxar_senha_var.get()
        senha = buscar_senha(nome_senha)

        if senha:
            senha_gerada_label.config(text="Senha puxada: " + senha)
        else:
            messagebox.showinfo("Erro", "Essa senha não existe.")

        janela_puxar_senha.destroy()

    tk.Button(janela_puxar_senha, text="Puxar Senha", command=puxar_senha, font=("Arial", 14)).pack(pady=10)

def buscar_senha(nome_senha):
    # Implemente a lógica para buscar a senha no arquivo TXT
    # Retorne a senha se encontrada, ou None se não encontrada
    with open("senhas.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for i in range(0, len(linhas), 4):
            nome = linhas[i].split(":")[1].strip()
            senha = linhas[i + 1].split(":")[1].strip()
            if nome == nome_senha:
                return senha
    return None

def limpar_campos():
    tamanho_var.set("")
    nome_var.set("")
    senha_gerada_label.config(text="")

def gerar_senha_e_salvar():
    opcao = opcao_var.get()

    # Defina o tamanho da senha
    tamanho_senha = int(tamanho_var.get())

    # Escolha os caracteres com base na opção do usuário
    if opcao == 1:
        caracteres = string.ascii_letters
    elif opcao == 2:
        caracteres = string.digits
    elif opcao == 3:
        caracteres = string.ascii_letters + string.digits
    else:
        messagebox.showinfo("Erro", "Opção inválida. Escolha 1, 2 ou 3.")
        return

    # Peça ao usuário para fornecer um nome para a senha
    nome_senha = nome_var.get()

    # Gere a senha
    senha = gerar_senha(tamanho_senha, caracteres)

    # Obtenha a data e hora de criação
    data_hora_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Exiba a senha gerada em uma nova janela
    exibir_senha_gerada(senha)

    # Salve a senha no arquivo TXT
    salvar_senha(nome_senha, senha, data_hora_criacao)

    # Limpar os campos após gerar a senha
    limpar_campos()

# Interface Gráfica
root = tk.Tk()
root.title("Gerador de Senhas by l3bZ")
root.geometry("800x600")  # Tamanho da janela

# Configuração de estilo
root.configure(bg="white")  # Fundo branco

opcao_var = tk.IntVar()
opcao_var.set(1)

tamanho_var = tk.StringVar()
nome_var = tk.StringVar()

# Configurações iniciais da interface
tk.Label(root, text="Gerador de Senhas", fg="green", bg="white", font=("Arial", 24)).pack(pady=20)

# Utilizando o estilo ttk para Checkbuttons
checkbutton_style = ttk.Style()
checkbutton_style.layout("TCheckbutton", [('Checkbutton.padding', {'sticky': 'nswe', 'children':
                    [('Checkbutton.indicator', {'expand': '0', 'side': 'left', 'sticky': 'nswe'}),
                     ('Checkbutton.focus', {'expand': '1', 'side': 'left', 'sticky': 'nswe'}),
                     ('Checkbutton.label', {'sticky': 'nswe'})]})])

checkbutton_style.configure("TCheckbutton", background="white", foreground="black")

ttk.Checkbutton(root, text="Letras", variable=opcao_var, onvalue=1, offvalue=0, style="TCheckbutton").pack()
ttk.Checkbutton(root, text="Números", variable=opcao_var, onvalue=2, offvalue=0, style="TCheckbutton").pack()
ttk.Checkbutton(root, text="Letras e Números", variable=opcao_var, onvalue=3, offvalue=0, style="TCheckbutton").pack()

tk.Label(root, text="Quantidade de caractéres da senha:", fg="black", bg="white", font=("Arial", 16)).pack()
tamanho_entry = tk.Entry(root, textvariable=tamanho_var, font=("Arial", 14))
tamanho_entry.pack()

tk.Label(root, text="Nome da senha:", fg="black", bg="white", font=("Arial", 16)).pack()
nome_entry = tk.Entry(root, textvariable=nome_var, font=("Arial", 14))
nome_entry.pack()

tk.Button(root, text="Gerar Senha", command=gerar_senha_e_salvar, font=("Arial", 16), bg="blue", fg="white").pack(pady=20)

tk.Button(root, text="Puxar Senha", command=abrir_janela_puxar_senha, font=("Arial", 16), bg="green", fg="white").pack(pady=20)

senha_gerada_label = tk.Label(root, text="", fg="black", bg="white", font=("Arial", 16))
senha_gerada_label.pack()

# Iniciar o loop principal
root.mainloop()
