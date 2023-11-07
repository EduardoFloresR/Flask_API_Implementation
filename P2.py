from flask import Flask, jsonify, request
import math
app= Flask(__name__)

@app.route("/nombre", methods=["POST"])
def setName():
    if request.method=='POST':
        dato_posteado = request.get_json()
        dato = dato_posteado['dato']
        return jsonify(str("Almacenado correctamente  " + str(dato)))
    
@app.route("/mensaje", methods=["GET"])
def message():
    dato_posteado = request.get_json()
    nombre = dato_posteado['nombre']
    return jsonify("Saludos cordiales, " +  nombre)

@app.route("/raices", methods=["GET"])
def calcularRaices():
    # Obtén los valores a, b y c de la URL
    coefa = float(request.args.get("a"))
    coefb = float(request.args.get("b"))
    coefc = float(request.args.get("c"))

    # Calcula las raíces de la ecuación cuadrática
    discriminante = coefb**2 - 4*coefa*coefc
    if discriminante > 0:
        x1 = (-coefb + math.sqrt(discriminante)) / (2*coefa)
        x2 = (-coefb - math.sqrt(discriminante)) / (2*coefa)
        return jsonify({"raices": [x1, x2]})
    elif discriminante == 0:
        x = -coefb / (2*coefa)
        return jsonify({"raices": [x]})
    else:
        return jsonify({"raices": []})  # No hay raíces reales

if __name__ == '__main__':
    app.run(debug=True)