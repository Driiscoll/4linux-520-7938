import flask

from calculadora.operacoes import adicao, subtracao, multiplicacao

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "OLÁ MUNDO DO FLASK"

@app.route("/saudacao")
def saudar():
    return 'Olá :)'

@app.route("/saudacao/<nome>")
def sauda_nome(nome):
    return f'olá! {nome}'

@app.route("/somar/<int:x>/<int:y>")
def somar(x, y):
    return f"soma de {x} e {y} é {adicao.somar(x, y)}"