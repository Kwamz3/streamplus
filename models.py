from pydantic import BaseModel

class Movie_List(BaseModel):
    id: int
    title: str
    year: int
    runtime: int
    genre: str
    producer: str
    poster: str