''' Programa 06 Ordenamiento EREW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''

import threading
import time


def executeThread01(a, i, odd, even):
    a[2 * i] = odd[i]
    a[2 * i + 1] = even[i]

def executeThread02(a, i, Laux):
    if (a[2 * i + 1] < a[2 * i]):
        a[2 * i + 1], a[2 * i] = interchange(a[2 * i + 1], a[2 * i])

def interchange(b, c):
    aux = b
    b = c
    c = aux
    return b, c

def oddEvenSplit(a):
    n = len(a)
    aux = int(n / 2)
    b = a[0:aux]
    c = a[aux:n]
    return (b, c)


def oddEvenMergePRAM(a):
    n = len(a)
    if n == 2:
        if (a[0] > a[1]):
            a[0], a[1] = interchange(a[0], a[1])
    else:
        odd, even = oddEvenSplit(a)
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
        thread = threading.Thread(target=executeThread01, args=(L, i, even, odd))
        thread.start()
        thread.join()

    lCopy = L.copy()
    for i in range(0, int(n / 2)):
        thread = threading.Thread(target=executeThread02, args=(L, i, lCopy))
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