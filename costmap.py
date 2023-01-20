import numpy as np

CM_CELL_SIZE = 1
CM_WIDTH = 10

class CostMap:
    map_to_corner: np.ndarray
    corner_to_cm: np.ndarray
    cm_to_rover: np.ndarray
    cm_grid: np.ndarray

    def __init__(self) -> None:
        
        # init transforms to zero
        self.map_to_corner = np.eye(3)
        self.corner_to_cm = np.eye(3)
        self.cm_to_rover = np.eye(3)

        # transform from costmap corner to center
        self.corner_to_cm[:2, 2] = [CM_WIDTH / 2, CM_WIDTH / 2]

        # determine costmap size from width and cell size, init to zeros
        cells = np.ceil(CM_WIDTH / CM_CELL_SIZE).astype(int)
        self.cm_grid = np.zeros((cells, cells))
    
    def new_pointcloud(self, points: np.ndarray):
        """
        update the costmap given the new set of points
        :param points: 2xN numpy array containing [x, y] points in the rover frame
        """

        # convert points to homogenous form
        h_points = np.vstack((points, np.ones(points.shape[1])))

        # transform points into costmap corner frame
        h_points_corner = self.corner_to_cm @ self.cm_to_rover @ h_points
    
        # convert out of homogenous form
        points_corner = h_points_corner[:2, :]

    def update_costmap(self, points: np.ndarray):
        """
        add the given set of points to the costmap
        :param points: 2xN numpy array containing [x, y] points in the costmap corner frame
        """

        for p in points.T:
            x_id = np.floor((p[0] - min_x) / pixel_size).astype(int)
            y_id = np.floor((p[1] - min_y) / pixel_size).astype(int)