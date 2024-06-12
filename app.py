import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    # SAMPLE OUTPUT
    ticket_class = request.form["ticket_class"]
    age = request.form["age"]
    fare = request.form["fare"]
    gender = request.form["gender"]
    embarkation = request.form["embarkation"]
    relatives = request.form["relatives"]

    data = [ticket_class, age, fare, gender, embarkation, relatives]

    # MODIFY TO ADD MODEL PREDICTION LOGIC HERE

    return render_template("predict.html", data=data)


@app.route("/dataset")
def dataset():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM titanic_data")
    rows = cursor.fetchall()
    conn.close()

    updated_rows = []
    for row in rows:
        row = list(row)
        row[0] = row[0] + 1

        row[1] = "Yes" if row[1] == 1 else "No"

        row[5] = "Male" if row[5] == 1 else "Female"

        if row[6] == 1:
            row[6] = "Queenstown"
        elif row[7] == 1:
            row[6] = "Southampton"
        else:
            row[6] = "Cherbourg"

        updated_rows.append(row)

    return render_template("dataset.html", rows=updated_rows)
