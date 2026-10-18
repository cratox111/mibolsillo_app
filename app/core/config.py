import os

# DB
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://diego2011:123456@localhost:5432/mibolsillo",
)