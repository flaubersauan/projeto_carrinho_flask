from flask import *

app = Flask(__name__)

app.config['SECRET_KEY'] = 'VCNAOVAIMEDESCOBRIR'

usuarios = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('cadastro.html')
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    if nome not in usuarios:
        usuarios[nome] = senha
        return redirect(url_for('login'))
    return 'Usuário já cadastrado. <a href="/login">Login</a>'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    print(usuarios)
    print(f"Tentando login com nome={nome}, senha={senha}")
    if nome in usuarios and usuarios[nome] == senha:
        session['user'] = nome
        return redirect(url_for('dash'))
    return 'Login inválido. <a href="/login">Tente novamente</a>'


@app.route('/dashboard')
def dash():
    if 'user' in session:
        nome = session['user']
        return render_template('dash.html', nome=nome)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    nome = session.pop('user', None)
    return render_template('logout.html', nome=nome)

@app.route('/produtos')
def produtos():
    ...

@app.route('/carrinho')
def carrinho():
    ... 