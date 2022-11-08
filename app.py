from fastapi import FastAPI, File, UploadFile
from Model import AmostraEntenty
from Controller import TreinadorController
from Typing import Union
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return {"PERCEPTRON": "Bem vindo ao algortimo perceptron"}


@app.post('/treinar')
def upload_file_and_read(dataset: AmostraEntenty.Dataset):
    algoritmo = TreinadorController.treinar(dataset.conteudo)
    TreinadorController.separarEmDoisGrupos(algoritmo, dataset.conteudo)
    return {'Resultado treino', TreinadorController.perceptron2String(algoritmo)}

@app.post('/verificar/')
def test_oleo(dataset: AmostraEntenty.Dataset, x1: Union[float, None], x2: Union[float, None], x3: Union[float, None]):
    algoritmo = TreinadorController.treinar(dataset.conteudo)
    oleo = [x1, x2, x3]
    return {'Resultado', TreinadorController.buscarGrupoOleo(algoritmo, oleo)}
