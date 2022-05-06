import collections

from Model import AmostraEntenty
from collections import ChainMap


def treinar(dataset):
    algoritmo = collections.ChainMap()
    algoritmo['w1'] = 0
    algoritmo['w2'] = 0
    algoritmo['w3'] = 0
    algoritmo['topo'] = 1
    for x in range(10):
        for amostra in dataset:
            elementos = amostra.split()
            u = (algoritmo['w1'] * float(elementos[0])) + (algoritmo['w2'] * float(elementos[1])) + (
                algoritmo['w3'] * float(elementos[2]))
            y = degrau(u)
            e = float(elementos[3]) - y
            algoritmo['w1'] = algoritmo['w1'] + 1 * e * float(elementos[0])
            algoritmo['w2'] = algoritmo['w2'] + 1 * e * float(elementos[1])
            algoritmo['w3'] = algoritmo['w3'] + 1 * e * float(elementos[2])
            algoritmo['topo'] = algoritmo['topo'] + 1 * e * 1
            print(algoritmo)
    return {'Treinando': 'Ainda a ser implementado'}


def degrau(u):
    if u >= 0:
        return 1
    return 0
