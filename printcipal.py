# Sustantivos

# file=open("sustantivosIngles.txt","wb")
# print("Name of the file:",file.name)
# print("Closed or not:",file.closed)
# print("Opening mode:",file.mode)
# file.close()

# fo=open("hola.txt","w")
# fo.write("Python is a great language.\nYeah its great!!\n")
# fo.close()

# leyendo un archivo
# fo=open("sustantivosIngles.txt","r+")
# stre=fo.read(10)
# print("Read String is: ",stre)
# fo.close()

# fo=open("sustantivosIngles.txt","r+")
# stre=fo.read(10)
# print("read string is:",stre)
##check current position
# position=fo.tell()
# print("Current file position:",position)
##reposition pointer at the beginning once again
# position=fo.seek(3,0)#parametros(num1=numero de bytes a desplazar desde num2,num2=desde donde se inicia a contar 0=principio 1=posicion actual 2= fin de archivo)
# stre=fo.read(10)
# print("Again read String is:",stre)
# fo.close()

import random

# recargamos las palabras
file = open("sustantivos.txt", "r")
sw = True
palabras = []
while sw:
    cadena = file.readline()
    if cadena != '':
        elemento = cadena.split(',')
        palabras.append(elemento)
    else:
        sw = False

# comienza el juego
vidas = 10
puntaje = 0
print("Traduzca las siguiente palabras al español o al ingles, tiene", vidas, "vidas")
while len(palabras) != 0 and vidas != 0:
    ran = random.randint(0, len(palabras) - 1)
    ran2 = random.randint(0, 1)
    complemento = 1 - ran2
    i = palabras[ran]
    if int(i[2]) < 3:
        respuesta = input(i[ran2] + ' >> ')
        if respuesta == i[complemento]:
            print("Correcto!!")
            i[2] = int(i[2]) + 1
            puntaje += 1
        else:
            vidas -= 1
            print("Incorrecto, la respuesta es:", i[complemento])
            if vidas != 0: print("vidas:", vidas)
    else:
        del palabras[ran]
else:
    if vidas == 0:
        print("Lo siento perdiste")
    else:
        print("Aprobaste la leccion Sustantivos!!")
    print("vidas:", vidas, "/ 10")
    print("Tu puntaje:", puntaje)
    print("Palabras sin completar:", len(palabras), "de un total de 200 palabras")
