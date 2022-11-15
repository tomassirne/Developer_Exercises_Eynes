import random

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
            if (lista[j]["Edad"] < lista[i]["Edad"]):
                k = j
                while( k < i):
                    swap(lista,k,i)
                    k += 1
                break
             
    print("ID de Persona más joven: ", lista[9]["Id"])
    print("ID de Persona más vieja: ", lista[0]["Id"])
    return lista
    
lista_usuarios = genera_lista()
ordena_lista_decreciente(lista_usuarios)