import math

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def manhattan_distance(point1, point2):
    """
    Calculate the Manhattan distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
        float: The Manhattan distance between the two points.
    """
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def chebyshev_distance(point1, point2):
    """
    Calculate the Chebyshev distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
        float: The Chebyshev distance between the two points.
    """
    return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))

def minkowski_distance(point1, point2, p):
    """
    Calculate the Minkowski distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).
        p (int): The order of the Minkowski distance.

    Returns:
        float: The Minkowski distance between the two points.
    """
    return (abs(point1[0] - point2[0])**p + abs(point1[1] - point2[1])**p)**(1/p)
