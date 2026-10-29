import os

# DB
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://diego2011:123456@localhost:5432/mibolsillo",
)


SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "09d25e096ca2556c818166b7a9563b93f7099f6f08d3e7",
)


ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256",
)