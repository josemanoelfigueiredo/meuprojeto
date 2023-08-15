from app import app,db
from flask import render_template, url_for, flash, redirect, request
from app.forms import Contato,Cadastro
from app.models import ContatoModels, CadastroModels

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
        flash('Cadastro concluido!')
        nome = cadastro.nome.data
        email = cadastro.email.data
        telefone = cadastro.telefone.data
        senha = cadastro.senha.data

        novo_cadastro = CadastroModels(nome = nome, email = email, telefone = telefone, senha = senha)
        db.session.add(novo_cadastro)
        db.session.commit()

    return render_template('cadastro.html', title = 'Cadastre-se', cadastro = cadastro)

@app.route('/login')
def login():
    return render_template('login.html', title = 'Login')


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

