from fastapi import FastAPI, HTTPException, Query, Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from typing import List, Optional
from models import Movie, MovieCreate, MovieUpdate
import os
from pathlib import Path as FilePath

app = FastAPI(
    title="StreamPlus API",
    description="A movie streaming service API",
    version="2.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database
movies_db: List[Movie] = [
    Movie(
        id=1, 
        title="Inception", 
        year=2010, 
        runtime=148, 
        genre="Action, Adventure, Sci-Fi", 
        producer="Emma Thomas, Christopher Nolan", 
        poster="https://resizing.flixster.com/dSNjD5Et5yjFYT--3tDorUqiH8c=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p10980706_p_v13_ar.jpg"
    ),
    Movie(
        id=2, 
        title="The Dark Knight", 
        year=2008, 
        runtime=152, 
        genre="Action, Crime, Drama", 
        producer="Emma Thomas, Charles Roven, Christopher Nolan", 
        poster="https://resizing.flixster.com/oo28C7Wr0cd5AVysj3KFYBmmNMA=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p12607594_p_v10_at.jpg"
    ),
    Movie(
        id=3, 
        title="Interstellar", 
        year=2014, 
        runtime=169, 
        genre="Action, Adventure, Sci-Fi", 
        producer="Emma Thomas, Christopher Nolan, Lynda Obst", 
        poster="https://resizing.flixster.com/MHH-KUNH3IYgrGaWHNBD3fA3hUw=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p11873485_p_v10_az.jpg"
    ),
    Movie(
        id=4, 
        title="Avengers: Endgame", 
        year=2019, 
        runtime=181, 
        genre="Action, Crime, Drama", 
        producer="Kevin Feige", 
        poster="https://resizing.flixster.com/t_euF7h0tUiid3gGWdVZuRkC9ws=/206x305/v2/https://resizing.flixster.com/qIe0yjJYL2q1Ny0Af1_i6Uen1Xo=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzkwYTAwNjk1LTYzNWUtNDA3Ny05YjQyLTMzNDM0MzlmYTBmOS5qcGc="
    ),
    Movie(
        id=5, 
        title="Black Panther", 
        year=2018, 
        runtime=134, 
        genre="Action, Adventure, Sci-Fi", 
        producer="Kevin Feige", 
        poster="https://resizing.flixster.com/fnRMJMGdQshXrDU88pGgxa4vEsg=/206x305/v2/https://resizing.flixster.com/qtYisqOwDStnpo2P22PRTHC53Uk=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2NmMmQ0ZTRiLWVkOGYtNDllNS05ZjRiLWYyY2RhMjk1YzRjYi5qcGc="
    ),
    Movie(
        id=6, 
        title="Spider-Man: No Way Home", 
        year=2021, 
        runtime=148, 
        genre="Action, Adventure, Fantasy", 
        producer="Kevin Feige, Amy Pascal", 
        poster="https://resizing.flixster.com/n0ZezjP5D67ig876rHKSh5SH1BQ=/206x305/v2/https://resizing.flixster.com/2q0ja5pOYxDRZ2b8LD4ukjr8zqI=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzgwNzVmNjE2LTJiY2QtNDhhMS04ODZlLTlkZDU4YzU5YjEzNi5qcGc="
    ),
    Movie(
        id=7, 
        title="Doctor Strange in the Multiverse of Madness", 
        year=2022, 
        runtime=126, 
        genre="Action, Adventure, Fantasy", 
        producer="Kevin Feige", 
        poster="https://resizing.flixster.com/S9KgcQ-aXTMxJdDcawazTAMi25w=/206x305/v2/https://resizing.flixster.com/CRy_xsBh3o8Dv9iXP99rf1IqzqU=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzg3N2Y1M2ZlLTk4OGYtNDE4YS1iYjRmLWJhMjkyMTRkYWFkYi5qcGc="
    ),
    Movie(
        id=8, 
        title="Thor: Ragnarok", 
        year=2017, 
        runtime=130, 
        genre="Action, Adventure, Comedy", 
        producer="Kevin Feige", 
        poster="https://resizing.flixster.com/ze6SWWpaVcr3LrT75YlnBeDkeic=/206x305/v2/https://resizing.flixster.com/KELM3SNcyzWJQ4yFxSmffjfnDw8=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzdjNDU5MGQ2LTNjMjEtNGRkOC1iMTMzLWJmMDE4ZGU2YzA1ZS5qcGc="
    ),
    Movie(
        id=9, 
        title="The Batman", 
        year=2022, 
        runtime=176, 
        genre="Action, Crime, Drama", 
        producer="Dylan Clark, Matt Reeves", 
        poster="https://resizing.flixster.com/EDwgO6uDRQHzGb-QP5HOHjnnfSQ=/206x305/v2/https://resizing.flixster.com/jv5ZCndtFhgkydyfoqpnEba8OWw=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2VlNzQ2NzNiLTJkZDUtNDhlOS04MGFhLTBjM2IwMzEyNTFkMy5qcGc="
    ),
    Movie(
        id=10, 
        title="Dune: Part One", 
        year=2021, 
        runtime=155, 
        genre="Action, Adventure, Drama", 
        producer="Mary Parent, Denis Villeneuve, Cale Boyter", 
        poster="https://resizing.flixster.com/Ouo5Lpg3kAbilLJkvJNvL5TdbBA=/206x305/v2/https://resizing.flixster.com/8jJemXwPsjGJcVg4xNB2gyh6BwM=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzgwMWYyNjEzLWYzOWEtNGEwMy05ZTcxLWYwOTJmYjAwZmRmOC5qcGc="
    ),
]


@app.get("/", tags=["Root"])
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to StreamPlus API",
        "version": "2.0.0",
        "endpoints": {
            "movies": "/movies",
            "movie_by_id": "/movies/{id}",
            "search": "/movies/search?title={title}",
            "docs": "/docs",
            "videos": "/videos/{filename}"
        }
    }


