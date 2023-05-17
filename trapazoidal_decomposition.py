import numpy as np

def fetch_data(src: str): return np.loadtxt(fname = src, skiprows = 1, converters = float, dtype = np.uint16)

class facet:

    def __init__(self, p1: np.ndarray, p2: np.ndarray, p3: np.ndarray, p4: np.ndarray) -> None:
        self.p1, self.p2, self.p3, self.p4 = p1, p2, p3, p4
        # now we gotta sort'em in the way he asked

    # I think we need a boolen method method that tells us wether a point p 'sees' this facet



def CH_3D(points: np.ndarray):

    # init the 1st 3 faces
    confilctG = {} # (point, face) map

    np.random.shuffle(points)

    for p in points:

        # get faces viewed by p and destroy them

        # build new facets with p and the horizon edges

        confilctG # update

    return sorted(confilctG.values(), key = "the ordered he asked for")