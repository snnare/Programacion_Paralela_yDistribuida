''' Programa 05 ORDENAMIENTO CRCW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''
import  threading

def ordenamientoCRCW(L,win, n, L2):
    for i in range(n):
        win[i] = 0
    print('-' * 63)
    print("--> Paso 01: ", win)
    print('-' * 63)
    for i in range(n):
        for j in range(n):
            if L[i] > L [j]:
                win[i] = win[i] + 1
    print('-' * 63)
    print("--> Paso 02: ", win)
    print('-' * 63)
    for i in  range (n):
        L2 [win[i]] = L[i]
    print('-' * 63)
    print("--> Paso 03: ", L2)
    print('-' * 63)
    print("Arreglo ordenado: ", L2)
    print('-' * 63)


def main():
    L = [95,10,6,15]
    L2 = [0,0,0,0]
    win = [9,9,9,9]
    n = 4
    print('-' * 63)
    print('\t'* 4 ,' Ordenamiento CRCW')
    print('-' * 63)
    print("Arreglo a ordenar: ", L)
    print('-' * 63)
    thread =  threading.Thread(target=ordenamientoCRCW, args=(L, win , n , L2))
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()