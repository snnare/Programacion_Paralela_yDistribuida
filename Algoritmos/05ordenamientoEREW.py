# Definicion de Funciones
import threading
import os
import math


# Definicion de Funciones
def hilo3(L2, INI, FIN):
    oddEvenMerge(L2, INI, FIN)
    print ("Procesos: ", L2[1:FIN + 1])


def OddEvenMerge(L2, INI, FIN):
    t3 = threading.Thread(target=oddEvenMerge, args=(L2, INI, FIN))
    t3.start()
    t3.join()


def oddEvenMerge(L2, INI, FIN):
    m = (FIN - INI) + 1
    odd = [0 for _ in range(int ((m / 2) + 1))]
    even = [0 for _ in range(int((m / 2) + 1))]
    if (m == 2):
        if (L2[INI] > L2[FIN]):
            intercambio(L2, INI, FIN)
    else:
        oddEvenSplit(L2, odd, even, INI, m)
        t = threading.Thread(target=ordena, args=(odd, int(m / 2)))
        t.start()
        t.join()
        t2 = threading.Thread(target=ordena, args=(even, int(m / 2)))
        t2.start()
        t2.join()

        i = 1
        while (i <= int(m / 2)):
            t = threading.Thread(target=mezcla, args=(L2, odd, even, i, 1))
            t.start()
            t.join()
            i += 1

        i = 1
        while (i < int(m / 2)):
            t = threading.Thread(target=HiloOddEven, args=(L2, i))
            t.start()
            t.join()
            i = i + 1
        i = 1
        while (i <= int(m / 2)):
            t = threading.Thread(target=HiloOddEvenC, args=(L2, i))
            t.start()
            t.join()
            i = i + 1


def intercambio(L2, INI, FIN):
    aux = L2[INI]
    L2[INI] = L2[FIN]
    L2[FIN] = aux


def oddEvenSplit(L2, odd, even, INI, FIN):
    od = 1
    ev = 1
    x = INI
    while (x <= FIN):
        if ((x % 2) == 0):
            even[ev] = L2[x]
            ev = ev + 1
        else:
            odd[od] = L2[x]
            od = od + 1
        x = x + 1
    print ("Valor  odd: ", odd[1:FIN + 1])
    print ("\nvalor  even: ", even[1:FIN + 1])

def ordena(L2, FIN):
    L3 = L2
    numero = FIN
    OddEvenMerge(L3, 1, numero)


def mezcla(L2, odd, even, j, aux):
    m = L2
    impar = odd
    par = even
    m[(2 * j) - 1] = impar[j]
    m[2 * j] = par[j]


def HiloOddEven(num, i):
    numero = num
    j = i
    a = (2 * j)
    b = (2 * j) + 1
    if (numero[a] > numero[b]):
        intercambio(numero, a, b)


def HiloOddEvenC(num, i):
    numero = num
    j = i
    a = (2 * j) - 1
    b = (2 * j)
    if (numero[a] > numero[b]):
        intercambio(numero, a, b)

def main():
    L = [15, 18, 16, 22, 23, 40, 35, 55, 53, 66, 60, 69, 70, 78, 72, 85]
    n = len(L)
    OddEvenMerge(L, 1, n)
    print(L)


main()



