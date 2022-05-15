'''
import math
import threading


def proceso (i,j, lista):
    if(((2*j)%(math.pow(2,i)) ) == 0):
        lista[2*j] = lista[2*j] + lista [((2*j)-(int(math.pow(2,i-1))))]

def main():
    lista =  [0,5,2,10,1,8,12,7,3]
    n =  8
    log = int(math.log(8,2))

    print(lista)

    for i in range(1, log + 1):
        print(i, ". Paso")

        for j in range(1, int((n/2)+1)):
            t = threading.Thread(target=proceso(i,j,lista))
            #print(t = threading.current_thread())
            t.start()
            t.join()
            print(lista[1:9])
    print(lista[1:9])
    print("Resultado: ", lista[8])

main()
'''
import  threading
import  math

def hilo03(L2, INI,FIN):
    oddEvenMerge(L2,INI,FIN)
    print("Procesos ",L2[1:FIN+1])


def OddEvenMerge(L2,INI,FIN):
    t3=threading.Thread(target=oddEvenMerge,args=(L2,INI,FIN))
    t3.start()
    t3.join()


def oddEvenMerge(L2, INI, FIN):
    m = (FIN - INI) + 1
    odd = [0 for _ in range((m / 2) + 1)]
    even = [0 for _ in range((m / 2) + 1)]
    if (m == 2):
        if (L2[INI] > L2[FIN]):
            intercambio(L2, INI, FIN)
    else:
        oddEvenSplit(L2, odd, even, INI, m)
        t = threading.Thread(target=ordena, args=(odd, (m / 2)))
        t.start()
        t.join()
        t2 = threading.Thread(target=ordena, args=(even, (m / 2)))
        t2.start()
        t2.join()

        i = 1
        while (i <= (m / 2)):
            t = threading.Thread(target=mezcla, args=(L2, odd, even, i, 1))
            t.start()
            t.join()
            i = i + 1

        i = 1
        while (i < int(m / 2)):
            t = threading.Thread(target=HiloOddEven, args=(L2, i))
            t.start()
            t.join()
            i = i + 1
        i = 1
        while (i <= int(m / 2)):
            t = threading.Thread(target=HiloOddEvenC, args=(L2, i))
            t.start()
            t.join()
            i = i + 1


def intercambio(L2, INI, FIN):
    aux = L2[INI]
    L2[INI] = L2[FIN]
    L2[FIN] = aux


def oddEvenSplit(L2, odd, even, INI, FIN):
    od = 1
    ev = 1
    x = INI
    while (x <= FIN):
        if ((x % 2) == 0):
            even[ev] = L2[x]
            ev = ev + 1
        else:
            odd[od] = L2[x]
            od = od + 1
        x = x + 1
    print ("valor  odd: ", odd[1:FIN + 1] )
    print ("\nvalor  even: ", even[1:FIN + 1] )


def ordena(L2, FIN):
    L3 = L2
    numero = FIN
    OddEvenMerge(L3, 1, numero)


def mezcla(L2, odd, even, j, aux):
    m = L2
    impar = odd
    par = even
    m[(2 * j) - 1] = impar[j]
    m[2 * j] = par[j]


def HiloOddEven(num, i):
    numero = num
    j = i
    a = (2 * j)
    b = (2 * j) + 1
    if (numero[a] > numero[b]):
        intercambio(numero, a, b)


def HiloOddEvenC(num, i):
    numero = num
    j = i
    a = (2 * j) - 1
    b = (2 * j)
    if (numero[a] > numero[b]):
        intercambio(numero, a, b)

print ("\n INGRESE EL NUMERO DE VALORES A INGRESAR : " )
print("(NOTA: SOLO PUEDE INGRESAR UN NUMERO PAR DE VALORES A ORDENAR)")
n = int(input())

while((n%2)!=0):
    print ("EL NUMERO DE VALORES NO ES PAR")
    print ("INGRESE UN NUMERO DE VALORES QUE SEA PAR: ")
    n=int(input())
L=[0 for _ in range(n+1)]

i = 0
while (i < n):
    print ("\nINGRESE VALOR NUMERO ", i + 1 )
    x = int(input())
    L[i + 1] = x
    i +=1

print ("VALORES INICIALES: ", L[1:n + 1])
OddEvenMerge(L, 1, n)

print ("\nVALORES ORDENADOS: ", L[1:n + 1])

