import sqlite3
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def fetch_data():
    conn = sqlite3.connect("database.db")
    df = pd.read_sql_query("SELECT * FROM titanic_data", conn)
    conn.close()
    return df


def train_model(df):
    X = df.drop(columns=["ID", "Survived"])
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=100, random_state=42)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    with open("titanic_model.pkl", "wb") as f:
        pickle.dump(clf, f)


if __name__ == "__main__":
    df = fetch_data()
    train_model(df)
