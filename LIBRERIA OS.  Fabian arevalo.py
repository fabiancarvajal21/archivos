#FABIAN CARVAJAL
import os

def llenar_lista (lista):
    for i in range (3):
        nombre = str (input("Ingrese el nombre que quiere añadir a la lista "))
        lista.append(nombre)
    return (lista) 

def crea_usuario (lista):
    for user in range (len(lista)):
        command_line = str ("adduser "+ lista[user])
        os.system (command_line)
        print (f"Se ha creado el usuario numero {user} {lista[user]}")
        
if __name__=="__main__":
    lista = []
    llenar_lista (lista)
    print (" la lista: ", lista, "ha sido crada ")
    print (lista)
    y = crea_usuario (lista)        