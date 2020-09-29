DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    title VARCHAR(255),
    genre VARCHAR(255),
    artist_id INT REFERENCES artist(id)
)
