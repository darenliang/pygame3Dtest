class Point:
    """
    Simple point abstraction to allow class referencing via "pointers"
    """

    def __init__(self, x: float, y: float, z: float):
        """
        Point constructor
        :param x: x coordinate
        :param y: y coordinate
        :param z: z coordinate
        """
        self.coordinates = (x, y, z)
