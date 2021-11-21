import random
from datetime import datetime
from typing import Dict, List

import requests
from pydantic import BaseModel

from app.DataModels import Location, WeatherReport
from app.print_service import print_userspace


class User(BaseModel):
    username: str
    hash_password: str
    is_admin: bool = False
    locations: Dict[str, Location] = {}
    weather_reports: Dict[str, WeatherReport] = {}

    def oe_add_surf_location(self, location: Location) -> bool:
        if location.location_name in self.locations:
            print(f"{location} already exists")
        self.locations[location.location_name] = location
        return True

    def oe_remove_surf_location(self, location_name: str) -> bool:
        if location_name in self.locations:
            del self.locations[location_name]
        return True

    def oe_display_userspace(self) -> bool:
        print_userspace()
        for location in self.locations.values():
            print(f"{location}")
            print(f"{self.weather_reports.get(location.location_name, '')}\n")
        return True

    def oe_get_weather(self, time: datetime) -> bool:
        my_ts = time.timestamp()
        for location_name, location in self.locations.items():
            weather_report_dict = {"timestamp": my_ts}
            self._fill_weather_report(weather_report_dict, location, my_ts, "gfs", ["wind"])
            self._fill_weather_report(weather_report_dict, location, my_ts, "gfsWave", ["waves"])
            self.weather_reports[location_name] = WeatherReport.parse_obj(weather_report_dict)
        return True

    @staticmethod
    def _fill_weather_report(weather_report_dict: dict, location: Location, my_ts: float, model: str,
                             parameters: List[str]) -> None:
        data = {
            "lat": location.coordinates.latitude,
            "lon": location.coordinates.longitude,
            "model": model,
            "parameters": parameters,
            "key": "IK8OOTjThIWGghVVuEYgCQ5MQ5x6UtmR"
        }
        response = requests.post("https://api.windy.com/api/point-forecast/v2", json=data).json()
        index = 0
        for ts in response.get("ts", []):
            if ts > my_ts:
                break
            index += 1

        for unit_key, unit_value in response.get("units", {}).items():
            weather_report_key = unit_key.replace("-surface", "")
            weather_report_dict[weather_report_key] = response[unit_key][index]
            weather_report_dict[f"{weather_report_key}_unit"] = unit_value

    def oe_ask_on_surf_the_best_spot(self) -> bool:
        location_name = random.choice(list(self.locations.keys()))
        print("-" * 51 + f"\nThe best spot to go surfing:\n{self.locations[location_name]}\n" + "-" * 51 )
        return True
