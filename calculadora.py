import tkinter as tk
from tkinter import messagebox

# Função para processar a entrada da calculadora
def on_button_click(value):
    current_text = entry.get()
    if value == "C":
        entry.delete(0, tk.END)  # Limpa a entrada
    elif value == "=":
        try:
            result = eval(current_text)  # Avalia a expressão matemática
            entry.delete(0, tk.END)  # Limpa a entrada
            entry.insert(tk.END, str(result))  # Insere o resultado
        except Exception as e:
            messagebox.showerror("Erro", "Entrada inválida")  # Exibe uma mensagem de erro
            entry.delete(0, tk.END)  # Limpa a entrada
    else:
        entry.insert(tk.END, value)  # Insere o valor clicado

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")  # Tamanho da janela

# Campo de entrada onde os números e expressões aparecem
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões da calculadora
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Criação dos botões da interface
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=lambda value=button: on_button_click(value)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Inicia o loop da interface
root.mainloop()
