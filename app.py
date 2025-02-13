from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Lógica para lidar com o registro do usuário
        pass
    # Renderiza o template da página de registro
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica de autenticação aqui
    return render_template('login.html')
# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Aba de Cursos com Aulas Gravadas
@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

# Aba de Jogos (Flashcards)
@app.route('/jogos')
def jogos():
    return render_template('jogos.html')

# Aba de Materiais de Apoio
@app.route('/materiais')
def materiais():
    return render_template('materiais.html')

# Aba de Lives
@app.route('/lives')
def lives():
    return render_template('lives.html')

if __name__ == '__main__':
    app.run(debug=True)