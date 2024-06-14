import sqlite3
import pickle
import numpy as np
from flask import Flask, render_template, request


app = Flask(__name__)

with open("titanic_model.pkl", "rb") as f:
    model = pickle.load(f)


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

    sex_male = 1 if gender == "Male" else 0
    embarked_q = 1 if embarkation == "Queenstown" else 0
    embarked_s = 1 if embarkation == "Southampton" else 0

    features = np.array(
        [[ticket_class, age, fare, sex_male, embarked_q, embarked_s, relatives]]
    )

    data = [ticket_class, age, fare, gender, embarkation, relatives]

    survived = model.predict(features)[0]
    survived_status = "Survived" if survived == 1 else "Not Survived"

    return render_template("predict.html", data=data, survived_status=survived_status)


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
