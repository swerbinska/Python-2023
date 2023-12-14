# flask --app hello run

from flask import Flask #importujemy Flaska

app = Flask(__name__) #tworzymy aplikacje webowea


@app.route("/") #sciezka ktora jest obslugiwana
def hello_world():
    return "<p>Hello, World!</p>" #i taka strona sie utwrozy pod konkretnym adresem z tym napisem
