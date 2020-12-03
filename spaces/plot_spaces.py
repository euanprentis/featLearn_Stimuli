import numpy as np
import matplotlib.pyplot as plt
from os import listdir

load_dirs = ['corr_D1', 'corr_D1D2', 'corr_D2', 'uncorr_unclust', 'uncorr_clust']

for load_dir in load_dirs:

    files = listdir(load_dir)
    files = [f for f in files if '.csv' in f]

    fig, axs = plt.subplots(len(files))
    y = np.ones(24)
    for i in range(len(files)):
        data = np.genfromtxt(load_dir+'/'+files[i], delimiter=',')

        axs[i].plot(data[:, 0], y, '|')
        axs[i].axis('off')


plt.show()
