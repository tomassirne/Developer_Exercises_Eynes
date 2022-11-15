"""
# Aclaración: 
# Para la funcion encontrar_secuencia se utilizará una lista aleatoria creada a mano, para poder determinar cuál es la respuesta del test
# Para la funcion crea_matriz_5x5 sólo se testeará que la matriz sea de 5x5 y que los elementos sean enteros. 

#TEST1
>>> matriz = crea_matriz_5x5()
>>> len(matriz) == 5
True
>>> len(matriz[0]) == 5
True

#TEST2
>>> matriz = crea_matriz_5x5()
>>> for i in range(5): type(matriz[0][i]) 
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>

#TEST3
>>> matriz = crea_matriz_5x5()
>>> for i in range(5): type(matriz[1][i]) 
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>

#TEST4
>>> matriz = crea_matriz_5x5()
>>> for i in range(5): type(matriz[2][i]) 
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>

#TEST5
>>> matriz = crea_matriz_5x5()
>>> for i in range(5): type(matriz[3][i]) 
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>

#TEST5
>>> matriz = crea_matriz_5x5()
>>> for i in range(5): type(matriz[4][i]) 
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>

#TEST7
>>> matriz = [[2,3,4,3,3],[2,4,5,6,3],[8,10,8,10,10],[12,13,14,15,3],[16,17,18,19,7]]
>>> encontrar_secuencia(matriz)
No hay Subsecuencia
False

#TEST8
>>> matriz = [[2,3,4,3,3],[2,4,5,6,3],[8,10,10,10,10],[12,13,14,15,3],[16,17,18,19,7]]
>>> encontrar_secuencia(matriz)
Hay Subsecuencia de 4 números consecutivos
La posicion de la Subsecuencia es de [2, 1] a [2, 4]
True

#TEST9
>>> matriz = [[2,3,4,3,3],[2,4,5,6,3],[8,10,10,10,3],[12,13,14,15,3],[16,17,18,19,7]]
>>> encontrar_secuencia(matriz)
Hay Subsecuencia de 4 números consecutivos
La posicion de la Subsecuencia es de [0, 4] a [3, 4]
True

"""



import random
import doctest

def crea_matriz_5x5():
    matriz = list()
    for i in range(5):
        fila = [random.randint(0,10000) for _ in range(5)]
        matriz.append(fila)
    return matriz

def encontrar_secuencia(matriz : list()):
    if encontrar_secuencia_en_matriz(matriz) is None:
        matriz = transponer(matriz)
        if encontrar_secuencia_en_matriz(matriz) is None:
            print("No hay Subsecuencia")
            return False
        else:
            columna , fila_inicio , fila_fin = encontrar_secuencia_en_matriz(matriz)
            inicio = [fila_inicio,columna]
            fin = [fila_fin,columna]
    else:
        fila , columna_inicio , columna_fin = encontrar_secuencia_en_matriz(matriz)
        inicio = [fila,columna_inicio]
        fin = [fila,columna_fin]
    print("Hay Subsecuencia de 4 números consecutivos")
    print(f"La posicion de la Subsecuencia es de {inicio} a {fin}")
    return True


def encontrar_secuencia_en_matriz(matriz : list()): 
    pos_subsec = None
    
    for i in range(len(matriz)):
        if matriz[i][0] == matriz[i][3] :
            if es_subsec_elementos_iguales(matriz[i],0,3):
                pos_subsec = [i,0,3]
                break
        elif matriz[i][1] == matriz[i][4]:
            if es_subsec_elementos_iguales(matriz[i],1,4):
                pos_subsec = [i,1,4]
                break
    return pos_subsec
    

def es_subsec_elementos_iguales(lista : list(), inicio : int(), fin :int()):
    i = inicio
    hay_subsec = True
    while ( i < fin and hay_subsec):
        if lista[i] != lista[i+1]:
            hay_subsec = False
        i += 1
    return hay_subsec

    
def transponer(matriz):
    matriz_transpuesta = [[None for i in range(len(matriz))] for j in range(len(matriz[0]))]
    
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matriz_transpuesta[i][j] = matriz[j][i]
    return matriz_transpuesta


#matriz = [[2,3,4,3,3],[2,4,5,6,3],[8,10,10,10,3],[12,13,14,15,3],[16,17,18,19,7]]
#print(type(matriz[0][0]))
doctest.testmod()


