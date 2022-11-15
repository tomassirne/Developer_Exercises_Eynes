import random

def crea_matriz_5x5():
    matriz = list()
    for i in range(5):
        fila = [random.randint(0,1000) for _ in range(5)]
        matriz.append(fila)

matriz = crea_matriz_5x5()

