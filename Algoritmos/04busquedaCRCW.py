''' Programa 04 BUSQUEDA CRCW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''

import threading


def executeThreadMinCRCW1(win, i):
    win[i] = 0


def executeThreadMinCRCW2(L, win, i, j):
    if (L[i] > L[j]):
        win[i] = 1
    else:
        win[j] = 1


def executeThreadMinCRCW3(win, i, indexMin):
    if (win[i] == 0):
        indexMin[0] = i


def minCRCW(L):
    N = len(L) - 1
    win = [None for _ in range(N + 1)]
    win[0] = 0

    list_threads = []

    for i in range(1, N + 1):
        thread = threading.Thread(target=executeThreadMinCRCW1, args=(win, i))
        list_threads.append(thread)
        thread.start()
    for hilo in list_threads:
        hilo.join()
    list_threads = []

    for j in range(1, N + 1):
        i = j - 1
        thread = threading.Thread(target=executeThreadMinCRCW2, args=(L, win, i, j))
        list_threads.append(thread)
        thread.start()
    for hilo in list_threads:
        hilo.join()
    list_threads = []

    indexMin = [0]
    for i in range(1, N + 1):
        thread = threading.Thread(target=executeThreadMinCRCW3, args=(win, i, indexMin))
        list_threads.append(thread)
        thread.start()

    for hilo in list_threads:
        hilo.join()

    print(win)
    print('indice minimo es:', indexMin, 'El número más pequeño es:', L[indexMin[0]])
    return L[indexMin[0]]


L = [95, 10, 6, 5]
print('Arreglo original:', L)

minCRCW(L)