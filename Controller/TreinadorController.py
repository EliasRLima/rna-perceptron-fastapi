import collections

from Model import AmostraEntenty
from collections import ChainMap


def treinar(dataset):
    algoritmo = collections.ChainMap()
    algoritmo['w1'] = 0
    algoritmo['w2'] = 0
    algoritmo['w3'] = 0
    algoritmo['topo'] = 0
    n = 0.1
    for x in range(1):
        for amostra in dataset:
            elementos = amostra.split()
            u = (algoritmo['w1'] * float(elementos[0])) + (algoritmo['w2'] * float(elementos[1])) + (
                algoritmo['w3'] * float(elementos[2]))
            y = degrau(u)
            e = float(elementos[3]) - y
            algoritmo['w1'] = algoritmo['w1'] + n * e * float(elementos[0])
            algoritmo['w2'] = algoritmo['w2'] + n * e * float(elementos[1])
            algoritmo['w3'] = algoritmo['w3'] + n * e * float(elementos[2])
            algoritmo['topo'] = algoritmo['topo'] + n * e * 1
            print(algoritmo)
    return perceptron2String(algoritmo)


def degrau(u):
    if u >= 0:
        return 1
    return 0


def perceptron2String(algoritmo):
    texto = "{ Algoritmo:"
    texto += "  topo -> " + str(float(algoritmo['topo']))
    texto += "  w1 -> " + str(float(algoritmo['w1']))
    texto += "  w2 -> " + str(float(algoritmo['w2']))
    texto += " w3 -> " + str(float(algoritmo['w3']))
    texto += " }"
    return texto

