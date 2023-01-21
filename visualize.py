import numpy as np
import matplotlib.pyplot as plt
from costmap import CostMap


def plot_costmap(cm: CostMap):
    """
    Plot costmap as an image in matplotlib, assumes cell width is 1.
    # TODO: use pygame
    """
    plt.imshow(cm.cm_grid)
    

def visualize():
    cm = CostMap()
    points = np.random.rand(2, 20) * 10
    cm.add_new_points(points)
    plot_costmap(cm)
    plt.plot(points[0, :], points[1, :], "r.")
    x = cm.cm_points.reshape(-1, 2).T
    added_points = x[:, ~np.any(np.isnan(x), axis=0)]
    print(added_points)
    plt.plot(added_points[0, :], added_points[1, :], "b.")
    plt.show()

visualize()