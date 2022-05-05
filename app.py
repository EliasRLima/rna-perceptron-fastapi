from fastapi import FastAPI, File, UploadFile
from Model import AmostraEntenty
from Controller import TreinadorController, ArquivoController

app = FastAPI()


@app.get("/")
async def root():
    return {"PERCEPTRON": "Bem vindo ao algortimo perceptron"}


#@app.post('/treinar')
#def create_perceptron(file: UploadFile):
#    return {"filename": file.filename}

    #dataset = ArquivoController.gerarDataset(file)
    #return TreinadorController.treinar(dataset)


@app.post('/treinar')
async def upload_file_and_read(
        file: UploadFile = File(...),
):
    if file.content_type.startswith("text"):
        text_binary = await readTxt(file) # call `await`
        response = text_binary.decode()
    else:
        # do something
        response = file.filename

    return response


def readTxt(file):
    return file.read()
