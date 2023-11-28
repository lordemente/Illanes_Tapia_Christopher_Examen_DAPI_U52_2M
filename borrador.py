
def ListaNombre(lista):
    '''Lista de nombres: esta lista de nombres guarda una cantidad 
        indeterminada de nombres en este formato:
['Nombre Apellido 1' , 'Nombre Apellido 2' , ... , 'Nombre Apellido N]'''
#     lista= []
#     nombre, apellido= lista.split(" ")

    for i in range(len(lista)):
        lista.append(OrdenarNombre(apellido, nombre))
        return lista

    return





while True:
        nombre = input("Ingresa tu nombre: ")
        # apellido = input("Ingresa tu nombre: ")
        if nombre == "terminar":
            break
        else:
            a,b = nombre.split(" ")
            print(b,a)
            

lista = []

lista.append(b)
lista.append(a)
print(lista)


# for i in range(len(lista)):
#      a= lista[i][0]

# print(lista)



# lista = []

# for i in range(2):
#     usuario = input(": ")

#     nombre_completo = usuario.split(",")

#     lista.append(nombre_completo)
#     lista.sort()

#     print(lista)
#     print(len(lista))

# nombre = input(":")