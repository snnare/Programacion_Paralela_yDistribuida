# IMPLEMENATCION DE ALGORITMO DIFUSION UNO A TODOS
# 29/11/2021

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# inicializar
rand_num = numpy.zeros(1)

if rank == 0:
    rand_num[0] = numpy.random.uniform(0)

comm.Bcast(rand_num, root=0)
print("Proceso", rank, "tiene el numero", rand_num)