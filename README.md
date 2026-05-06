# 🎬 Movie ETL Pipeline

A beginner data engineering project that builds an end-to-end ETL 
(Extract, Transform, Load) pipeline using Python.

## 📌 What It Does
- **Extracts** movie data from the [OMDB API](http://www.omdbapi.com/)
- **Transforms** raw data by cleaning fields like Box Office and Runtime
- **Loads** clean data into a SQLite database and generates a CSV report

## 🛠️ Tech Stack
- Python 3.13
- pandas
- requests
- SQLite3

## 📁 Project Structure
movie-etl-pipeline/
├── extract.py        # Fetches data from OMDB API
├── transform.py      # Cleans and structures the data
├── load.py           # Loads into SQLite, generates report
├── pipeline.py       # Runs full ETL in one command
├── requirements.txt  # Dependencies
└── output/
├── raw_movies.json    # Raw API data
├── clean_movies.csv   # Cleaned data
├── report.csv         # Top 5 by box office
└── movies.db          # SQLite database

## 🚀 How To Run

1. Clone the repo
```bash
   git clone https://github.com/ajanderson10/movie-etl-pipeline.git
   cd movie-etl-pipeline
```

2. Create a virtual environment
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies
```bash
   pip3 install -r requirements.txt
```

4. Add your OMDB API key
```bash
   touch .env
   # Add this line to .env:
   # OMDB_API_KEY=your_key_here
```

5. Run the pipeline
```bash
   python3 pipeline.py
```

## 📊 Sample Output

| Title | Box Office | IMDB Rating |
|---|---|---|
| The Dark Knight | $534,987,076 | 9.1 |
| Forrest Gump | $330,455,270 | 8.8 |
| Inception | $292,587,330 | 8.8 |