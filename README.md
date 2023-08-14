# meuprojeto
 
## Aplicação Flask para iniciantes

Flask para Iniciantes: Um Microframework Web em Python

Flask é um microframework web em Python, perfeito para iniciantes que desejam criar aplicações web de forma simples e rápida. Sua abordagem minimalista e intuitiva permite que você foque no desenvolvimento sem se preocupar com complexidades excessivas.

Com o Flask, você pode criar rotas facilmente, mapeando URLs para funções que manipulam as requisições. Isso torna a construção de páginas web e serviços mais acessível, permitindo que você comece a desenvolver rapidamente.

Além disso, o Flask integra-se de forma perfeita com o mecanismo de templates Jinja2, facilitando a criação de páginas dinâmicas com conteúdo personalizado. Com a documentação detalhada e uma comunidade ativa, você encontrará todo o suporte necessário para se aventurar no desenvolvimento web com Python.

Em suma, Flask é a escolha ideal para iniciantes que desejam dar os primeiros passos na construção de aplicações web em Python, sem abrir mão da flexibilidade e da facilidade de uso. Com Flask, você poderá criar aplicações web incríveis e começar sua jornada no desenvolvimento web de forma empolgante!
## Instalação e Criação de um ambiente virtual

#### 1° passo: Crie uma pasta de projeto:

```bash
mkdir myproject
cd myproject
py -3 -m venv venv
```

#### 2° passo: Faça a ativação da sua maquina virtual:

```bash
venv\Scripts\activate
```

#### 3° passo: Instale o Flask

```bash
pip install Flask
```

#### 4° passo: Para instalar as dependências desse projeto, use o comando abaixo.

```bash
pip install -r requirements.txt
```

#### 5° passo: se Você aprimorou o projeto, contribua adcionando as depêndencias que utilizou com o comando abaixo:

```bash
pip freeze > requirements.txt
```
#### No terminal, na pasta do seu projeto, execute o seguinte comando para criar uma pasta para as migrações:
```bash
flask db init
```
#### Isso criará uma pasta chamada migrations onde as migrações serão armazenadas.
#### Agora você pode usar o seguinte comando para gerar uma migração baseada nos modelos que você definiu:
```bash
flask db migrate -m "Nome da Migração"
```
#### Resumindo:
```bash flask db init ``` - Uma vez para inicializar o sistema de migração.
```bash flask db migrate ```- Sempre que você fizer alterações em seus modelos.
```bash flask db upgrade ``` - Sempre que você quiser aplicar as migrações pendentes ao banco de dados.




## Autores

- [@josemanoelfigueiredo](https://www.github.com/josemanoelfigueiredo)


## Licença

[MIT](https://choosealicense.com/licenses/mit/)

![Logo](https://flask-ptbr.readthedocs.io/en/latest/_images/logo-full.png)
