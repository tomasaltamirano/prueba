# from datos import *
# from mostrar_y_recorrer import * 


def evitar_repeticion_palabras(lista_repetidos: list, eleccion_usuario,diccionario,bandera_2 = False ) -> None:

    bandera = False
    for palabra in lista_repetidos:
        if palabra == eleccion_usuario:
            eleccion_usuario = valiar_existencia_de_palabra(diccionario,lista_repetidos,bandera_2)
            bandera = True
            break
        if bandera == True:
            break


    if bandera != True:
        lista_repetidos.append(eleccion_usuario)
        print(lista_repetidos)
    return eleccion_usuario







def valiar_existencia_de_palabra( diccionario,lista_repetidos,bandera_2=False):
    bandera = False

    while True:
        if bandera_2 == True:
            print("esta palabra ya fue ingresada, vuelva a intentar ")
        eleccion_usuario = input("elija la palabra: ")

        for categoria in diccionario:

            for palabra in diccionario[categoria]:

                if palabra == eleccion_usuario:
                    bandera = True
                    break

            if bandera == True:
                break
        
        if bandera == False:
            print("esta palabra no existe, vuelva a intentar ")
        
        

        if bandera ==  True:
            bandera_2 = True
            eleccion_usuario = evitar_repeticion_palabras(lista_repetidos,eleccion_usuario,diccionario,bandera_2)
            break
    return eleccion_usuario
    
        


def definir_categoria(diccionario,lista_repetidos):

    eleccion_usuario= valiar_existencia_de_palabra(diccionario,lista_repetidos)
    

    devuleve_categoria = None
    bandera = False


    for categoria, palabras in diccionario.items():
        
        if eleccion_usuario in palabras:

            print(f"Ingresaste a la categoría: {categoria}")
            bandera = True
            devuleve_categoria = diccionario[categoria]
            break
            
        
        
    if bandera == False and devuleve_categoria == None:
        print("La palabra no pertenece a ninguna categoría.")

    return devuleve_categoria






def pedir_palabras_restantes(categoria,contador,lista_repetidos,diccionario):
# y si se equivoca restamos una vida y contador vuelve a 0 repitiendo el proceso
    for i in range(3):

        eleccion_usuario = valiar_existencia_de_palabra(diccionario,lista_repetidos)

        for palabra in categoria:

                if palabra == eleccion_usuario:
                    print("existe")
                    contador += 1

    return contador