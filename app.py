#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return app.send_static_file("index.html")

from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def juego():
    return render_template('index.html')

@app.route('/jugar', methods=['POST'])
def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntuacion_jugador = 0
    puntuacion_oponente = 0

    opcion_jugador = request.form['opcion_jugador']

    if opcion_jugador not in opciones:
        return "Opción no válida. Elige entre piedra, papel o tijeras."

    opcion_oponente = random.choice(opciones)

    if opcion_jugador == opcion_oponente:
        resultado = "Empate"
    elif (
        (opcion_jugador == "piedra" and opcion_oponente == "tijeras")
        or (opcion_jugador == "tijeras" and opcion_oponente == "papel")
        or (opcion_jugador == "papel" and opcion_oponente == "piedra")
    ):
        resultado = "¡Ganaste esta ronda!"
        puntuacion_jugador += 1
    else:
        resultado = "Oponente gana esta ronda."
        puntuacion_oponente += 1

    puntuacion = f"Puntuación: Jugador {puntuacion_jugador} - Oponente {puntuacion_oponente}"

    return render_template('resultado.html', opcion_jugador=opcion_jugador, opcion_oponente=opcion_oponente, resultado=resultado, puntuacion=puntuacion)

if __name__ == "__main__":
    app.run(debug=True)
