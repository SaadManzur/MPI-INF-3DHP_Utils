frame_nums = {
    (1, 1): 6416, (1, 2): 12430,
    (2, 1): 6502, (2, 2): 6081,
    (3, 1): 12488, (3, 2): 12283,
    (4, 1): 6171, (4, 2): 6675,
    (5, 1): 12820, (5, 2): 12312,
    (6, 1): 6188, (6, 2): 6145,
    (7, 1): 6239, (7, 2): 6320,
    (8, 1): 6468, (8, 2): 6054
}

all_joint_names = [
    'spine3', #0
    'spine4', #1
    'spine2', #2
    'spine', #3 
    'pelvis', #4       
    'neck', #5
    'head', #6
    'head_top', #7
    'left_clavicle', #8
    'left_shoulder', #9
    'left_elbow', #10
    'left_wrist', #11
    'left_hand', #12
    'right_clavicle', #13
    'right_shoulder', #14
    'right_elbow', #15
    'right_wrist', #16
    'right_hand', #17
    'left_hip', #18
    'left_knee', #19
    'left_ankle', #20
    'left_foot', #21
    'left_toe', #22   
    'right_hip', #23
    'right_knee', #24
    'right_ankle', #25
    'right_foot', #26
    'right_toe' #27
]

h36m_correspondence = [7, 5, 14, 15, 16, 9, 10, 11, 23, 24, 25, 18, 19, 20, 4, 3, 6]

h36m_correspondence_names = [all_joint_names[i] for i in h36m_correspondence]

h36m_selected_16 = [4, 23, 24, 25, 18, 19, 20, 3, 5, 6, 9, 10, 11, 14, 15, 16]

h36m_16_names = [all_joint_names[i] for i in h36m_selected_16]

h36m_selected_14 = [4, 23, 24, 25, 18, 19, 20, 5, 9, 10, 11, 14, 15, 16]

h36m_14_names = [all_joint_names[i] for i in h36m_selected_14]