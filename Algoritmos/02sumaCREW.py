import threading
import time
import math

def thread(i,j,arrays):
    arrays[j]=arrays[j]+arrays[j-pow(2,i-1)]
    print (arrays)

def sumaCREW(arrays):
    n = len(arrays)
    logaritmic = int(math.log(n))

    for i in range(1, logaritmic):
        for j in range((pow(2,i-1)+1),n):
            p = threading.Thread(target=thread, args=(i,j,arrays))
            p.start()
            p.join()
            print(i,j)

    print(arrays)

def main():
    # Array de ejemplo:
    # arrays = [0,5,2,10,1,8,12,7,3]
    # Resultado: [0, 5, 7, 17, 18, 26, 38, 45, 48]
    arrays = []
    i = 1
    titulo = "\t02 Suma CREW"
    line = "--" * len(titulo)
    print(titulo + "\n" + line)
    x = int(input("Digite el tamanio del vector: "))

    while (i <= x):
        date = int(input("Digite un numero: "))
        arrays.append(date)
        print(arrays)
        i += 1
    sumaCREW(arrays)


if __name__ == '__main__':
    main()







