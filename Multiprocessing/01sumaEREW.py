''' Programa 01 SUMA EREW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''
import threading
import math
import multiprocessing

def executeProcess(i, j, A):
    if (((2 * j) % (math.pow(2, i))) == 0):
        A[2 * j] = A[2 * j] + A[((2 * j) - ((int)(math.pow(2, i - 1))))]

def main():
    print("-" * 37)
    print("\t \t  \t Suma EREW")
    print("-" * 37)
    A = [0, 1, 1, 1, 1, 1, 1, 1, 1]
    print(A)
    n = len(A) - 1
    log = int(math.log(n, 2))

    for i in range(1, log + 1):
        for j in range(1, (int)(n / 2) + 1):
            p = multiprocessing.Process(target=executeProcess,args=(i,j,A))
            p.run()
            p.start()
            p.join()
            print(p.is_alive())
        print("-->",A)
    print("-" * 37)
    print("Resultado: ",A[n])
    print("-" * 37)


if __name__ == '__main__':
    main()