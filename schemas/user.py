from pydantic import BaseModel #BaseModel se importo para que nuestro esquema herede de el

class User(BaseModel):
    email: str
    password: str