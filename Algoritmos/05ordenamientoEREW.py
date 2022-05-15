import os
import math
from threading import Thread


# Definicion de Funciones

def hilo1(Win, i):
    Win[i] = 0


def hilo2(L, Win, i, j):
    if (L[i] > L[j]):
        Win[i] = 1
    else:
        Win[j] = 1


def hilo3(Win, i, ind):
    if (Win[i] == 0):
        ind[0] = i



L = []
x = int(input("INGRESE EL NUMERO DE DATOS A INGRESAR EN EL VECTOR:"))
i = 1
while (i <= x):
    n1 = int(input("INGRESE DATO:"))
    L.append(n1)
    print (L)
    i += 1
Win = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ind = [1000000000000000000000000]
i = 0
n = len(L)

while (i < n):
    if (i >= 0):
        t = Thread(target=hilo1, args=(Win, i))
        t.start()
        t.join()
    i = i + 1
i = 0
j = i + 1

print
"PROCESO 1"
print
"Vector original:----->", L
print
Win

while (j < n):
    if (i < j):
        if (i >= 0):
            t = Thread(target=hilo2, args=(L, Win, i, j))
            t.start()
            t.join()
    i = i + 1
    j = j + 1
i = 0
print
"\nPROCESO 2"
print
Win

while (i < n):
    if (i >= 0):
        t = Thread(target=hilo3, args=(Win, i, ind))
        t.start()
        t.join()
        i = i + 1

print
"\nPROCESO 3"
print
"Señalando el valor minimo con un cero en el vector 0\n", Win

print
" \nEl valor minimo es:  ", L[ind[0]]

os.system('pause')