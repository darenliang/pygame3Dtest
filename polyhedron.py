import math
from typing import List, Tuple

from point import Point


class Polyhedron:
    """
    Polyhedron abstraction to improve rotation operation efficiency by only
    computing each point rotations exactly one time
    """

    def __init__(self, points: List[Point], edges: List[Tuple[Point, Point]]):
        """
        Polyhedron constructor
        :param points: points to set
        :param edges: edges to set
        """
        self.points = points
        self.edges = edges


def create_cube() -> Polyhedron:
    """
    Create cube
    :return: Cube
    """
    p1 = Point(1, 1, 1)
    p2 = Point(1, 1, -1)
    p3 = Point(1, -1, 1)
    p4 = Point(1, -1, -1)
    p5 = Point(-1, 1, 1)
    p6 = Point(-1, 1, -1)
    p7 = Point(-1, -1, 1)
    p8 = Point(-1, -1, -1)

    return Polyhedron(
        [p1, p2, p3, p4, p5, p6, p7, p8],
        [
            (p1, p5), (p5, p7), (p7, p3), (p3, p1),
            (p2, p6), (p6, p8), (p8, p4), (p4, p2),
            (p1, p2), (p5, p6), (p7, p8), (p3, p4)
        ]
    )


def create_tetrahedron() -> Polyhedron:
    """
    Create tetrahedron
    :return: Tetrahedron
    """
    p1 = Point(2 * math.sqrt(8 / 9), 0, -2 / 3)
    p2 = Point(-2 * math.sqrt(2 / 9), 2 * math.sqrt(2 / 3), -2 / 3)
    p3 = Point(-2 * math.sqrt(2 / 9), -2 * math.sqrt(2 / 3), -2 / 3)
    p4 = Point(0, 0, 2)

    return Polyhedron(
        [p1, p2, p3, p4],
        [
            (p1, p2), (p2, p3), (p3, p1),
            (p1, p4), (p2, p4), (p3, p4)
        ]
    )


def create_octahedron() -> Polyhedron:
    """
    Create octahedron
    :return: Octahedron
    """
    p1 = Point(2, 0, 0)
    p2 = Point(-2, 0, 0)
    p3 = Point(0, 2, 0)
    p4 = Point(0, -2, 0)
    p5 = Point(0, 0, 2)
    p6 = Point(0, 0, -2)

    return Polyhedron(
        [p1, p2, p3, p4, p5, p6],
        [
            (p1, p3), (p3, p2), (p2, p4), (p4, p1),
            (p1, p5), (p2, p5), (p3, p5), (p4, p5),
            (p1, p6), (p2, p6), (p3, p6), (p4, p6)
        ]
    )


def create_icosahedron() -> Polyhedron:
    """
    Create icosahedron
    :return: Icosahedron
    """
    phi = (1 + math.sqrt(5)) / 2

    p1 = Point(0, 1, phi)
    p2 = Point(0, 1, -phi)
    p3 = Point(0, -1, phi)
    p4 = Point(0, -1, -phi)
    p5 = Point(1, phi, 0)
    p6 = Point(1, -phi, 0)
    p7 = Point(-1, phi, 0)
    p8 = Point(-1, -phi, 0)
    p9 = Point(phi, 0, 1)
    p10 = Point(phi, 0, -1)
    p11 = Point(-phi, 0, 1)
    p12 = Point(-phi, 0, -1)

    return Polyhedron(
        [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12],
        [
            (p1, p3), (p1, p5), (p1, p7), (p1, p9), (p1, p11),
            (p3, p9), (p9, p5), (p5, p7), (p7, p11), (p11, p3),
            (p4, p2), (p4, p6), (p4, p8), (p4, p10), (p4, p12),
            (p2, p10), (p10, p6), (p6, p8), (p8, p12), (p12, p2),
            (p2, p5), (p5, p10), (p10, p9), (p9, p6), (p6, p3),
            (p3, p8), (p8, p11), (p11, p12), (p12, p7), (p7, p2)
        ]
    )
