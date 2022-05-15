import  math
import threading


def MinCRCW (lista, win, n):
    # WIN
    for i in range(n):
        win[i] = 0
    print("Paso 1: ",win)

    for i in range(n):
        for j in range(n):
            if lista[i] > lista[j]:
                win[i] = 1
    print("Paso 1: ",win)


    for i in range(n):
        if(win[i] == 0):
            indexMin = i
    print("Paso 3: Indice Minimo", indexMin)

    print("\n RESULTADO: ",lista[indexMin])
def main():
    lista = [95,10,6,15]
    win = [9,9,9,9]
    n = 4

    print(lista)
    t = threading.Thread(target=MinCRCW(lista,win,n))
    t.start()
    t.join()
    #Thread.start(MinCRCW(lista,win,n))

main()