from flask import Flask, render_template, request, flash
import sqlite3
import re
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Necessário para mensagens flash

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  password_hash TEXT, 
                  strength TEXT, 
                  feedback TEXT)''')
    conn.commit()
    conn.close()

# Função para verificar a força da senha
def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    if criteria_met == 5:
        return "forte", "Parabéns, sua senha é super segura!"
    elif criteria_met >= 3:
        return "moderada", "Tá quase lá! Que tal adicionar mais alguns caracteres especiais ou números?"
    else:
        return "fraca", "Vamos melhorar? Tente usar pelo menos 8 caracteres, com letras maiúsculas, minúsculas, números e algo como ! ou @."

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if password:
            strength, feedback = check_password_strength(password)
            # Gerar hash da senha para armazenamento seguro
            password_hash = generate_password_hash(password, method='pbkdf2:sha256')
            
            # Salvar no banco de dados
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("INSERT INTO passwords (password_hash, strength, feedback) VALUES (?, ?, ?)",
                      (password_hash, strength, feedback))
            conn.commit()
            conn.close()
            
            flash(f"Sua senha é {strength}: {feedback}")
        else:
            flash("Por favor, digite uma senha!")
    
    # Recuperar histórico do banco de dados
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT strength, feedback FROM passwords ORDER BY id DESC LIMIT 5")
    history = c.fetchall()
    conn.close()
    
    return render_template('index.html', history=history)

if __name__ == '__main__':
    init_db()  # Inicializa o banco de dados
    app.run(debug=True)