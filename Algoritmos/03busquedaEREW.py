import threading
import math

def hilo1(Temp2, i, j):
    Temp2.insert(j, Temp2[j - (2 ** i - 1)])


def hilo2(K, Temp2, x, n):
    if (x < (n - 1)):
        if (K[x] == Temp2[x]):
            Temp2[x] = x + 1
        else:
            Temp2[x] = 99999


def hilo3(Temp2, n, k):
    if (Temp2[(2 ** (k)) - 1] > Temp2[2 ** k]):
        Temp2[k] = Temp2[2 * k]
    else:
        Temp2[k] = Temp2[(2 ** (k)) - 1]


def Broadcast(Temp, x, n):
    Temp2 = []
    Temp2 = Temp
    Temp2.insert(0, numero)
    Temp2.insert(1, numero)
    i = 1
    while (i <= lg):
        j = (2 ** (i - 1)) + 1
        while (j <= 2 ** i):
            t = threading.Thread(target=hilo1, args=(Temp2, i, j))
            t.start()
            t.join()
            j = j + 1
        i = i + 1


def SearchPram(Temp, lista, n):
    i = 0
    while (i <= n):
        t = threading.Thread(target=hilo2, args=(lista, Temp, i, n))
        t.start()
        t.join()
        i = i + 1


def MinPram(Temp, n):
    i = 1
    while (i <= lg):
        j = 1
        while (j <= int(n / (2 ** j))):
            t = threading.Thread(target=hilo3, args=(Temp, n, i))
            t.start()
            t.join()
            j = j + 1
        i = i + 1


a = []
Temp = []
lista = [2, -1, 23, -4, 2, 5, -2, 5, -2, 0, 5, 1, 5, -5, 8, 5, 3, -2]
n = len(lista)
lg = int(math.log(n, 2))
# ->  Esta parte es estatica solo agregar a la variable  numero el numero a buscar
numero = 2
print
lista
Broadcast(Temp, numero, n)
print
"------------------------------------------------------------------------"
print
"\nVECTOR TEMPORAL: "
print
Temp
SearchPram(Temp, lista, n)
print
"------------------------------------------------------------------------"
print
"\nINDICES:"
print
Temp
MinPram(Temp, n)
h = 1
while (h < len(Temp)):
    if (Temp[h] != 99999):
        pos = Temp[h]
        break
    h = h + 1
print
"------------------------------------------------------------------------"
print
"DONDE", numero, " ESTA EN LA POSICION NUMERO: ", pos