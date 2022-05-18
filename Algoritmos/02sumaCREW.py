''' Programa 02 SUMA CREW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''

import threading
import math

def  thread01(i,j,A,B):
    B[j]=A[j]+A[(j-2**((i)-1))]


def sumaEREW():
    A = [0, 5, 2, 10, 1, 8, 12, 7, 3]
    B = A.copy()
    n = len(A) - 1
    lg = int(math.log(n, 2))
    print('Programa 2. SUMA CREW')
    print('-' * 33)
    print(A)
    print('-' * 33)
    for i in range(1, lg + 1):
        for j in range((2 ** (i - 1) + 1), n + 1):
            h = threading.Thread(target=thread01, args=(i, j, A, B))
            h.start()
            h.join()
        A = B.copy()
        print(A)

def main():
    sumaEREW()


if __name__ == '__main__':
    main()