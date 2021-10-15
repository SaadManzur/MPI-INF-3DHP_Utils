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
        
        for seq in seqs:

            sub_i, seq_i = int(subj[-1]), int(seq[-1])

            data[(sub_i, seq_i)] = {}

            print("Parsing {s}: {se}".format(s=subj, se=seq))

            annot_file = os.path.join(base_path, subj, seq, "annot.mat")
            cam_file = os.path.join(base_path, subj, seq, "camera.calibration")

            data_3dc, data_2d = load_annotations(annot_file, frame_nums[(sub_i, seq_i)])
            cam_data = load_calibration(cam_file)

            data[(sub_i, seq_i)]['3dc'] = data_3dc
            data[(sub_i, seq_i)]['2d'] = data_2d
            data[(sub_i, seq_i)]['cam'] = cam_data

    np.savez_compressed(output_path, data=data, idx_14=h36m_selected_14, idx_16=h36m_selected_16)
        

def load_annotations(file, frame_count):

    assert os.path.exists(file)

    annotations = loadmat(file)

    data_3ds = []
    data_2ds = []

    for i in range(14):
        print(annotations['valid_frame'][i, 0])
        data_2ds.append(annotations['annot2'][i, 0][:frame_count, :].reshape((-1, 28, 2)))
        data_3ds.append(annotations['annot3'][i, 0][:frame_count, :].reshape((-1, 28, 3)))

    return data_3ds, data_2ds

def load_calibration(file):

    assert os.path.exists(file)

    cam_data = []

    with open(file, 'r') as cam_:

        _ = cam_.readline()

        while cam_.readline():
            sensor = np.array(cam_.readline().split()[1:], dtype=np.float16)
            size = np.array(cam_.readline().split()[1:], dtype=np.float16)
            _ = cam_.readline()
            intrinsic = np.array(cam_.readline().split()[1:], dtype=np.float16)
            extrinsic = np.array(cam_.readline().split()[1:], dtype=np.float16)
            radial = cam_.readline().split()[1:]

            cam_data.append({
                "sensor": sensor,
                "size": size,
                "intrinsic": intrinsic.reshape((4, 4)),
                "extrinsic": extrinsic.reshape((4, 4))
            })

        cam_.close()

    return cam_data