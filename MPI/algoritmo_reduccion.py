# IMPLEMENATCION DE ALGORITMO REDUCCION
# 29/11/2021

import numpy
from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
rankF = numpy.array(float(rank))
total = numpy.zeros(1)
comm.Reduce(rankF, total, op=MPI.MAX)

print("Process", rank, "has the number", total)