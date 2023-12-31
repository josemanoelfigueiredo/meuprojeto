from app import app, db

class ContatoModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    telefone = db.Column(db.String(14), nullable = False)
    conteudo = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return f'<Contato {self.nome}>'
    
class CadastroModels(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    telefone = db.Column(db.String(14), nullable = False)
    senha = db.Column(db.String(40), nullable = False)
    rua = db.Column(db.String(40), nullable = False)
    bairro = db.Column(db.String(40), nullable = False)
    cidade = db.Column(db.String(40), nullable = False)
    uf = db.Column(db.String(40), nullable = False)
    cpf = db.Column(db.String(40), nullable = False, unique = True)

    def __repr__(self):
        return 'Cadastro'