@app.get("/movies", response_model=List[Movie], tags=["Movies"])
def get_all_movies(
    genre: Optional[str] = Query(None, description="Filter by genre"),
    year: Optional[int] = Query(None, description="Filter by year"),
    limit: Optional[int] = Query(None, ge=1, description="Limit number of results")
):
    """Get all movies with optional filters"""
    filtered_movies = movies_db
    
    if genre:
        filtered_movies = [m for m in filtered_movies if genre.lower() in m.genre.lower()]
    
    if year:
        filtered_movies = [m for m in filtered_movies if m.year == year]
    
    if limit:
        filtered_movies = filtered_movies[:limit]
    
    return filtered_movies


@app.get("/movies/{movie_id}", response_model=Movie, tags=["Movies"])
def get_movie_by_id(movie_id: int = Path(..., ge=1, description="The ID of the movie")):
    """Get a specific movie by ID"""
    movie = next((m for m in movies_db if m.id == movie_id), None)
    
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with ID {movie_id} not found")
    
    return movie


@app.get("/movies/search/", response_model=List[Movie], tags=["Movies"])
def search_movies(
    title: Optional[str] = Query(None, description="Search by title"),
    producer: Optional[str] = Query(None, description="Search by producer")
):
    """Search movies by title or producer"""
    if not title and not producer:
        raise HTTPException(status_code=400, detail="Please provide at least one search parameter")
    
    results = movies_db
    
    if title:
        results = [m for m in results if title.lower() in m.title.lower()]
    
    if producer:
        results = [m for m in results if producer.lower() in m.producer.lower()]
    
    if not results:
        raise HTTPException(status_code=404, detail="No movies found matching your search")
    
    return results


@app.post("/movies", response_model=Movie, status_code=201, tags=["Movies"])
def create_movie(movie: MovieCreate):
    """Create a new movie"""
    # Generate new ID
    new_id = max([m.id for m in movies_db], default=0) + 1
    
    # Check if title already exists
    if any(m.title.lower() == movie.title.lower() for m in movies_db):
        raise HTTPException(status_code=400, detail="Movie with this title already exists")
    
    new_movie = Movie(id=new_id, **movie.dict())
    movies_db.append(new_movie)
    
    return new_movie


@app.put("/movies/{movie_id}", response_model=Movie, tags=["Movies"])
def update_movie(
    movie_update: MovieUpdate,
    movie_id: int = Path(..., ge=1)
):
    """Update an existing movie"""
    movie_index = next((i for i, m in enumerate(movies_db) if m.id == movie_id), None)
    
    if movie_index is None:
        raise HTTPException(status_code=404, detail=f"Movie with ID {movie_id} not found")
    
    existing_movie = movies_db[movie_index]
    update_data = movie_update.dict(exclude_unset=True)
    
    updated_movie = existing_movie.copy(update=update_data)
    movies_db[movie_index] = updated_movie
    
    return updated_movie


@app.delete("/movies/{movie_id}", tags=["Movies"])
def delete_movie(movie_id: int = Path(..., ge=1)):
    """Delete a movie"""
    movie_index = next((i for i, m in enumerate(movies_db) if m.id == movie_id), None)
    
    if movie_index is None:
        raise HTTPException(status_code=404, detail=f"Movie with ID {movie_id} not found")
    
    deleted_movie = movies_db.pop(movie_index)
    
    return {
        "message": "Movie deleted successfully",
        "deleted_movie": deleted_movie
    }
    
    
def iterfile(path: str):
    with open(path, "rb") as file:
        yield from file
    


@app.get("/videos/{filename}", tags=["Videos"])
def get_video(filename: str = Path(..., description="Name of the video file")):
    """Serve a video file from the videos directory"""
    # Specify the base path for videos - use relative path for deployment compatibility
    video_base_path = os.path.join(os.getcwd(), "videos")
    
    # Construct the full video path
    video_path = os.path.join(video_base_path, filename)
    
    # Security check: ensure the path is within the videos directory
    try:
        video_full_path = os.path.abspath(video_path)
        base_full_path = os.path.abspath(video_base_path)
        
        if not video_full_path.startswith(base_full_path):
            raise HTTPException(status_code=403, detail="Access denied")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid file path")
    
    # Check if file exists
    if not os.path.exists(video_path):
        raise HTTPException(status_code=404, detail=f"Video file '{filename}' not found")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(video_path):
        raise HTTPException(status_code=400, detail="Invalid file")
    
    # Stream the video file
    return StreamingResponse(
        iterfile(video_path), 
        media_type="video/mp4",
        headers={
            "Accept-Ranges": "bytes",
            "Content-Disposition": f"inline; filename={filename}"
        }
    )


@app.get("/health", tags=["Health"])
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "total_movies": len(movies_db)
    }
    