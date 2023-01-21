import numpy as np

CM_CELL_SIZE = 1
CM_WIDTH = 10

class CostMap:
    # transforms
    map_to_corner: np.ndarray
    corner_to_cm: np.ndarray
    cm_to_rover: np.ndarray

    # NxN grid to store cost values
    cm_grid: np.ndarray

    # NXNx2 array of points underlying grid
    cm_points: np.ndarray

    # TODO: refactor 2xN to Nx2

    def __init__(self) -> None:
        
        # init transforms to zero
        self.map_to_corner = np.eye(3)
        self.corner_to_cm = np.eye(3)
        self.cm_to_rover = np.eye(3)

        # transform from costmap corner to center
        self.corner_to_cm[:2, 2] = [CM_WIDTH / 2, CM_WIDTH / 2]

        # determine costmap size from width and cell size, init to zeros
        # TODO: rename num_cells
        self.num_cells = np.ceil(CM_WIDTH / CM_CELL_SIZE).astype(int)
        self.cm_grid = np.zeros((self.num_cells, self.num_cells))
        
        self.cm_points = np.zeros((self.num_cells, self.num_cells, 2))
        self.cm_points[:] = np.nan
    
    def add_new_points(self, points: np.ndarray):
        """
        update the costmap given the new set of points
        :param points: 2xN numpy array containing [x, y] points in the rover frame
        """

        # convert points to homogenous form
        h_points = np.vstack((points, np.ones(points.shape[1])))

        # transform points into costmap corner frame
        h_points_corner = self.corner_to_cm @ self.cm_to_rover @ h_points
        # h_points_corner = h_points
    
        # convert out of homogenous form
        points_corner = h_points_corner[:2, :]

        # points = points_corner

        # get costmap indices to put points at
        # TODO: refactor to reduce unecessary stuff
        ids = np.floor(points / CM_CELL_SIZE).astype(int)
        valid_mask = np.all(ids < self.num_cells, axis=0) 
        valid_ids = ids[:, valid_mask]
        valid_points = points[:, valid_mask]
        
        # swap from x,y order to i,j order
        self.cm_grid[valid_ids[1, :], valid_ids[0, :]] = 1
        self.cm_points[valid_ids[1, :], valid_ids[0, :], :] = valid_points.T
        

    def update_rover(self, map_to_rover: np.ndarray):
        
        # calculate delta transform
        
        # propagate costmap with delta transform
        
        # split map to rover transform into map to cm and cm to rover, update each
        ...
    
    def propagate(self, delta_tf: np.ndarray):
        
        # apply delta_tf to all underlying points

        
        # empty costmap
        
        # add_new_points to costmap
        ...