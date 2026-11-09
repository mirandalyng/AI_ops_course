from fastapi import FastAPI
from utils import query_duckdb
from data_models import Prompt
from agents import agent

app = FastAPI()


@app.get("/movies")
# Async is not needed in fastAPI (its default) but is market anyways to show api endpoint
async def read_movies(genre: str | None = None):
    if genre:
        sql = "SELECT * FROM movies WHERE genre = ?;"
        params = [genre]
    else:
        sql = "FROM movies;"
        params = None

    movies = query_duckdb(sql, parameters=params)
    # dataframe but will return it / make it into dict
    return movies.to_dict(orient="records")


# post data
@app.post("/movie")
async def create_movie(query: Prompt):
    result = await agent.run(query.prompt)
    movie = result.output
    # Save to database
    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?,?)",
        parameters=[movie.title, movie.year, movie.genre,
                    movie.rating, movie.summary]
    )
    return movie
