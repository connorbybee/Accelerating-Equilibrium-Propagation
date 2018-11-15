import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from IPython import display
from matplotlib import offsetbox
import scipy.optimize as optim
import scipy.stats
from  scipy.special import gamma
from scipy.stats import gaussian_kde as kde
import itertools

    
def plotmats(mats,
             flattened=True,
             nrows=4,
             ncols=4,
             log_dir=None,
             name=None,
             cb=True,
             cmap='gray',
             random=True):
    plt.rcParams['image.cmap'] = cmap
    
    if len(mats.shape) > 2:
        flattened = False
        
    if nrows * ncols > mats.shape[0]:
        nrows = 1
        ncols = mats.shape[0]

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * 3, nrows * 2))

    axes = axes.ravel()

    if random:
        idx = np.random.choice(range(mats.shape[0]), size=nrows * ncols, replace=False)
    else:
        idx = np.array(range(nrows * ncols))

    if flattened:
        dx = int(np.sqrt(mats.shape[1]))
        dy = dx
    else:
        dx = mats.shape[1]
        dy = mats.shape[2]

    for i, ax in enumerate(axes):
        ax.grid(False)
        ax.axis('off')
        if cb:
            plt.colorbar(ax.matshow(mats[idx[i]].reshape((dx, dy))), ax=ax)
        else:
            ax.matshow(mats[idx[i]].reshape((dx, dy)))

    if log_dir is not None:
        if name is None:
            name = 'mats.png'
        plt.savefig(os.path.join(log_dir, name + '.png'))
    plt.tight_layout()
        