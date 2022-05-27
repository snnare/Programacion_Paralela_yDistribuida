#
# Alumno:
import multiprocessing
import math


def executeProcess_broadcast(i, j, A):
    A[j-1] = A[j-1 - int(math.pow(2, i-1))]

def broadcast(A, x):
    n = len(A)
    log = int(math.log(n, 2))
    A[0] = x
    for i in range(1, log+1):
        for j in range(int(math.pow(2, i-1))+1, int(math.pow(2, i))+1):
            p = multiprocessing.Process(target=executeProcess_broadcast, args=(i, j, A))
            p.start()
            p.join()


def executeProcess_minimo(i, L, B):
    if L[2*i-2] > L[2*i-1]:
        B[i-1] = L[2*i-1]
    else:
        B[i-1] = L[2*i-2]

def minimo(L):
    n = len(L)
    log = int(math.log(n, 2))
    B = multiprocessing.Array('i', L[:])
    for j in range(1, log+1):
        for i in range(1, int(n / math.pow(2, j)) + 1):
            p = multiprocessing.Process(target=executeProcess_minimo, args=(i, L, B))
            p.start()
            p.join()
        L[:] = B[:]
    return L[0]


def executeProcess_busqueda(i, L, Temp):
    if L[i-1] == Temp[i-1]:
        Temp[i-1] = i
    else:
        Temp[i-1] = 1000000


def busquedaEREW(L, x):
    n = len(L)
    Temp = multiprocessing.Array('i', [0] * n)
    broadcast(Temp, x)
    for i in range(1, n+1):
        p = multiprocessing.Process(target=executeProcess_busqueda, args=(i, L, Temp))
        p.start()
        p.join()
    return minimo(Temp)


if __name__ == '__main__':
    arr = multiprocessing.Array('i', [2, -1, 23, -4, 2, 5, -2, 0, 25, 1, 5, -5, 8, 5, 3, -7])
    numero = 25
    print("\nBUSQUEDA PRAM EREW\n")
    print("Arreglo: \n" + str(arr[:]) + "\n")
    print("Numero a buscar en el arreglo: " + str(numero) + "\n")
    position = busquedaEREW(arr, numero)
    if position == 1000000:
        print("El numero no se encuentra en el arreglo.")
    else:
        print("El numero se encuentra en la " + str(position) + "º posicion.\n")