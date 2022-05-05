from fastapi import FastAPI, File, UploadFile


def gerarDataset(file: UploadFile):
    #arquivo = open(file, 'r')
    for linha in file:
        print(linha)
    return 1;
