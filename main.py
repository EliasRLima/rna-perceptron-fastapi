from fastapi import FastAPI
from Model import AmostraEntenty
from Controller import TreinadorController

app = FastAPI()


@app.get("/")
async def root():
    return {"PERCEPTRON": "Bem vindo ao algortimo perceptron"}


@app.post('/treinar')
def create_perceptron(dataset: AmostraEntenty.amostra):
    return TreinadorController.treinar(dataset)
