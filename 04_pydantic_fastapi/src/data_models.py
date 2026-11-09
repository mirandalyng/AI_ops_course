from pydantic import BaseModel, Field
from typing import Literal  # Specification


# Pydantic model = BaseModel
# Movie inhereites form it
# LLM reads the descriptions
class Movie(BaseModel):
    title: str = Field(description="Title of movie")
    year: int = Field(description="Year when this movie came out")
    genre: Literal["action", "comedy", "romance",
                   "cartoon", "adventure"] = Field(
                       description=(
                           "main genre, if there is more than 1 choose the one that is most charectaristic for the movie")
    )
    rating: int = Field(
        description=(
            "give a rating between 1 and 5."
            " The higher rating the more populare it is"),
        gt=0, lt=6)

    summary: str = Field(
        description="Short exciting summary of the movie. 2-3 sentences.")


class Prompt(BaseModel):
    prompt: str
