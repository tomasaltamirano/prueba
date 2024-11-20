from datos import *
# print(diccionario)
lista = []

def cargar_lista(lista):
    
    for categoria in diccionario:

        lista += diccionario[categoria]
    
    return lista

def borrar_elemento_de_lista (lista_vieja,numero):
    lista_nueva = []

    for i in range(len(lista_vieja)):

        if i != numero:
            lista_nueva += [lista_vieja[i]]

    return lista_nueva



def cargar_matriz_principal (lista):

    matriz_principal = []
    
    lista = cargar_lista(lista)

    for j in range(4):

        fila = []

        for i in range(4):

            numero = random.randint(0,len(lista)-1)
            fila += [lista[numero]]
            lista = borrar_elemento_de_lista(lista,numero)

        matriz_principal += [fila]

    return matriz_principal
    

def mostrar_matriz(matriz_principal):

    for i in range (len(matriz_principal)):
        
        for j in range(len(matriz_principal[0])):

            print(matriz_principal[i][j],end=" | ")
        print("")
        


