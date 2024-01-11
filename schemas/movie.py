from typing import Optional
from pydantic import BaseModel, Field #BaseModel se importo para que nuestro esquema herede de el
                                      #Field se importo para hacer validaciones especificas a nuestro esquema

#El modelo ya incluye la validacion de tipo de dato y que siempre sea requerido
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=40) #El parametro no puedo superar una longitud de 15 caracteres y minimo 5
    overview: str = Field(min_length=15, max_length=80) #Default indica que si no se recibe este parametro por defecto sera el default
    year: int = Field(le=2022) #"le" hace que el valor sea menor o igual a el indicado si queremos que solo sea menor pero no igual seria "lt"
    rating: float = Field(ge=1, le=10) #"ge" indica que el valor debe ser mayor o igual a el indicado si queremos que solo sea mayor pero no igual seria "gt"
    category: str = Field(min_length=5, max_length=15)

    class Config: #Con esta clase se evitar tener que poner el default en todos los atributos
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2022,
	            "rating": 9.8,
		        "category": "Acción"
            }
        }