import numpy as np
from itertools import combinations, product



def fetch_data(src: str): return np.loadtxt(fname = src, skiprows = 1, converters = float, dtype = np.uint16)

def orient2D(vx1, vx2, vx3) -> bool:      return np.linalg.det(np.vstack((np.ones(3), np.vstack((vx1, vx2, vx3)).transpose()))) > 0
def orient3D(vx1, vx2, vx3, pnt) -> bool: return np.linalg.det(np.vstack((np.ones(4), np.vstack((vx1, vx2, vx3, pnt)).transpose()))) > 0


class facet:

    def __init__(self, vx1, vx2, vx3):
        self.vx1, self.vx2, self.vx3 = (vx1, vx2, vx3) if orient2D(vx1, vx2, vx3) else (vx3, vx2, vx1)

    # I think we need a boolen method method that tells us wether a point p 'sees' this facet



def CH_3D(points: np.ndarray):

    ''' Randomized Incremental Algorithm for computing 3D - convex hull '''

    # 1. permuting randomly

    np.random.shuffle(points)

    # 2. initiating conflict graph

    faces2points = { facet( * vxs) : set()  for vxs in combinations(points[:4], 3) }
    points = points[4:]
    points2faces = { pnt : set()  for pnt in points }

    for pnt, face in product(points, faces2points):
        if not face.sees(pnt): continue
        points2faces[pnt].add(face)
        faces2points[face].add(pnt)

    # 3. executing the rest of the algo iterativly

    for ind, pnt in enumerate(points):

        conflicted_faces = points2faces[pnt]
        if not conflicted_faces: continue

        # build new facets and updtae conflict graph acorrdingly
        horizon_edges = []  # implement here, should be list of tuples of points
        new_faces = [facet( * edge, pnt) for edge in horizon_edges]
        for face in new_faces:
            conflicted_points = {} # implement here
            for cnf_pnt in conflicted_points:
                points2faces[cnf_pnt].add(face)
            faces2points[face].update(conflicted_points)

        # deystroying faces in conflict
        for face in conflicted_faces:
            for observer_pnt in faces2points[face]:
                points2faces[observer_pnt].remove(face)
        del faces2points[face]


    return sorted(faces2points, key = "the ordered he asked for")