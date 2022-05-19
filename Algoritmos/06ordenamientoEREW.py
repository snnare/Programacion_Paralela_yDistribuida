''' Programa 06 Ordenamiento EREW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''

import threading
import time

def thread01(L, i, odd, even):
    L[2 * i] = odd[i]
    L[2 * i + 1] = even[i]

def thread02(L, i, Laux):
    if (L[2 * i + 1] < L[2 * i]):
        L[2 * i + 1], L[2 * i] = interchange(L[2 * i + 1], L[2 * i])

def interchange(L1, L2):
    aux = L1
    L1 = L2
    L2 = aux
    return L1, L2

def oddEvenSplit(L):
    n = len(L)
    aux = int(n / 2)
    L1 = L[0:aux]
    L2 = L[aux:n]
    return (L1, L2)

def oddEvenMergePRAM(L):
    n = len(L)
    if n == 2:
        if (L[0] > L[1]):
            L[0], L[1] = interchange(L[0], L[1])
    else:
        odd, even = oddEvenSplit(L)
        oddEvenMergePRAM(odd)
        oddEvenMergePRAM(even)
        return (odd, even)

def main():
    L = [16, 22, 35, 40, 55, 66, 70, 85, 15, 18, 23, 53, 60, 69, 72, 78]
    print('-' * 63)
    print('\t'*4,'Ordenamiento EREW')
    print('-' * 63)
    print('Arreglo: ', L)
    print('-' * 63)
    oddEvenMergePRAM(L)
    odd, even = oddEvenMergePRAM(L)
    n = len(L)

    for i in range(0, int(n / 2)):
        thread = threading.Thread(target=thread01, args=(L, i, even, odd))
        thread.start()
        thread.join()

    lCopy = L.copy()
    for i in range(0, int(n / 2)):
        thread = threading.Thread(target=thread02, args=(L, i, lCopy))
        thread.start()
        thread.join()
    print('-' * 63)
    print('Ordenando ...')
    print('-' * 63)
    print(oddEvenMergePRAM(even))
    print(oddEvenMergePRAM(odd))
    print(oddEvenSplit(L))
    print(oddEvenMergePRAM(L))
    print('-' * 63)
    print('Arreglo Ordenado: \n', L)
    print('-' * 63)
    time.sleep(2)


if __name__ == '__main__':
    main()