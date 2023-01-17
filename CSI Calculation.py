import numpy as np
import matplotlib.pyplot as plot

def csi_calculation(csi_array):
num_frames = 4000
num_users = 2
pilot_reps = 10
bs_antennas = 32
subcarriers = 64

csi_array = np.array(csi)
csi_array = csi_array.astype('complex64')

csi_array_size = (num_frames*num_users*pilot_reps*bs_antennas*subcarriers)

csi_vec = np.reshape(csi_array,(1,csi_array_size))
csi_mag = np.linalg.norm(csi_vec)

plot.hist(csi_mag)
