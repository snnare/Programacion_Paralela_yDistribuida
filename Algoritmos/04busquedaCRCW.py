''' Programa 04 BUSQUEDA CRCW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''

import threading

def MinCRCW (lista, win, n):
    print('-' * 63)
    print('\t' * 4, 'Busqueda CRCW')
    print('-' * 63)
    for i in range(n):
        win[i] = 0
    print('-' * 63)
    print("Primer paso 1: \n",win)
    print('-' * 63)
    for i in range(n):
        for j in range(n):
            if lista[i] > lista[j]:
                win[i] = 1
    print('-' * 63)
    print("Segundo paso 2: \n",win)
    print('-' * 63)
    for i in range(n):
        if(win[i] == 0):
            indexMin = i
    print('-' * 63)
    print("El elemento minimo es: ",lista[indexMin]," con IndexMin:", indexMin)
    print('-' * 63)
    print('-' * 63)

def main():
    array = [95,10,6,15]
    win = [9 for _ in range (len(array))]
    '''  En caso de querer digitar los datos del arreglo manualmente
    n = int(input("Ingrese el tamanio del arreglo: "))
    for i in range(n):
        dato = int(input("Digite un numero: "))
        array.append(dato)
        win.append(9)
        print(array)
    print(array)
    '''
    #win.append(9)
    t = threading.Thread(target=MinCRCW(array,win,len(array)))
    t.start()
    t.join()


if __name__ == "__main__":
    main()
