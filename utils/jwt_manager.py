from jwt import encode, decode

def create_token(data: dict) -> str:
    #payload es el contenido que voy a convertir al token
    #key es la clave secreta para generar el token
    #algorithm es el algoritmo que se va a utilizar para generar el token
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=["HS256"])
    return data
