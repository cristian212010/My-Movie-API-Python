from fastapi import APIRouter
from fastapi import Depends, Body, HTTPException, Path, Query, status  #Body se importo para recibir los datos desde la request del Body
from fastapi.responses import JSONResponse #JSONResponse se import para que nuestras api retonen JSON
from typing import List 
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

#Dependencies nos va a permitir que la funcion que esta en su interior se ejecute cuando se llame esta ruta y asi validar el JWT
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=status.HTTP_200_OK, dependencies=[Depends(JWTBearer())]) #response_model nos permite indicarle el tipo de respuesta que va a retornar
def get_movies() -> List[Movie]: #con "->" se le indica el tipo de respuesta que va a retornar la funcion
    db = Session()
    result = MovieService(db).get_movies() #Se llama al servicio para que haga la consulta en la bd y nos retorne el resultado
    #jsonable_encoder es una funcion que se utiliza para convertir un objeto python en un formato que se puede serializar como JSON
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result)) #el status_code=status.HTTP_200_OK nos sirve para indicar el estado de la peticion cuando es exitosa

#Parametros de ruta
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie: #con Path indicamos que el valor debe cumplir esas condiciones
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Parametros Query
@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Movie]: #con Query indicamos que el valor debe cumplir esas condiciones
    db = Session()
    result = MovieService(db).get_movie_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201) #el status_code=200 nos sirve para indicar el estado de la peticion cuando es exitosa
def create_movie(movie: Movie) -> dict:
    db = Session() #Abre la coneccion a la base de datos
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"}) #el status_code=200 nos sirve para indicar el estado de la peticion cuando es exitosa

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie : Movie) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message' : 'No encontrado'})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la pelicula"})
        
@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id : int) -> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message' : 'No encontrado'})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la pelicula"})