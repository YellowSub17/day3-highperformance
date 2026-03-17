

from mpi4py import MPI
import time



if __name__=='__main__':

    mpi_com = MPI.COMM_WORLD

    mpi_rank = mpi_com.Get_rank()
    mpi_size = mpi_com.Get_size()

    time.sleep(5-mpi_rank)

    
    print(f'Hello from rank {mpi_rank}')


