
''' Programa 03  BUSQUEDA EREW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''
import multiprocessing
import math

what = 100000

def executeProcessBroadCast(i, j, A):
    A[j] = A[(j - 2 ** (i - 1))]

def executeProcessMinimal(L, i):
    if (L[2 * i - 1] > L[2 * i]):
        L[i] = L[2 * i]
    else:
        L[i] = L[2 * i - 1]

def executeProcessesBusqueda(L, aux, i):
    if (L[i] == aux[i]):
        aux[i] = i
    else:
        aux[i] = what

def BroadCast(A, x, k):
    process = []
    A[1] = x
    for i in range(1, k + 1):
        for j in range(2 ** (i - 1) + 1, 2 ** i + 1):
            p = multiprocessing.Process(target=executeProcessBroadCast,  args=(i,j,A))
            process.append(p)
            p.run()
            p.start()
            p.join()
            # print("Proceso: ", p.is_alive)

def minimal(L, N):
    process = []
    log = int(math.log(N, 2))
    for j in range(1, log + 1):
        for i in range(1, int(N / 2 ** j) + 1):
            p = multiprocessing.Process(target=executeProcessMinimal,  args=(L, i))
            process.append(p)
            p.run()
            p.start()
            p.join()
            # print("Proceso: ", p.is_alive)
    return L[1]

def busquedaErew(L,x,n,k):
    process = []
    aux = []
    for i in range(0, n + 1):
        aux.append(x)
    aux[0] = what

    BroadCast(aux, x, k)

    for i in range(1, n + 1):
        p = multiprocessing.Process(target=executeProcessesBusqueda,  args=(L, aux, i))
        process.append(p)
        p.run()
        p.start()
        p.join()
        # print("Proceso: ", p.is_alive)

    i_min = minimal(aux, n)
    return i_min


def main():
    L = [2, -1, 23, -4, 2, 5, -2, 0, 5, 1, 5, -5, 8, 5, 3, -2]
    n = len(L) - 1
    lg = int(math.log(n, 2))

    print('-' * 63)
    print("Arreglo: \n", L)
    print('-' * 63)
    x = int(input("Dato a buscar: "))

    i = busquedaErew(L,x,n,lg)
    print('\nEl número ', x, ' se encuentra en la posición: ', i)

if __name__ == '__main__':
    main()