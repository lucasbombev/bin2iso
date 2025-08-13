import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def selecionar_arquivo_bin():
    """Abre uma caixa de diálogo para selecionar o arquivo .bin."""
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo .bin",
        filetypes=(("Arquivos BIN", "*.bin"), ("Todos os arquivos", "*.*"))
    )
    if caminho_arquivo:
        entry_bin.delete(0, tk.END)
        entry_bin.insert(0, caminho_arquivo)
        # Tenta encontrar o arquivo .cue correspondente
        caminho_cue_sugerido = os.path.splitext(caminho_arquivo)[0] + ".cue"
        if os.path.exists(caminho_cue_sugerido):
            entry_cue.delete(0, tk.END)
            entry_cue.insert(0, caminho_cue_sugerido)

def selecionar_arquivo_cue():
    """Abre uma caixa de diálogo para selecionar o arquivo .cue."""
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo .cue",
        filetypes=(("Arquivos CUE", "*.cue"), ("Todos os arquivos", "*.*"))
    )
    if caminho_arquivo:
        entry_cue.delete(0, tk.END)
        entry_cue.insert(0, caminho_arquivo)

def selecionar_saida_iso():
    """Abre uma caixa de diálogo para definir o local e nome do arquivo .iso de saída."""
    caminho_arquivo = filedialog.asksaveasfilename(
        title="Salvar arquivo .iso como...",
        defaultextension=".iso",
        filetypes=(("Arquivos ISO", "*.iso"), ("Todos os arquivos", "*.*"))
    )
    if caminho_arquivo:
        entry_iso.delete(0, tk.END)
        entry_iso.insert(0, caminho_arquivo)

def converter_para_iso():
    """Executa o processo de conversão utilizando o bchunk."""
    arquivo_bin = entry_bin.get()
    arquivo_cue = entry_cue.get()
    arquivo_iso = entry_iso.get()

    if not arquivo_bin or not arquivo_cue or not arquivo_iso:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Comando para o bchunk
    comando = ["bchunk", arquivo_bin, arquivo_cue, arquivo_iso]

    try:
        # Executa o comando em um novo processo
        processo = subprocess.run(comando, check=True, capture_output=True, text=True)
        messagebox.showinfo("Sucesso", f"Arquivo convertido com sucesso para:\n{arquivo_iso}")
    except FileNotFoundError:
        messagebox.showerror("Erro", "O comando 'bchunk' não foi encontrado.\nVerifique se ele está instalado e no PATH do seu sistema.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro na Conversão", f"Ocorreu um erro durante a conversão:\n{e.stderr}")
    except Exception as e:
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro inesperado:\n{str(e)}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("BIN2ISO Gabriel Brilhante")
janela.geometry("500x250")
janela.resizable(False, False)

# Frame principal
frame = tk.Frame(janela, padx=10, pady=10)
frame.pack(expand=True, fill=tk.BOTH)

# Campo para o arquivo .bin
label_bin = tk.Label(frame, text="Arquivo .bin:")
label_bin.grid(row=0, column=0, sticky=tk.W, pady=5)
entry_bin = tk.Entry(frame, width=50)
entry_bin.grid(row=0, column=1, padx=5)
botao_bin = tk.Button(frame, text="Procurar...", command=selecionar_arquivo_bin)
botao_bin.grid(row=0, column=2)

# Campo para o arquivo .cue
label_cue = tk.Label(frame, text="Arquivo .cue:")
label_cue.grid(row=1, column=0, sticky=tk.W, pady=5)
entry_cue = tk.Entry(frame, width=50)
entry_cue.grid(row=1, column=1, padx=5)
botao_cue = tk.Button(frame, text="Procurar...", command=selecionar_arquivo_cue)
botao_cue.grid(row=1, column=2)

# Campo para o arquivo de saída .iso
label_iso = tk.Label(frame, text="Salvar .iso como:")
label_iso.grid(row=2, column=0, sticky=tk.W, pady=5)
entry_iso = tk.Entry(frame, width=50)
entry_iso.grid(row=2, column=1, padx=5)
botao_iso = tk.Button(frame, text="Salvar...", command=selecionar_saida_iso)
botao_iso.grid(row=2, column=2)

# Botão de conversão
botao_converter = tk.Button(frame, text="Converter para ISO", command=converter_para_iso, bg="lightblue", font=("Arial", 12, "bold"))
botao_converter.grid(row=3, columnspan=3, pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()