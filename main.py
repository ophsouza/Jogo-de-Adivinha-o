import tkinter as tk
from tkinter import messagebox
import random

# Criar a janela principal
janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("300x200")

# Gerar um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0

def verificar_tentativa():
    global tentativas
    tentativas += 1
    tentativa = int(entrada.get())

    if tentativa < numero_secreto:
        resultado.config(text="Muito baixo!")
    elif tentativa > numero_secreto:
        resultado.config(text="Muito alto!")
    else:
        resultado.config(text=f"Parabéns! Você adivinhou em {tentativas} tentativas.")
        messagebox.showinfo("Vitória", f"Você adivinhou o número em {tentativas} tentativas!")
        resetar_jogo()

def resetar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    entrada.delete(0, tk.END)
    resultado.config(text="")

# Rótulo
rotulo = tk.Label(janela, text="Digite um número entre 1 e 100:")
rotulo.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela)
entrada.pack(pady=10)

# Botão para verificar a tentativa
botao = tk.Button(janela, text="Verificar", command=verificar_tentativa)
botao.pack(pady=10)

# Rótulo para mostrar o resultado
resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

# Iniciar o loop principal
janela.mainloop()
