import requests
import json

# Your OMDB API key
API_KEY = "4c9561cc"  # 👈 replace this with your actual key

# List of movies to fetch
MOVIES = [
    "The Dark Knight",
    "Inception",
    "Interstellar",
    "The Matrix",
    "Parasite",
    "Forrest Gump",
    "The Godfather",
    "Pulp Fiction",
    "Goodfellas",
    "Whiplash"
]


def fetch_movie(title):
    """Fetch a single movie's data from OMDB API"""
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        print(f"✅ Fetched: {title}")
        return data
    else:
        print(f"❌ Failed: {title}")
        return None


def extract():
    """Fetch all movies and save raw data to a JSON file"""
    print("Starting extraction...\n")
    results = []

    for movie in MOVIES:
        data = fetch_movie(movie)
        if data:
            results.append(data)

    # Save raw data to a JSON file
    with open("output/raw_movies.json", "w") as f:
        json.dump(results, f, indent=4)

    print(
        f"\n✅ Extraction complete! {len(results)} movies saved to output/raw_movies.json")
    return results


if __name__ == "__main__":
    extract()
