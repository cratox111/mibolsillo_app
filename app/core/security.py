from datetime import timedelta, datetime, timezone
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from jose import jwt

from app.core.config import ALGORITHM, SECRET_KEY


pwd_hash = PasswordHash.recommended()


def hash_password(password):
    password_hashed = pwd_hash.hash(password)

    return password_hashed


def verity_password(password, correct_password):
    if not pwd_hash.verify(password, correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect password"
        )


def create_token(user):
    token = jwt.encode({
            "iss": "auth/login",
            "sub": user.id,
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
        }, key=SECRET_KEY, algorithm=ALGORITHM)

    return token


def get_user_of_token(token):
    token_de = jwt.decode(token=token, key=SECRET_KEY, algorithms=ALGORITHM)

    return token_de["sub"]