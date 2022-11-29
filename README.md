back end challenge

## About the project

Back end challenge, would have to decode a file based on CNAB (Procol used for banking communication in Brazil) 
saving in relational database, and making it available through a simple page, only registered users can access the resource

file to be consumed:
````
https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt
````

##


## Getting Started

Setup project environment with virtual environments and pip.
```
## Create virtual enviromnment
$python3 -m venv venv 

##Active virtual environment and install dependencies
$source venv/bin/activate
$pip install -r requirements.txt

## Run server project 
run project on your localhost
```

Optional Running project in Docker
````
$docker compose up

## Base url Docker
http://localhost:8001

`````

## Access features

important, to access the resources it is necessary to be logged in,
if you try to access directly through the link without being logged in, you will be redirected to the login page

1. Register user:
````

http://localhost:8000/api/register_page

## Docker
http://localhost:8001/api/register_page
````
2. Login:
````
http://localhost:8000/api/login_page

## Docker
http://localhost:8001/api/login_page

````
3. After logging in you will be redirected to home , having access to the resources

4. Upload cnab txt file:
````
http://localhost:8000/api/upload

## Docker
http://localhost:8001/api/upload
````
5. Access registration information in the database
````
http://localhost:8000/api/data

## Docker

http://localhost:8001/api/data
````


