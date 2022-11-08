import collections

from Model import AmostraEntenty
from collections import ChainMap


def treinar(dataset):
    algoritmo = collections.ChainMap()
    algoritmo['w1'] = 1
    algoritmo['w2'] = 1
    algoritmo['w3'] = 1
    n = 1
    for x in range(100):
        for amostra in dataset:
            elementos = amostra.split()
            u = (algoritmo['w1'] * float(elementos[0])) + (algoritmo['w2'] * float(elementos[1])) + (
                algoritmo['w3'] * float(elementos[2]))
            y = degrau(u)
            if x == 1:
                print(algoritmo)
                print(y)
                print(int(float(elementos[3])))
            e = 0
            if int(float(elementos[3])) != y:
                e = degrau(int(float(elementos[3]))) - y
                algoritmo['w1'] = algoritmo['w1'] + n * e * float(elementos[0])
                algoritmo['w2'] = algoritmo['w2'] + n * e * float(elementos[1])
                algoritmo['w3'] = algoritmo['w3'] + n * e * float(elementos[2])
            #print(algoritmo)
    return algoritmo

def buscarGrupoOleo(algoritmo, oleo):
    u = (algoritmo['w1'] * float(oleo[0])) + (algoritmo['w2'] * float(oleo[1])) + (
                algoritmo['w3'] * float(oleo[2]))
    y = degrau(u)
    return y

def separarEmDoisGrupos(algoritmo, dataset):
    p1 = []
    p2 = []
    for amostra in dataset:
        elementos = amostra.split()
        u = (algoritmo['w1'] * float(elementos[0])) + (algoritmo['w2'] * float(elementos[1])) + (algoritmo['w3'] * float(elementos[2]))
        y = degrau(u)
        if y == 0:
            p1.append('Elemento: ' + str(float(elementos[0])) + ' ' + str(float(elementos[1])) + ' ' + str(float(elementos[2])))
        else:
            p2.append('Elemento: ' + str(float(elementos[0])) + ' ' + str(float(elementos[1])) + ' ' + str(float(elementos[2])))

    print("Separados.\n")
    print("p1:", p1)
    print("p2:", p2)


def degrau(u):
    if u >= 0:
        return 1
    return 0


def perceptron2String(algoritmo):
    texto = "{ Algoritmo:"
    texto += "  w1 -> " + str(float(algoritmo['w1']))
    texto += "  w2 -> " + str(float(algoritmo['w2']))
    texto += " w3 -> " + str(float(algoritmo['w3']))
    texto += " }"
    return texto

