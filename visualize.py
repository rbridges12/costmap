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
    points = np.random.rand(2, 20) * 20
    cm.add_new_points(points)
    plt.plot(points[0, :], points[1, :], "r.")
    plot_costmap(cm)
    plt.show()

visualize()