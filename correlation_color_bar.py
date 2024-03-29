import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
from pygments import highlight
from matplotlib.colors import ListedColormap
from biopandas.pdb import PandasPdb
import sys

if __name__ == '__main__':
    # pdb structure
    #input_pdb = sys.argv[1]

    # read the pdb
    #ppdb = PandasPdb()
    #ppdb.read_pdb(input_pdb)

    #correlation_vec = ppdb.df['ATOM']['b_factor'].to_numpy()

    # color palette
    white = np.array([1.0, 1.0, 1.0])
    red = np.array([1.0, 0.0, 0.0])
    # color gradient
    shades = 11
    gradient = np.linspace(white, red, shades)

    # generating color map
    cmap = ListedColormap(gradient)
    # generating color bar
    ax = plt.subplot()
    RGB = np.zeros([100,3])
    higher_bound = 1.0
    # calculate the RGB values and normalize it
    RGB[:, 0] = np.linspace(1.0, higher_bound, 100) 
    RGB[:, 1] = np.linspace(1.0, 0.0, 100) 
    RGB[:, 2] = np.linspace(1.0, 0.0, 100) 
    im = ax.imshow(RGB.reshape((10, 10, 3)),interpolation='nearest', cmap=cmap)
    upper_bound = 0.5
    bounds = np.linspace(0, upper_bound, shades)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)


    # create an axes on the right side of ax. The width of cax will be 5%
    # of ax and the padding between cax and ax will be fixed at 0.05 inch.
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="10%", pad=0.05)
    ax.remove()
    plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax, format="%.2f", ticks=bounds)
    plt.savefig("colorbar_upper_bound_%.2f.png"%upper_bound,dpi=300)

    plt.show()