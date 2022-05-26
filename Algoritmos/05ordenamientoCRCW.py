''' Programa 05 ORDENAMIENTO CRCW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''

import threading

def thread01(win, i):
    win[i] = 0


def thread02(L, win, i, j):
    if (L[i] > L[j]):
        win[i] = win[i] + 1
    else:
        win[j] = win[j] + 1


def thread03(L, win, i, aux):
    L[win[i]] = aux[i]


def main(L):
    N = len(L) - 1
    win = [None for _ in range(N + 1)]
    win[0] = 0

    list_threads = []

    for i in range(1, N + 1):
        thread = threading.Thread(target=thread01, args=(win, i))
        list_threads.append(thread)
        thread.start()
        thread.join()
    for hilo in list_threads:
        hilo.join()
    list_threads = []

    for it in range(1, N + 1):
        i = 0
        for j in range(it, N + 1):
            thread = threading.Thread(target=thread02, args=(L, win, i, j))
            list_threads.append(thread)
            thread.start()
            i += 1

        for hilo in list_threads:
            a = hilo.join()
    list_threads = []

    aux = L.copy()
    for i in range(0, N + 1):
        thread = threading.Thread(target=thread03, args=(L, win, i, aux))
        list_threads.append(thread)
        thread.start()

    for hilo in list_threads:
        hilo.join()

    print('Arreglo Ordenado', L)
    print('Win', win)

if __name__ == '__main__':
    # Arreglo a ordenar:
    L = [95, 10, 6, 5]
    print('Arreglo Desordenado:', L)
    main(L)