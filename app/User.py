"""
Date: 22 nov 2021
Time: 09.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is part of the source files
of the Small Proprietary Original Project OnSurf.
File content description: This file is a class file of the project.

This file contains the class User which inherits from the class BaseModel
from the Pydantic library.
Defining a base model for User allows to pass data to the object
and ensure all fields will conform to types defined in the model.

The User class defines attributes username, hash_password, is_admin,
locations and weather_reports.
The class methods allow the user to interact with their userspace
with output events such as add_surf_location, remove_surf_location,
display_userspace, get_weather and ask_on_surf_the_best_spot

The userspace is an abstract idea which concretely is the combination
of locations of type Location and weather_reports of type WeatherReport
as dictionaries for a specific user.

Finally, the static private method _fill_weather_report post a weather request
to the windy API:
https://api.windy.com/point-forecast/docs (Windy)
This method generate a json object with the Api response to the Post request sent.
A timestamp filters the api response to keep only the values
for the date and time the user asked a weather report for.
The weather keys are renamed and the values are passed in
the weather_report dictionary of the user.
note:
In the get_weather there is two post requests using _fill_weather_report.
One request for wind and one request for waves.
"""
import random
from datetime import datetime
from typing import Dict, List

import requests
from pydantic import BaseModel

from app.DataModels import Location, WeatherReport
from app.print_service import print_userspace, print_line


class User(BaseModel):
    username: str
    hash_password: str
    is_admin: bool = False
    locations: Dict[str, Location] = {}
    weather_reports: Dict[str, WeatherReport] = {}

    def add_surf_location(self, location: Location) -> bool:
        if location.location_name in self.locations:
            print(f"{location} already exists")
        self.locations[location.location_name] = location
        return True

    def remove_surf_location(self, location_name: str) -> bool:
        if location_name in self.locations:
            del self.locations[location_name]
        return True

    def display_userspace(self) -> bool:
        print_userspace()
        for location in self.locations.values():
            print_line("_")
            print(f"{location}")
            print(f"{self.weather_reports.get(location.location_name, '')}\n")
        return True

    def get_weather(self, time: datetime) -> bool:
        my_ts = time.timestamp()
        for location_name, location in self.locations.items():
            weather_report_dict = {"timestamp": my_ts}
            self._fill_weather_report(weather_report_dict, location, my_ts,
                                      "gfs", ["wind"])
            self._fill_weather_report(weather_report_dict, location, my_ts,
                                      "gfsWave", ["waves"])
            self.weather_reports[location_name] = \
                WeatherReport.parse_obj(weather_report_dict)
        return True

    def ask_on_surf_the_best_spot(self) -> bool:
        # The surf spot is randomly selected. It is not the final version.
        # I will allocate 1h budget to improve this method.
        location_name = random.choice(list(self.locations.keys()))
        print_line("*")
        print(f"\nThe best beach to Surf is:\n{self.locations[location_name]}\n")
        print_line("*")
        return True

    @staticmethod
    def _fill_weather_report(weather_report_dict: dict, location: Location,
                             my_ts: float, model: str, parameters: List[str]) -> None:
        data = {
            "lat": location.coordinates.latitude,
            "lon": location.coordinates.longitude,
            "model": model,
            "parameters": parameters,
            "key": "IK8OOTjThIWGghVVuEYgCQ5MQ5x6UtmR"
        }
        response = requests.post("https://api.windy.com/api/point-forecast/v2",
                                 json=data).json()
        index = 0
        for ts in response.get("ts", []):
            if ts > my_ts:
                break
            index += 1

        for unit_key, unit_value in response.get("units", {}).items():
            weather_report_key = unit_key.replace("-surface", "")
            weather_report_dict[weather_report_key] = response[unit_key][index]
            weather_report_dict[f"{weather_report_key}_unit"] = unit_value
