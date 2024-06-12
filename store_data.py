import sqlite3
import pandas as pd


def store_data(csv_file):
    df = pd.read_csv(csv_file)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS titanic_data (
            ID INTEGER,
            Survived INTEGER,
            Pclass INTEGER,
            Age INTEGER,
            Fare REAL,
            Sex_male INTEGER,
            Embarked_Q INTEGER,
            Embarked_S INTEGER,
            Family INTEGER
        )
    """
    )

    df.to_sql("titanic_data", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    store_data("cleaned_titanic_train_df.csv")
