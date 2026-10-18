from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {'msg': 'Hola Mi Bolsillo'}