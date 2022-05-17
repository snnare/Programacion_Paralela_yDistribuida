# MATAR UN PROCESO

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print()
    print("Comenzando la función")
    time.sleep(0.1)
    print("Finalizando la función")


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print("Proceso antes de su ejecución:", p, p.is_alive())
    p.start()
    print("Proceso corriendo:", p, p.is_alive())
    p.terminate()
    print("Proceso terminado:", p, p.is_alive())
    p.join()
    print("Proceso unido:", p, p.is_alive())
    print("Código de Salida del proceso:", p.exitcode)