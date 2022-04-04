from flask import Flask, render_template, request, jsonify
from models.calculadora import Calculadora

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calcula")
def calcular():
    num1 = int(request.args['number1'])
    num2 = int(request.args['number2'])
    oper = request.args['oper']

    calculadora = Calculadora()
    resultado = calculadora.calcular(oper, num1, num2)
    return jsonify(resultado)
    

if __name__ == "__main__":
    app.run(debug=True)
