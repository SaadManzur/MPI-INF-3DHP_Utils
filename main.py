from core.parser import parse_data

data_path_base = "/home/saad/Personal/Research/Dataset/MPI-INF-3DHP/mpi_inf_3dhp/Dataset/Train"
output_path = "out/mpii_compiled.npz"

if __name__ == "__main__":
    
    parse_data(data_path_base, output_path)