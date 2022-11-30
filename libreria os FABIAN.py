import os


def llenar(lista):
    for i in range(3):
        dato = str(input("Digite el nombre del usuario: "))
        lista.append(dato)


def crear_usuario(lista):
    for i in range(len(lista)):
        dato = str(lista[i])
        command_line = 'adduser ' + dato
        linea = str(command_line)
        os.system(linea)
        print("El usuario ha sido creado", dato)


if __name__ == "__main__":
    lista_datos = []
    print("Llenar la lista")
    llenar(lista_datos)
    print(lista_datos)
    print("*" * 42)
    crear_usuario(lista_datos)