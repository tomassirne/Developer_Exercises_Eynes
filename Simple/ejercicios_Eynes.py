"""
# Aclaración: 
# Para la funcion ordena_lista_decreciente se utilizará una lista aleatoria creada a mano, para poder determinar cuál es la respuesta del test
# Para la funcion genera_lista sólo se testeará que la lista tenga 10 elementos y que estos estén en rango entre 1 y 100 

#TEST1
>>> lista = [{'Id': 1, 'Edad': 93}, {'Id': 2, 'Edad': 1}, {'Id': 3, 'Edad': 66}, {'Id': 4, 'Edad': 43}, {'Id': 5, 'Edad': 36}, {'Id': 6, 'Edad': 72}, {'Id': 7, 'Edad': 77}, {'Id': 8, 'Edad': 39}, {'Id': 9, 'Edad': 53}, {'Id': 10, 'Edad': 61}]
>>> ordena_lista_decreciente(lista)
ID de Persona más joven:  2
ID de Persona más vieja:  1
[{'Id': 1, 'Edad': 93}, {'Id': 7, 'Edad': 77}, {'Id': 6, 'Edad': 72}, {'Id': 3, 'Edad': 66}, {'Id': 10, 'Edad': 61}, {'Id': 9, 'Edad': 53}, {'Id': 4, 'Edad': 43}, {'Id': 8, 'Edad': 39}, {'Id': 5, 'Edad': 36}, {'Id': 2, 'Edad': 1}]

#TEST2
>>> lista = genera_lista()
>>> len(lista) == 10
True

#TEST3
>>> lista = genera_lista()
>>> for i in range(10): 0 < lista[i]["Edad"] and lista[i]["Edad"] <= 100 
True
True
True
True
True
True
True
True
True
True

"""

import random
import doctest

def genera_lista():
    """
    Complejidad de peor caso de Algoritmo: O(1)
    """
    usuario = {"Id":int , "Edad":int}
    lista_usuarios = list()

    for i in range(10):
        usuario["Id"] = i+1
        usuario["Edad"] = random.randint(1,100)
        lista_usuarios.append(usuario.copy())
    return lista_usuarios


def swap(lista: list() , i : int() , j : int()):
    """
    Funcion que intercambia el contenido de dos posiciones de una lista
    Complejidad de peor caso de Algoritmo: O(1)
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    return lista

def ordena_lista_decreciente(lista: list()):
    """
    Método a Utilizar: Insertion Sort 
    Complejidad de peor caso de Algoritmo: O(n^2) 
    siendo n = len(lista)
    """
    for i in range(1,len(lista)):
        for j in range(i):
            if lista[j]["Edad"] < lista[i]["Edad"]:
                k = j
                while( k < i):
                    swap(lista,k,i)
                    k += 1
                break
             
    print("ID de Persona más joven: ", lista[9]["Id"])
    print("ID de Persona más vieja: ", lista[0]["Id"])
    return lista
    

doctest.testmod()