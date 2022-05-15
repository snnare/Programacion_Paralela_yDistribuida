import threading

def MinCRCW (lista, win, n):

    print("\n \t Busqueda CRCW ")
    for i in range(n):
        win[i] = 0
    print("Primer paso 1: ",win)

    for i in range(n):
        for j in range(n):
            if lista[i] > lista[j]:
                win[i] = 1
    print("Segundo paso 2: ",win)

    for i in range(n):
        if(win[i] == 0):
            indexMin = i
    print("Tercer paso 3: Indice Minimo", indexMin)

    print("\n El minimo es: : ",lista[indexMin])

def main():
    lista = []
    win = []
    # win = [9, 9, 9, 9]
    n = int(input("Ingrese el tamanio del arreglo: "))
    for i in range(n):
        dato = int(input("Digite un numero: "))
        lista.append(dato)
        win.append(9)
        print(lista)
    print(lista)
    t = threading.Thread(target=MinCRCW(lista,win,n))
    t.start()
    t.join()


if __name__ == "__main__":
    main()
