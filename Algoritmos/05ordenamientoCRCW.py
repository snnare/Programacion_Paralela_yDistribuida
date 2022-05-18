import math
import  threading

def ordCRCW(L,win, n, L2):
    for i in range(n):
        win[i] = 0
    print("Paso 01: ", win)


    for i in range(n):
        for j in range(n):
            if L[i] > L [j]:
                win[i] = win[i] + 1
    print("Paso 02: ", win)

    for i in  range (n):
        L2 [win[i]] = L[i]
    print("Paso 03: ", L2)


def main():
    L = [95,10,6,15]
    L2 = [0,0,0,0]
    win = [9,9,9,9]
    n = 4
    print("Numeros: ", L)
    t = threading.Thread(ordCRCW(L,win,n,L2))

if __name__ == '__main__':
    main()