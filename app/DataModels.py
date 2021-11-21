import datetime
from enum import Enum

from pydantic import BaseModel, Field


class CoordinatesGPS(BaseModel):
    longitude: float = Field(..., gt=-180, le=180)
    latitude: float = Field(..., gt=-90, le=90)


class Location(BaseModel):
    location_name: str
    coordinates: CoordinatesGPS

    def __str__(self):
        lat_suffix = "°N" if self.coordinates.latitude > 0 else "°S"
        lon_suffix = "°W" if self.coordinates.longitude > 0 else "°E"
        return f"{self.location_name} ({abs(self.coordinates.latitude):.3f}{lat_suffix} - {abs(self.coordinates.longitude):.3f}{lon_suffix})"


class CompassPoints(str, Enum):
    N = 'N'
    NE = 'NE'
    E = 'E'
    SE = 'SE'
    S = 'S'
    SW = 'SW'
    W = 'W'
    NW = 'NW'


class WeatherReport(BaseModel):
    waves_height: float
    waves_height_unit: str
    waves_direction: float
    waves_direction_unit: str
    wind_u: float
    wind_u_unit: str
    wind_v: float
    wind_v_unit: str
    timestamp: float

    def __str__(self):
        return (f"    Weather report: {datetime.datetime.fromtimestamp(self.timestamp).strftime('%A - %d %B %Y - %HH')}\n"
               f"        Waves: {abs(self.waves_height):.2f}{self.waves_height_unit}"
               f" - {abs(self.waves_direction):.2f}{self.waves_direction_unit}\n"
               f"        Wind: {abs(self.wind_u):.2f}{self.wind_u_unit}"
               f" - {abs(self.wind_v):.2f}{self.wind_v_unit}\n")
