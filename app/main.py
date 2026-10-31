from fastapi import FastAPI
from app.routes import auth_route, category_route, user_route


app = FastAPI()

app.include_router(auth_route.router)
app.include_router(user_route.router)
app.include_router(category_route.router)


@app.get('/')
async def root():
    return {'msg': 'Hola Mi Bolsillo'}