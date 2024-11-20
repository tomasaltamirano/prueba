import random
from package.mostrar_y_recorrer import *
from package.logica_juego import *
# from package.datos import *


# diccionario = {"peces" : ["bagre" , "dorado" , "salmon" , "anchoa"], 
#                "verduras" : ["zanahoria", "espinaca", "brocoli", "papa"],
#                "bebidas": ["agua", "jugo", "te", "cafe"],
#                "carnes": ["pollo", "res", "vaca", "cerdo"]}




# lista = []

# def cargar_lista(lista):
    
#     for categoria in diccionario:

#         lista += diccionario[categoria]
    
#     return lista

# def borrar_elemento_de_lista (lista_vieja,numero):
#     lista_nueva = []

#     for i in range(len(lista_vieja)):

#         if i != numero:
#             lista_nueva += [lista_vieja[i]]

#     return lista_nueva



# def cargar_matriz_principal (lista):

#     matriz_principal = []
    
#     lista = cargar_lista(lista)

#     for j in range(4):

#         fila = []

#         for i in range(4):

#             numero = random.randint(0,len(lista)-1)
#             fila += [lista[numero]]
#             lista = borrar_elemento_de_lista(lista,numero)

#         matriz_principal += [fila]

#     return matriz_principal
    

# def mostrar_matriz(matriz_principal):

#     for i in range (len(matriz_principal)):
        
#         for j in range(len(matriz_principal[0])):

#             print(matriz_principal[i][j],end=" | ")
#         print("")









# def evitar_repeticion_palabras(lista_repetidos: list, eleccion_usuario,diccionario,bandera_2 = False ) -> None:

#     bandera = False
#     for palabra in lista_repetidos:
#         if palabra == eleccion_usuario:
#             eleccion_usuario = valiar_existencia_de_palabra(diccionario,lista_repetidos,bandera_2)
#             bandera = True
#             break
#         if bandera == True:
#             break


#     if bandera != True:
#         lista_repetidos.append(eleccion_usuario)
#         print(lista_repetidos)
#     return eleccion_usuario







# def valiar_existencia_de_palabra( diccionario,lista_repetidos,bandera_2=False):
#     bandera = False

#     while True:
#         if bandera_2 == True:
#             print("esta palabra ya fue ingresada, vuelva a intentar ")
#         eleccion_usuario = input("elija la palabra: ")

#         for categoria in diccionario:

#             for palabra in diccionario[categoria]:

#                 if palabra == eleccion_usuario:
#                     bandera = True
#                     break

#             if bandera == True:
#                 break
        
#         if bandera == False:
#             print("esta palabra no existe, vuelva a intentar ")
        
        

#         if bandera ==  True:
#             bandera_2 = True
#             eleccion_usuario = evitar_repeticion_palabras(lista_repetidos,eleccion_usuario,diccionario,bandera_2)
#             break
#     return eleccion_usuario
    
        


# def definir_categoria(diccionario,lista_repetidos):

#     eleccion_usuario= valiar_existencia_de_palabra(diccionario,lista_repetidos)
    

#     devuleve_categoria = None
#     bandera = False


#     for categoria, palabras in diccionario.items():
        
#         if eleccion_usuario in palabras:

#             print(f"Ingresaste a la categoría: {categoria}")
#             bandera = True
#             devuleve_categoria = diccionario[categoria]
#             break
            
        
        
#     if bandera == False and devuleve_categoria == None:
#         print("La palabra no pertenece a ninguna categoría.")

#     return devuleve_categoria






# def pedir_palabras_restantes(categoria,contador,lista_repetidos,diccionario):
# # y si se equivoca restamos una vida y contador vuelve a 0 repitiendo el proceso
#     for i in range(3):

#         eleccion_usuario = valiar_existencia_de_palabra(diccionario,lista_repetidos)

#         for palabra in categoria:

#                 if palabra == eleccion_usuario:
#                     print("existe")
#                     contador += 1

#     return contador






def jugar_juego (matriz_principal,diccionario) :
    lista_repetidos = []
    for i in range(4):
        print(f"\033[1;36mRonda: {i + 1}\033[0m")
        contador = 0
        
        categoria = definir_categoria(diccionario,lista_repetidos)
        
        if categoria != None:
            contador += 1


        contador = pedir_palabras_restantes(categoria,contador,lista_repetidos,diccionario)


        if contador == 4:
            print("completaste una fila!")
        else:
            print("la palabra ingresada no forma parte de la categoria")
            
    return contador




matriz_principal = cargar_matriz_principal(lista)
mostrar_matriz(matriz_principal)
jugar_juego (matriz_principal,diccionario)



#- crear csv con los datos del diccionario

#- crear funcion para leer y traer los datos del csv

#- crear archivo solo para la lectura y escritura de archivos csv

#- tener las validaciones correspondientes para cada ingreso del usuario a traves de los input

#- tener/crear una funcion que retorne y ordene una nueva matriz con los resultados elegidos (solo si ganaste)

#- reutilizar la funcion mostrar_matriz para mostrar la nueva matriz ordenada

#- minificar las funciones, tratar de que las funciones hagan solo una cosa o un solo ciclo for
#- 
#- documentar las funciones 