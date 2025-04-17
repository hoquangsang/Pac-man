import math
from .vector import Vector2

def euclidean_distance(vec1: Vector2, vec2: Vector2):
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt((vec1[0] - vec2[0])**2 + (vec1[1] - vec2[1])**2)

def manhattan_distance(vec1: Vector2, vec2: Vector2):
    """
    Calculate the Manhattan distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
        float: The Manhattan distance between the two points.
    """
    return abs(vec1[0] - vec2[0]) + abs(vec1[1] - vec2[1])

def chebyshev_distance(vec1: Vector2, vec2: Vector2):
    """
    Calculate the Chebyshev distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).

    Returns:
        float: The Chebyshev distance between the two points.
    """
    return max(abs(vec1[0] - vec2[0]), abs(vec1[1] - vec2[1]))

def minkowski_distance(vec1: Vector2, vec2: Vector2, p: int):
    """
    Calculate the Minkowski distance between two points in 2D space.

    Args:
        point1 (tuple): Coordinates of the first point (x1, y1).
        point2 (tuple): Coordinates of the second point (x2, y2).
        p (int): The order of the Minkowski distance.

    Returns:
        float: The Minkowski distance between the two points.
    """
    return (abs(vec1[0] - vec2[0])**p + abs(vec1[1] - vec2[1])**p)**(1/p)
