from jose import JWTError, jwt
from datetime import datetime, timedelta

#SECRET_KEY
#Algorithm
#Expriation time

SECRET_KEY = "6a7e5fbded91f0f1c4b0b6e0c0c279df3a8d8a6d87955ea3b8f79d47f5b7c1e3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt