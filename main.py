from fastapi import FastAPI
from models import Movie_List

app = FastAPI()

movies = [
    Movie_List(id= 1, title= "Inception", year= 2010, runtime= 148, genre= "Action, Adventure, Sci-Fi", producer= "Emma Thomas, Christopher Nolan", poster= "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjYyNl5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg"),
    Movie_List(id= 2, title= "The Dark Knight", year= 2008, runtime= 152, genre= "Action, Crime, Drama", producer= "Emma Thomas, Charles Roven, Christopher Nolan", poster= "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg"),
    Movie_List(id= 3, title= "Interstellar", year= 2014, runtime= 169, genre= "Action, Adventure, Sci-Fi", producer= "Emma Thomas, Christopher Nolan, Lynda Obst", poster= "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDAtN2MyNi00ZjQ1LWFmZTItODM2ZTk2ZTQxYmJlXkEyXkFqcGc@._V1_SX300.jpg%22"),
    Movie_List(id= 4, title= "Avengers: Endgame", year= 2019, runtime= 181, genre= "Action, Crime, Drama", producer= "Kevin Feige", poster= "https://m.media-amazon.com/images/M/MV5BMTc5MDE2NzY0NV5BMl5BanBnXkFtZTgwNzU1NzY2NzM@._V1_SX300.jpg"),
    Movie_List(id= 5, title= "Black Panther", year= 2018, runtime= 134, genre= "Action, Adventure, Sci-Fi", producer= "Emma Thomas, Christopher Nolan", poster= "https://m.media-amazon.com/images/M/MV5BMTg1MzYzMjQ5NV5BMl5BanBnXkFtZTgwMTc4MjA2NDM@._V1_SX300.jpg"),
    Movie_List(id= 6, title= "Spider-Man: No Way Home", year= 2021, runtime= 148, genre= "Action, Adventure, Fantasy", producer= "Kevin Feige, Amy Pascal", poster= "https://m.media-amazon.com/images/M/MV5BZmMxYzYzYzEtNGE4My00NzA3LWIxZDQtYjhlNDQ0OTc2MjFhXkEyXkFqcGc@._V1_SX300.jpg%22"),
    Movie_List(id= 7, title= "Doctor Strange in the Multiverse of Madness", year= 2022, runtime= 126, genre= "Action, Adventure, Fantasy", producer= "Kevin Feige", poster= "https://m.media-amazon.com/images/M/MV5BMmU5NTJhNGItNGEzNi00ZTM2LThkMjEtZjQ4NDM1OGZlZjQ4XkEyXkFqcGc@._V1_SX300.jpg%22"),
    Movie_List(id= 8, title= "Thor: Ragnarok", year= 2017, runtime= 130, genre= "Action, Adventure, Comedy", producer= "Kevin Feige", poster= "https://m.media-amazon.com/images/M/MV5BMTg1NjYxNjA3OF5BMl5BanBnXkFtZTgwNzYyNDQ3MzI@._V1_SX300.jpg"),
    Movie_List(id= 9, title= "The Batman", year= 2022, runtime= 176, genre= "Action, Crime, Drama", producer= "Dylan Clark, Matt Reeves", poster= "https://m.media-amazon.com/images/M/MV5BN2E2YjMxY2UtNTEyYi00ZmFjLWFlZTQtMjE1YjY5MDA0MTcwXkEyXkFqcGc@._V1_SX300.jpg%22"),
    Movie_List(id= 10, title= "Dune: Part One", year= 2021, runtime= 155, genre= "Action, Adventure, Drama", producer= "Mary Parent, Denis Villeneuve, Cale Boyter", poster= "https://m.media-amazon.com/images/M/MV5BZTE0YWQzN2ItNjMyZS00ZjY2LWFhNjYtZDIyMTBlZTliMWZjXkEyXkFqcGc@._V1_SX300.jpg%22"),
]

@app.get("/")
def greeting():
    return {"message": "Welcome to Streamplus"}

@app.get("/home")
def get_all_movies():
    return movies