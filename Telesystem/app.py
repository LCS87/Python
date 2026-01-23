from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '33548084',
    'database': 'BANCO_DE_MEIS'
}

# Função para inserir cliente no banco de dados
def inserir_cliente(nome, email, telefone):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Inserir dados na tabela
    sql = "INSERT INTO Clientes (Nome, Email, Telefone) VALUES (%s, %s, %s)"
    values = (nome, email, telefone)

    try:
        cursor.execute(sql, values)
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

# Rota para a página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o formulário
@app.route('/inserir_cliente', methods=['POST'])
def processar_formulario():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']

    if inserir_cliente(nome, email, telefone):
        status = "Novo registro inserido com sucesso."
    else:
        status = "Erro ao inserir o registro."

    return render_template('index.html', status=status)

if __name__ == '__main__':
    app.run(debug=True)