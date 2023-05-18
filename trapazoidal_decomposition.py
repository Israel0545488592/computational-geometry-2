import numpy as np



def fetch_data(src: str): return np.loadtxt(fname = src, skiprows = 1, converters = float, dtype = np.uint16)

def orient2D(vx1, vx2, vx3) -> bool:      return np.linalg.det(np.vstack((np.ones(3), np.vstack((vx1, vx2, vx3)).transpose()))) > 0
def orient3D(vx1, vx2, vx3, pnt) -> bool: return np.linalg.det(np.vstack((np.ones(4), np.vstack((vx1, vx2, vx3, pnt)).transpose()))) > 0


class facet:

    def __init__(self, vx1, vx2, vx3):
        self.vx1, self.vx2, self.vx3 = (vx1, vx2, vx3) if orient2D(vx1, vx2, vx3) else (vx3, vx2, vx1)

    # I think we need a boolen method method that tells us wether a point p 'sees' this facet



def CH_3D(points: np.ndarray):

    ''' Randomized Incremental Algorithm for computing 3D - convex hull '''

    # init the 1st 3 faces
    confilctG = {} # (point, set(face)) map

    np.random.shuffle(points)

    for p in points:

        # get faces viewed by p and destroy them

        # build new facets with p and the horizon edges

        confilctG # update

    return sorted(confilctG.values(), key = "the ordered he asked for")