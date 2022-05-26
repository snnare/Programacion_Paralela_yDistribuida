''' Programa 02 SUMA CREW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''
import multiprocessing
import threading
import math

def  process(i,j,A):
    if(((int)(math.pow(2,i-1)) + 1) <= j):
        A[j] = A[j] + A[j - ((int)(math.pow(2,i-1)))]
        print(A[1:9])

def sumaEREW():
    A = [0, 5, 2, 10, 1, 8, 12, 7, 3]
    n = len(A) - 1
    lg = int(math.log(n, 2))
    j = 1

    print("-" * 37)
    print('Programa 2. SUMA CREW')
    print("-" * 37)
    print(A)
    print('-' * 37)
    for i in range(1, lg + 1):
        while j <= n:
            p = multiprocessing.Process(target=process, args=(i,j,A))
            p.run()
            p.start()
            p.join()
            j+=1

    print("Suma total es: -->",A[n])

def main():
    sumaEREW()


if __name__ == '__main__':
    main()