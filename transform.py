import pandas as pd
import json


def transform():
    """Clean and transform raw movie data"""
    print("Starting transformation...\n")

    # Load raw data
    with open("output/raw_movies.json", "r") as f:
        raw_data = json.load(f)

    df = pd.DataFrame(raw_data)

    # Keep only the columns we care about
    columns = ["Title", "Year", "Genre", "Director",
               "imdbRating", "BoxOffice", "Runtime", "Language"]
    df = df[columns]

    # Clean BoxOffice — remove $ and commas, convert to integer
    df["BoxOffice"] = df["BoxOffice"].str.replace("[$,]", "", regex=True)
    df["BoxOffice"] = pd.to_numeric(df["BoxOffice"], errors="coerce")

    # Clean Runtime — remove " min", convert to integer
    df["Runtime"] = df["Runtime"].str.replace(" min", "", regex=False)
    df["Runtime"] = pd.to_numeric(df["Runtime"], errors="coerce")

    # Clean imdbRating — convert to float
    df["imdbRating"] = pd.to_numeric(df["imdbRating"], errors="coerce")

    # Clean Year — convert to integer
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

    # Add a processed timestamp
    df["processed_at"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")

    # Drop any rows with missing critical data
    df = df.dropna(subset=["imdbRating", "BoxOffice"])

    print(df[["Title", "imdbRating", "BoxOffice"]].to_string(index=False))
    print(f"\n✅ Transformation complete! {len(df)} movies cleaned.")

    # Save cleaned data
    df.to_csv("output/clean_movies.csv", index=False)
    print("💾 Saved to output/clean_movies.csv")

    return df


if __name__ == "__main__":
    transform()
