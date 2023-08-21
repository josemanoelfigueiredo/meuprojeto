from app import app,db, bcrypt
from flask import render_template, url_for, flash, redirect, request, session
from app.forms import Contato,Cadastro
from app.models import ContatoModels, CadastroModels
from flask_bcrypt import check_password_hash
import time

@app.route('/')
def index():
    return render_template('index.html', title = 'Inicio')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', title = 'Sobre')

@app.route('/projeto')
def projeto():
    return render_template('projetos.html', title = 'Projetos')

@app.route('/teste')
def teste():
    return render_template('teste.html', title = 'Testes')


@app.route('/cadastro',  methods=['GET','POST'])
def cadastro():
    
    cadastro = Cadastro()
    if cadastro.validate_on_submit():
        try:
        
            nome = cadastro.nome.data
            email = cadastro.email.data
            telefone = cadastro.telefone.data
            senha = cadastro.senha.data
            hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
            novo_cadastro = CadastroModels(nome = nome, email = email, telefone = telefone, senha = hash_senha)
            db.session.add(novo_cadastro)
            db.session.commit()
            flash('Seu Cadastro foi realizado com sucesso!')
        except Exception as e:
            flash('Ocorreu um erro ao cadastrar!')
            print(str(e))
    return render_template('cadastro.html', title = 'Cadastre-se', cadastro = cadastro)

@app.route('/login', methods = ['GET' , 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        user = CadastroModels.query.filter_by(email = email).first()
        if user and check_password_hash(user.senha, senha):
            
            session['email'] = user.email
            session['nome'] = user.nome
            session['senha'] = user.senha
            session['telefone'] = user.telefone
            flash('Seja Bem vindo!')
            print( 'Deu certo')
            time.sleep(2)
            
            return redirect(url_for('index'))
        else:
            flash('Senha ou email incorreto')
    return render_template('login.html', title = 'Login')

@app.route('/sair')
def sair():
    session.pop('email', None)
    session.pop('nome', None)
    session.pop('telefone', None)
    session.pop('senha', None)
    return redirect(url_for('login'))

@app.route('/contato', methods=['GET','POST'])
def contato():
    dados_formulario = None
    formulario = Contato()
    if formulario.validate_on_submit():
        flash('Seu forms foi enviado com sucesso!')
        nome = formulario.nome.data
        telefone = formulario.telefone.data
        email = formulario.email.data
        conteudo = formulario.conteudo.data
        novo_contato = ContatoModels(nome = nome, email = email, telefone = telefone, conteudo = conteudo)
        db.session.add(novo_contato)
        db.session.commit()

    return render_template('contato.html', title = 'Contato',formulario = formulario, dados_formulario = dados_formulario)  

@app.route('/editar', methods=['GET','POST'])
def editar():
    if 'email' not in session:
        return redirect(url_for('login'))
    user = CadastroModels.query.filter_by(email = session['email']).first()
    if request.method == 'POST':
        user.nome = request.form.get('nome')
        user.email =request.form.get('email')
        user.telefone = request.form.get('telefone')
        senha = request.form.get('senha')
        user.email = request.form.get('email')
        user.senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        db.session.commit()
        session['email'] = user.email
        session['nome'] = user.nome
        session['senha'] = user.senha
        session['telefone'] = user.telefone
        flash('Seus dados foram alterados com sucesso!')

    return render_template('editar.html', title='Editar', user = user)