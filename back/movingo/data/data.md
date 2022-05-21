```bash
$ sqlite3 db.sqlite3
> .mode csv
.import --skip 1 data/movie.csv movies_movie
.import --skip 1 data/genre.csv movies_genre
.import --skip 1 data/movie_genre.csv movies_movie_genres
```

