





from mpi4py import MPI
import time
import numpy as np



if __name__=='__main__':

    mpi_comm = MPI.COMM_WORLD

    mpi_rank = mpi_comm.Get_rank()
    mpi_size = mpi_comm.Get_size()


    
    print(f'Hello from rank {mpi_rank}')

    
    this_rank_arr = np.random.randint( 0, 4, (5,5) ) 
    print(f'Rank {mpi_rank} generated array:\n{this_rank_arr}')

    if mpi_rank == 0:
        total_arr = np.zeros( (5,5), dtype=int )

    else:
        total_arr = None

    mpi_comm.Reduce(
            [this_rank_arr, MPI.INT],
            [total_arr, MPI.INT],
            op=MPI.SUM,
            root=0)

    if mpi_rank == 0:
        print(f'I summed everything into rank {mpi_rank}, and this is the result:\n{total_arr}')







