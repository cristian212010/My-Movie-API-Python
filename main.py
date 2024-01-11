from fastapi import FastAPI  #Body se importo para recibir los datos desde la request del Body
from fastapi.responses import HTMLResponse #HTMLResponse se importo para poder inyectar codigo HTML
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
# Establecer el título y la versión para los metadatos OpenAPI
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler) #Se llama al middleware para que se ejecuta cuando haya un error en la aplicaición
app.include_router(movie_router) #Llamamos a nuestro router en nuestra aplicacion principal
app.include_router(user_router)

Base.metadata.create_all(bind=engine) #Se encarga de crear todas las tablas definidas en la clase Base en la base de datos especificada por el objeto engine

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')
            
