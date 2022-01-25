"""
Date: 22 nov 2021
Time: 09.45
Author: Barbara Symeon
Product name: OnSurf
Product general description: This document is part of the source files of the Small Proprietary Original Project OnSurf.
File content description: This file is a test file of the project.

This file contains the class TestUser which performs tests on SPOP main functions: add_surf_location,
remove_surf_location, get_weather and ask_on_surf_the_best_spot.
"""

import datetime

from app.DataModels import Location, CoordinatesGPS
from app.User import User

test_file = open("test.txt", "w")

class TestUser:
    def test_add_surf_location(self):
        test_file.write("\ntest_add_surf_location\n")
        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        assert location.location_name not in user.locations
        result = user.add_surf_location(location)
        assert result
        test_file.write(f"{user.add_surf_location(location)} PASSED\n")
        assert location.location_name in user.locations
        test_file.write(f"location.location_name in user.locations PASSED\n")
        assert user.locations[location.location_name] == location
        test_file.write(f"{user.locations[location.location_name]} == {location} PASSED\n")

    def test_remove_surf_location(self):
        test_file.write("\ntest_remove_surf_location\n")
        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        user.add_surf_location(location)
        assert location.location_name in user.locations
        result = user.remove_surf_location(location.location_name)
        assert result
        test_file.write(f"{user.remove_surf_location(location.location_name)} PASSED\n")
        assert location.location_name not in user.locations
        test_file.write(f"location.location_name not in user.locations PASSED\n")



    def test_get_weather(self):
        test_file.write("\ntest_get_weather\n")
        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        user.add_surf_location(location)
        assert location.location_name not in user.weather_reports
        result = user.get_weather(datetime.datetime.now())
        assert result
        test_file.write(f"{user.get_weather(datetime.datetime.now())} PASSED\n")
        assert location.location_name in user.weather_reports
        test_file.write(f"location.location_name in user.weather_reports PASSED\n")


    def test_ask_on_surf_the_best_spot(self, capfd):
        test_file.write("\ntest_ask_on_surf_the_best_spot\n")

        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        user.add_surf_location(location)
        result = user.ask_on_surf_the_best_spot()
        test_file.write(f"{user.ask_on_surf_the_best_spot()} PASSED\n")
        out, err = capfd.readouterr()
        assert result
        assert "The best beach to Surf is:\nlocation_name" in out
        test_file.write(f"The best beach to Surf is: location_name PASSED\n")

