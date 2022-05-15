# Spawn a Process

import multiprocessing

def foo(i):
    print("Función Foo llamada dentro del Proceso: %s" %i)
    return

if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        Process_jobs.append(p)
        print(Process_jobs[i])
        p.start()
        p.join()
print(Process_jobs[i])
