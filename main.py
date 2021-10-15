from core.train_parser import parse_data as parse_train
from core.test_parser import parse_data as parse_test

train_path_base = "/home/saad/Personal/Research/Dataset/MPI-INF-3DHP/mpi_inf_3dhp/Dataset/Train"
test_path_base = "/home/saad/Personal/Research/Dataset/MPI-INF-3DHP/mpi_inf_3dhp/Dataset/Test"
train_output_path = "out/mpii_compiled.npz"
test_output_path = "out/mpii_compiled_test.npz"

TRAIN_SUBJECTS = ["S" + str(i) for i in range(1, 9)]
TEST_SUBJECTS = ["TS" + str(i) for i in range(1, 7)]

if __name__ == "__main__":
    
    train = False
    test = True

    if train:
        parse_train(train_path_base, train_output_path, TRAIN_SUBJECTS)
    
    if test:
        parse_test(test_path_base, test_output_path, TEST_SUBJECTS)