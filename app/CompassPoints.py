"""
Date: 22 nov 2021
Time: 09.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is part of the source files of the Small Proprietary Original Project OnSurf.
File content description: This file is a class file of the project.

This file contains the class CompassPoints which is an enumeration to facilitate the use of compass points names.

And this file contains one useful function degree_to_compass_points.
This function uses CompassPoints to return compass point names if given a polar angle
"""

from enum import Enum


class CompassPoints(str, Enum):
    N = 'North'
    NE = 'North East'
    E = 'East'
    SE = 'South East'
    S = 'South'
    SW = 'South West'
    W = 'West'
    NW = 'South West'


def degree_to_compass_points(degree: int) -> str:
    compass_points = [CompassPoints.N, CompassPoints.NE, CompassPoints.E, CompassPoints.SE, CompassPoints.S,
                      CompassPoints.SW, CompassPoints.W, CompassPoints.NW]
    ix = round(degree / (360. / len(compass_points)))
    return compass_points[ix % len(compass_points)]
