import threading
import math

A  =[[0 for _ in range(2)]  for _ in range(2)]
B  =[[0 for _ in range(2)]  for _ in range(2)]
C  =[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]
C2 =[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)]

def thread1(i,j,k):
    C[k][i][j]=int(A[i][k])* int(B[k][j])

def thread2(i,j,k,l):
    if(((2*k) % (2 **l))==0):
        C2[2*k][i][j]=int(C[2*k][i][j]+C[2*k-(2**(l))][i][j])

def llenarMatrices(A, B):
    print("Digite los datos de la matriz A")
    i = 0
    while (i < 2):
        j = 0
        while (j < 2):
            print("Digite el valor [", i + 1, ", ", j + 1, " ]: ")
            dato = int(input())
            A[i][j] = dato
            j += 1
        i += 1

    print("Digite los datos de la matriz B")
    i = 0
    while (i < 2):
        j = 0
        while (j < 2):
            print("Digite el valor [", i + 1, ", ", j + 1, " ]: ")
            dato = int(input())
            B[i][j] = dato
            j += 1
        i += 1


def main():
    lg = int(math.log(2, 2))
    llenarMatrices(A,B)
    print ("\nPROCEDIMIENTO DE LAS MULTIPLICACIONES : \n" )
    print ("[ ", A[0][0], "  ", A[0][1], " ]      X      [ ", B[0][0], "  ", B[0][1], " ]")
    print ("[ ", A[1][0], "  ", A[1][1], " ]      X      [ ", B[1][0], "  ", B[1][1], " ]")
    k = 0
    while (k < 2):
        i = 0
        while (i < 2):
            j = 0
            while (j < 2):
                t = threading.Thread(target=thread1(i,j,k))
                t.start()
                t.join()
                j+=1
            i +=1
        k += 1

    print ("\n\nPrimer proceso: ", C)
    l = 0
    while (l < lg):
        i = 0
        while (i < 2):
            j = 0
            while (j < 2):
                k = 0
                while (k < 1):
                    t = threading.Thread(target=thread2(i,j,k,l))
                    t.start()
                    t.join()
                    k = k + 1
                j +=  1
            i += 1
        l +=  1
    print ( "\nRESULTADO de A X B: \n" )
    print ("        [ ", C2[0][0][0], "  ", C2[0][0][1], " ]" )
    print ("        [ ", C2[0][1][0], "  ", C2[0][1][1], " ]")



if __name__ == '__main__':
    main()


