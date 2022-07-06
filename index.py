from flask import Flask, render_template, request
from main import Link, LISTA_CODIGOS

app = Flask(__name__)

def Verificar(codigo):
    for cod in LISTA_CODIGOS:
        if cod.link_curto == codigo:
            return cod
    return None

@app.route("/")
def home():
    base = Link("https://stefanlucas.com/")
    return render_template("index.html",link_base=base)

@app.route("/<page>")
def codigo(page):
    if Verificar(page):
        pagina = Verificar(page)
        return render_template("index.html",redirect=pagina)

@app.route("/criar", methods=["GET"])
def criar():
    link = request.args["link"]
    novo = Link(link)
    return render_template("index.html",Novo=novo)

if __name__ == "__main__":
    app.run(debug=True)