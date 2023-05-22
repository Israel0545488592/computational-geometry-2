import numpy as np
from itertools import product
from typing import Tuple
Point = np.ndarray



def fetch_data(src: str): return np.loadtxt(fname = src, skiprows = 1, converters = float, dtype = np.uint16)

def orient(vx1, vx2, vx3, pnt) -> bool: return np.linalg.det(np.vstack((np.ones(4), np.vstack((vx1, vx2, vx3, pnt)).transpose()))) > 0


class facet:

    def __init__(self, vxs: Tuple[Point], refrence: Point, neighbours: Tuple['facet']):

        self.vxs = vxs if orient(* vxs, refrence) else tuple(reversed(vxs))
        self.neibourhood = neighbours

    def sees(self, refrence: Point) -> bool: return orient(* self.vxs, refrence)

    def get_horizion(self, refrence: Point) -> Tuple['facet']: pass


def CH_3D(points: np.ndarray):

    ''' Randomized Incremental Algorithm for computing 3D - convex hull '''

    # 1. permuting input randomly

    np.random.shuffle(points)

    # 2. initiating conflict graph

    start, points = points = points[:4], points[4:]

    faces2points = { facet(* filter(lambda vx : vx != refrence), refrence) : set()  for refrence in start }
    points2faces = { pnt : set()  for pnt in points }

    for pnt, face in product(points, faces2points):
        if not face.sees(pnt): continue
        points2faces[pnt].add(face)
        faces2points[face].add(pnt)

    # 3. executing the rest of the algo iterativly

    for ind, pnt in enumerate(points):

        conflicted_faces = points2faces[pnt]

        horizon = [face.get_horizon(pnt) for face in conflicted_faces] # horizon edges

        # add new faces, we also need to connect them to the old faceses neighbours
        new_faces = []

        # deystroying old faces
        for face in conflicted_faces:
            for observer_pnt in faces2points[face]:
                points2faces[observer_pnt].remove(face)
        del faces2points[face]


    return sorted(faces2points, key = "the ordered he asked for")