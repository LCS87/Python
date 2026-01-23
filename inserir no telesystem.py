import mysql.connector
from tkinter import Tk, Label, Entry, Button

def inserir_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()

    # Inserir dados na tabela
    sql = "INSERT INTO Clientes (Nome, Email, Telefone) VALUES (%s, %s, %s)"
    values = (nome, email, telefone)

    try:
        cursor.execute(sql, values)
        conn.commit()
        status_label.config(text="Novo registro inserido com sucesso.")
    except Exception as e:
        status_label.config(text=f"Erro: {e}")
        conn.rollback()

# Configurações do banco de dados
config = {
    'host': 'seu_servidor_mysql',
    'user': 'seu_usuario_mysql',
    'password': 'sua_senha_mysql',
    'database': 'seu_banco_de_dados'
}

# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Criar janela
root = Tk()
root.title("Inserir Cliente")

# Labels e Entry para Nome
label_nome = Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10)
entry_nome = Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

# Labels e Entry para Email
label_email = Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10)
entry_email = Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Labels e Entry para Telefone
label_telefone = Label(root, text="Telefone:")
label_telefone.grid(row=2, column=0, padx=10, pady=10)
entry_telefone = Entry(root)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

# Botão para inserir cliente
btn_inserir = Button(root, text="Inserir Cliente", command=inserir_cliente)
btn_inserir.grid(row=3, column=0, columnspan=2, pady=10)

# Label para exibir status
status_label = Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2, pady=10)

# Função para fechar a conexão e fechar a janela
def fechar_janela():
    cursor.close()
    conn.close()
    root.destroy()

# Botão para fechar janela
btn_fechar = Button(root, text="Fechar", command=fechar_janela)
btn_fechar.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar loop da interface
root.mainloop()