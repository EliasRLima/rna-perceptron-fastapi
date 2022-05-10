from fastapi import FastAPI, File, UploadFile
from Model import AmostraEntenty
from Controller import TreinadorController
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return {"PERCEPTRON": "Bem vindo ao algortimo perceptron"}


@app.post('/treinar')
def upload_file_and_read(dataset: AmostraEntenty.Dataset):
    algoritmo = TreinadorController.treinar(dataset.conteudo)
    TreinadorController.operacao(algoritmo, dataset.conteudo)
    return {'Resultado treino', TreinadorController.perceptron2String(algoritmo)}

