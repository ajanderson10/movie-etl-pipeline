-- 1. Average rating by director
SELECT director, ROUND(AVG(imdb_rating), 2) as avg_rating
FROM movies
GROUP BY director
ORDER BY avg_rating DESC;

-- 2. Genre performance (high earning genres only)
SELECT genre, COUNT(*) as movie_count, ROUND(AVG(box_office), 0) as avg_box_office
FROM movies
GROUP BY genre
HAVING avg_box_office > 100000000
ORDER BY avg_box_office DESC;

-- 3. Rating tiers (CASE statement)
SELECT title, imdb_rating,
    CASE
    WHEN imdb_rating >= 9.0 THEN 'Masterpiece'
    WHEN imdb_rating >= 8.7 THEN 'Great'
    ELSE 'Good'
  END as tier
FROM movies
ORDER BY imdb_rating DESC;

-- 4. Box office vs rating rank (window function)
SELECT title, box_office,
    RANK() OVER (ORDER BY box_office DESC) as box_office_rank,
    RANK() OVER (ORDER BY imdb_rating DESC) as rating_rank
FROM movies;