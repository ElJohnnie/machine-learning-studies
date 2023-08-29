from mpi4py import MPI
comm = MPI.COMM _ WORLD
size = comm.Get _ size()
rank = comm.Get _ rank()
print('size=%d, rank=%d' % (size, rank))