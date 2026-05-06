import sqlite3
import pandas as pd


def load():
    """Load cleaned data into a SQLite database and generate a report"""
    print("Starting load...\n")

    # Read cleaned data
    df = pd.read_csv("output/clean_movies.csv")

    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect("output/movies.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            title TEXT,
            year INTEGER,
            genre TEXT,
            director TEXT,
            imdb_rating REAL,
            box_office INTEGER,
            runtime INTEGER,
            language TEXT,
            processed_at TEXT
        )
    """)

    # Clear old data and reload fresh
    cursor.execute("DELETE FROM movies")

    # Insert rows
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["Title"], row["Year"], row["Genre"], row["Director"],
            row["imdbRating"], row["BoxOffice"], row["Runtime"],
            row["Language"], row["processed_at"]
        ))

    conn.commit()

    # --- Generate Report ---
    print("🏆 Top 5 Movies by Box Office:\n")
    top5 = pd.read_sql(
        "SELECT title, box_office, imdb_rating FROM movies ORDER BY box_office DESC LIMIT 5", conn)
    print(top5.to_string(index=False))

    print("\n⭐ Top 5 Movies by IMDB Rating:\n")
    top_rated = pd.read_sql(
        "SELECT title, imdb_rating, box_office FROM movies ORDER BY imdb_rating DESC LIMIT 5", conn)
    print(top_rated.to_string(index=False))

    # Save report to CSV
    top5.to_csv("output/report.csv", index=False)
    print("\n💾 Report saved to output/report.csv")
    print("\n✅ Load complete! Data stored in output/movies.db")

    conn.close()


if __name__ == "__main__":
    load()
