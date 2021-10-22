import flask

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