"""
Date: 22 nov 2021
Time: 09.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is part of the source files
of the Small Proprietary Original Project OnSurf.
File content description: This file is a class file of the project.

This file contains classes CoordinatesGPS, Location, WeatherReport
which inherits from the class BaseModel from the Pydantic library.
Defining a base model for these classes allows to pass data to the object
and ensure all fields will conform to types defined in the model.

The class CoordinatesGPS ensures that the attributes longitude and latitude
will be constraint to be float types restricted to the values
between -180, 180 and -90, 90, respectively.

The Location class ensures that a Location has a location_name of type string
and coordinates of type CoordinatesGPS.
This class also has the base __str__ method overwritten
such that suffixes °N, °S for latitude and °W, °E for longitude matches coordinates.

The last class WeatherReport ensures that each attribute:
waves_height, waves_direction, wind_u, wind_v and timestamp are passed information
as defined in the model.
This class also has the base __str__ method overwritten as the attribute
information are not presented to the user as stored in the system.
First, date and time are given using the method weather_datetime.
Then, waves direction is presented as cardinal points instead of degrees for clarity.
The waves_height is presented to the user with a precision of 10**-1 in meters.
The wind_speed method returns the wind speed calculated by finding the distance
between attribute wind_u and wind_v.
This speed is given in knots to the user using the method wind_speed_knots.
Lastly, wind_direction returns the wind direction in degrees
from the polar angle of the wind_speed vector,
which is presented to the user as compass points instead of degrees for clarity.
"""
import datetime
from math import sqrt, atan2, pi

from pydantic import BaseModel, Field

from app.CompassPoints import degree_to_compass_points


class CoordinatesGPS(BaseModel):
    longitude: float = Field(..., gt=-180, le=180)
    latitude: float = Field(..., gt=-90, le=90)


class Location(BaseModel):
    location_name: str
    coordinates: CoordinatesGPS

    def __str__(self):
        lat_suffix = "°N" if self.coordinates.latitude > 0 else "°S"
        lon_suffix = "°W" if self.coordinates.longitude > 0 else "°E"
        return f"{self.location_name} ({abs(self.coordinates.latitude):.3f}" \
               f"{lat_suffix} - {abs(self.coordinates.longitude):.3f}{lon_suffix})"


class WeatherReport(BaseModel):
    waves_height: float
    waves_direction: int
    wind_u: float
    wind_v: float
    timestamp: float

    def __str__(self):
        date_and_time = datetime.datetime.fromtimestamp(self.timestamp)

        return (
            f"Weather report: {date_and_time.strftime('%A - %d %B %Y - %HH')}\n"
            f"        Waves: {degree_to_compass_points(abs(self.waves_direction))}"
            f" - {abs(self.waves_height):.1f}m\n"
            f"        Wind: {degree_to_compass_points(self.wind_direction())}"
            f" - {self.wind_speed_knots()} Knots\n")

    def wind_speed(self) -> float:
        return sqrt(self.wind_u ** 2 + self.wind_v ** 2)

    def wind_speed_knots(self) -> int:
        return int((self.wind_speed()) * 1.943844)

    def wind_direction(self) -> int:
        wind = atan2(self.wind_u / self.wind_speed(), self.wind_v / self.wind_speed())
        wind_to_degrees = wind * 180 / pi
        wind_from_degrees = int(wind_to_degrees + 180)
        return 90 - wind_from_degrees
