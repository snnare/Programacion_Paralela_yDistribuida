# IMPLEMENATCION DE ALGORITMO 2 REETIQUETADO
# 29/11/2021

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
LENGTH = 3

# crear vector para dividir
if rank == 0:
    # el tamaño se determina de modo que la longitud de recvbuf divida uniformemente
    # longitud de sendbuf
    x = numpy.linspace(1, size * LENGTH, size * LENGTH)
else:
    # todos los procesos deben tener un valor para x
    x = None

# inicializar como matriz numpy
x_local = numpy.zeros(LENGTH)

# todos los procesos deben tener un valor para x. Pero solo el proceso raíz
# aquí, todos los demás procesos tienen x = Ninguno.
comm.Scatter(x, x_local, root=0)

# debe notar que solo el proceso raíz tiene un valor para x que
# no es "Ninguno"
print("proceso", rank, "x:", x)
print("proceso", rank, "x_local:", x_local)