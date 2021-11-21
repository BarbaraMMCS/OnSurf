
import requests

if __name__ == "__main__":
    data = {
        "lat": 46.400,
        "lon": -1.510,
        "model": "gfsWave",
        "parameters": ["waves"],
        "key": "IK8OOTjThIWGghVVuEYgCQ5MQ5x6UtmR"
    }
    response = requests.post("https://api.windy.com/api/point-forecast/v2", json=data)
    print(response.status_code)
    print(response.headers['content-type'])
    print(response.text)

