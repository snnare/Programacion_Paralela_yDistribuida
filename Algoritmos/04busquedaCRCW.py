''' Programa 04 BUSQUEDA CRCW
Profesor: Elfego Gutierrez Ocampo
Alumno: Jose Angel Romero Rios
'''
import threading

def executeThread01(Win, i):
    Win[i] = 0

def executeThread02(L, Win, i, j):
    if (L[i] > L[j]):
        Win[i] = 1
    else:
        Win[j] = 1

def executeThread03(Win, i, ind):
    if (Win[i] == 0):
        ind[0] = i

def main():
    # Prueba 1
    # L = [95,1,6,15]
    # Prueba 2
    L = [95, 1, 6, 15]
    Win=[1,1,1,1,1,1,1,1,1,1,1,1,1]
    index=[1000000000000000000000000]
    i = 0
    n =len(L)
    print('\tBusqueda CRCW')
    print('Vector original: {}'.format(L))
    while i < n :
        if i >= 0:
            thread = threading.Thread(target=executeThread01, args =(Win,i))
            thread.start()
            thread.join()
        i+=1
    i = 0
    j= i + 1
    print("Win {}".format(Win[:len(L)]))
    while j < n:
        if i < j:
            if i >= 0:
                thread = threading.Thread(target=executeThread02, args=(L, Win, i, j))
                thread.start()
                thread.join()
        i+=1
        j+=1
    i = 0
    print("Win {}".format(Win[:len(L)]))
    while(i<n):
        if(i>=0):
            thread = threading.Thread(target=executeThread03, args = (Win,i,index))
            thread.start()
            thread.join()
            i+=1
    print("Valor minimo: {}".format(L[index[0]]))



if __name__ == '__main__':
    main()