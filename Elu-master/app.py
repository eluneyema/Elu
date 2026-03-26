from flask import Flask

app = Flask("meu sitezinho")

@app.route("/teste")
def teste():
    return "Rota teste ok"

app.run()