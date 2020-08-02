import MDAnalysis as mda
import MDAnalysis.analysis.pca as pca
import numpy as np
import sys

if __name__ == "__main__":
    # reading structure and trajectory from command line
    topology = sys.argv[1]
    trajectory = sys.argv[2]
    # initialization input
    u = mda.Universe(topology, trajectory)
    # running PCA
    input_pca = pca.PCA(u)
    input_pca.run()
    n_pcs = np.where(input_pca.cumulated_variance > 0.95)[0][0]
    print(n_pcs)
    pca_space = input_pca.transform(u, n_components=n_pcs)
    print(pca_space)
