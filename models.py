from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    """Pydantic model for Movie data validation"""
    id: int = Field(..., description="Unique identifier for the movie")
    title: str = Field(..., min_length=1, description="Movie title")
    year: int = Field(..., ge=1888, le=2100, description="Release year")
    runtime: int = Field(..., gt=0, description="Runtime in minutes")
    genre: str = Field(..., description="Movie genres")
    producer: str = Field(..., description="Movie producers")
    poster: str = Field(..., description="URL to movie poster")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Inception",
                "year": 2010,
                "runtime": 148,
                "genre": "Action, Adventure, Sci-Fi",
                "producer": "Emma Thomas, Christopher Nolan",
                "poster": "https://resizing.flixster.com/dSNjD5Et5yjFYT--3tDorUqiH8c=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p10980706_p_v13_ar.jpg"
            }
        }


class MovieCreate(BaseModel):
    """Model for creating a new movie (without ID)"""
    title: str = Field(..., min_length=1)
    year: int = Field(..., ge=1888, le=2100)
    runtime: int = Field(..., gt=0)
    genre: str
    producer: str
    poster: str


class MovieUpdate(BaseModel):
    """Model for updating a movie (all fields optional)"""
    title: Optional[str] = Field(None, min_length=1)
    year: Optional[int] = Field(None, ge=1888, le=2100)
    runtime: Optional[int] = Field(None, gt=0)
    genre: Optional[str] = None
    producer: Optional[str] = None
    poster: Optional[str] = None