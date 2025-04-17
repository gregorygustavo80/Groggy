from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    hora_dormir_str = ""

    if request.method == "POST":
        hora_dormir_str = request.form["hora_dormir"]
        try:
            hora_dormir = datetime.strptime(hora_dormir_str, "%H:%M")
            tempo_adormecer = timedelta(minutes=15)
            ciclo_sono = timedelta(minutes=90)

            for ciclos in range(4, 7):  # 4 a 6 ciclos
                tempo_total = tempo_adormecer + ciclo_sono * ciclos
                hora_acordar = hora_dormir + tempo_total
                resultados.append({
                    "ciclos": ciclos,
                    "horario": hora_acordar.strftime("%H:%M")
                })
        except ValueError:
            resultados = [{"erro": "Formato inválido. Use HH:MM"}]

    return render_template("index.html", resultados=resultados, hora_dormir=hora_dormir_str)

if __name__ == "__main__":
    app.run(debug=True)
