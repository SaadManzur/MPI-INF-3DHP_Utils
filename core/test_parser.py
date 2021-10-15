import os
import numpy as np
from glob import glob
from scipy.io import loadmat

from core.constants import frame_nums
from core.constants import h36m_selected_14
from core.constants import h36m_selected_16

def parse_data(base_path, output_path, subjects):

    assert os.path.exists(base_path)

    seqs = ["Seq1", "Seq2"]

    data = {}

    for subj in subjects:

        sub_i = int(subj[-1])

        data[sub_i] = {}

        print("Parsing {s}".format(s=subj))

        annot_file = os.path.join(base_path, subj, "annot_data.mat")

        data_3dc, data_2d = load_annotations(annot_file)

        data[sub_i]['3dc'] = data_3dc
        data[sub_i]['2d'] = data_2d

        break

    # np.savez_compressed(output_path, data=data, idx_14=h36m_selected_14, idx_16=h36m_selected_16)
        

def load_annotations(file):

    print(file)

    assert os.path.exists(file)

    annotations = loadmat(file)

    data_3ds = []
    data_2ds = []

    for i in range(14):
        print(annotations['valid_frame'][i, 0])
        data_2ds.append(annotations['annot2'][i, 0][:frame_count, :].reshape((-1, 28, 2)))
        data_3ds.append(annotations['annot3'][i, 0][:frame_count, :].reshape((-1, 28, 3)))

    return data_3ds, data_2ds
