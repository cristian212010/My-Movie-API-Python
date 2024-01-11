import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_file_name = "../database.sqlite" #nombre de la base de datos
base_dir = os.path.dirname(os.path.realpath(__file__)) #será nuestra url del archivo de sqlite

database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}" #une un string adicional con lo que declaramos de la ruta y nombre del archivo

engine = create_engine(database_url, echo=True) #crea una instancia del resultado de lo que devuelve la funcion create_engine()

Session = sessionmaker(bind=engine) #guarda la session creada a partir del engine

Base = declarative_base()

#¿Ques es un ORM?
#Es una libreria que nos permite la manipulacion de tablas en una base de datos como su feuran objetos de nuestra aplicacion