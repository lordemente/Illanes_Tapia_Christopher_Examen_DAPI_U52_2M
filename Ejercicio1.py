def OrdenarNombre(nombre, apellido):
    '''Esta función recibe un ‘nombre y apellido’ y devuelve el ‘apellido, nombre’.
    Parámetros:
        Nombre en el formato ‘Nombre Apellido’
    Salida:
            Nombre en el formato ‘Apellido, Nombre’
'''
    while True:
        if nombre == "terminar" or apellido == "terminar":
            break
        else:
            return f"{apellido} {nombre}"


def ListaNombre(lista):
    '''Lista de nombres: esta lista de nombres guarda una cantidad 
        indeterminada de nombres en este formato:
['Nombre Apellido 1' , 'Nombre Apellido 2' , ... , 'Nombre Apellido N]'''
#     lista= []
#     nombre, apellido= lista.split(" ")

    for i in range(len(lista)):
        lista.append(OrdenarNombre(apellido, nombre))
        return lista













''' Resuelto sin funciones'''

lista = []
while True:
    nombre = input(": ")
    apellido = input(": ")

    if nombre == "terminar" or apellido == "terminar":
        break
    else:
        lista.append(f" {apellido} {nombre}")
        # lista.append(nombre)
        lista.sort()
    print(lista)