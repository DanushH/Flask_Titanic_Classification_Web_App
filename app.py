from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    ticket_class = request.form["ticket_class"]
    age = request.form["age"]
    fare = request.form["fare"]
    gender = request.form["gender"]
    embarkation = request.form["embarkation"]
    relatives = request.form["relatives"]

    data = [ticket_class, age, fare, gender, embarkation, relatives]
    return render_template("predict.html", data=data)


@app.route("/dataset")
def dataset():
    return render_template("dataset.html")
