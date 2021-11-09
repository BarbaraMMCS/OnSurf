# OnSurf

Run the server
> python3 -m app.main

Dependencies
> automatically installed on replit by "poetry"

Hosts
If Replit the server adress is 
> https://OnSurf.barbarasymeon.repl.co/

If local the server adress is 
> http://0.0.0.0:8000/


Create User from Replit local host
> curl -X POST -H "Content-Type: application/json" -d '{"username": "barbara", "password": "mypassword"}' https://OnSurf.barbarasymeon.repl.co/create/user

Create User from own local host
> curl -X POST -H "Content-Type: application/json" -d '{"username": "barbara", "password": "mypassword"}' http://0.0.0.0:8000/create/user

Add Location from own local host
> curl -X 'POST' 'http://0.0.0.0:8000/add/location' -u username:password -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"longitude": 0, "latitude": 0, "location_name": "lux"}'

