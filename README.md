# OnSurf

Run the server
> python3 -m app.main

Dependencies
> automatically installed on replit by "poetry"

Create User
> curl -X POST -H "Content-Type: application/json" -d '{"username": "barbara", "password": "mypassword"}' http://127.0.0.1:8000/create/user

Add Location
> curl -X 'POST' 'http://0.0.0.0:8000/add/location' -u username:password -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"longitude": 0, "latitude": 0, "location_name": "lux"}'
