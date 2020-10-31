from typing import Tuple

import numpy
from scipy import spatial

import config
from polyhedron import Polyhedron


def apply_rotation(
        polyhedron: Polyhedron,
        angle: float,
        axis: Tuple[float, float, float]
):
    """
    Apply rotation to polyhedron
    :param polyhedron: Polyhedron
    :param angle: Angle of rotation in degrees
    :param axis: Axis of rotation
    """
    rotation_radians = numpy.radians(angle)
    rotation_axis = numpy.array(axis)
    rotation_vector = rotation_radians * rotation_axis
    rotation = spatial.transform.Rotation.from_rotvec(rotation_vector)

    for point in polyhedron.points:
        point.coordinates = rotation.apply(point.coordinates)


def adjust_coordinate(n: float) -> float:
    """
    Adjust coordinate for display
    :param n: Float number
    :return: Adjust float value
    """
    return n * config.SCALE_FACTOR + config.MIDDLE_LENGTH
