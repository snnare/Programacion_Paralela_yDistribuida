
''' Programa 03  BUSQUEDA EREW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''

import threading
import math

what = 100

def threadBroadCast(i, j, A):
    A[j] = A[(j - 2 ** (i - 1))]

def threadMinimum(L, i):
    if (L[2 * i - 1] > L[2 * i]):
        L[i] = L[2 * i]
    else:
        L[i] = L[2 * i - 1]

def threadSearching(L, aux, i):
    if (L[i] == aux[i]):
        aux[i] = i
    else:
        aux[i] = what

def BroadCast(A, x, k):
    A[1] = x
    for i in range(1, k + 1):
        for j in range(2 ** (i - 1) + 1, 2 ** i + 1):
            thread = threading.Thread(target=threadBroadCast, args=(i, j, A))
            thread.start()
            thread.join()

def minimal(L, N):
    log = int(math.log(N, 2))
    for j in range(1, log + 1):
        for i in range(1, int(N / 2 ** j) + 1):
            thread = threading.Thread(target=threadMinimum, args=(L, i))
            thread.start()
            thread.join()
    return L[1]

def busquedaErew(L, x, n, k):
    aux = []
    for i in range(0, n + 1):
        aux.append(x)
    aux[0] = what
    BroadCast(aux, x, k)
    for i in range(1, n + 1):
        thread = threading.Thread(target=threadSearching, args=(L, aux, i))
        thread.start()
        thread.join()
    i_min = minimal(aux, n)
    return i_min


def main():
    L = [2, -1, 23, -4, 2, 5, -2, 0, 5, 1, 5, -5, 8, 5, 3, -2]
    n = len(L) - 1
    k = int(math.log(n, 2))
    # Dato a buscar
    x = 2
    print('-' * 63)
    print('\t'*4,'Busqueda EREW')
    print('-' * 63)
    print('Array: ',L)
    print('-' * 63)
    position = busquedaErew(L, x, n, k)
    print('Elemento a buscar:',L[position],'||En la posicion:', position)
    print('-' * 63)


if __name__ == '__main__':
    main()