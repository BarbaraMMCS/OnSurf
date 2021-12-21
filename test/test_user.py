import datetime

from app.DataModels import Location, CoordinatesGPS
from app.User import User


class TestUser:
    def (self):
        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        assert location.location_name not in user.locations

        result = user.add_surf_location(location)
        assert result
        assert location.location_name in user.locations
        assert user.locations[location.location_name] == location

    def test_remove_surf_location(self):
        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        user.add_surf_location(location)
        assert location.location_name in user.locations

        result = user.remove_surf_location(location.location_name)
        assert result
        assert location.location_name not in user.locations

    def test_get_weather(self):
        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        user.add_surf_location(location)
        assert location.location_name not in user.weather_reports

        result = user.get_weather(datetime.datetime.now())
        assert result
        assert location.location_name in user.weather_reports

    def test_ask_on_surf_the_best_spot(self, capfd):
        user = User(username="username", hash_password="hash_password")
        location = Location(location_name="location_name", coordinates=CoordinatesGPS(longitude=0, latitude=0))
        user.add_surf_location(location)
        result = user.ask_on_surf_the_best_spot()
        out, err = capfd.readouterr()
        assert result
        assert "The best beach to Surf is:\nlocation_name" in out
