# medAware home assignment

Submitted by: Amihai Ben-Arush

## Assignment description
Create a system that run an app that receive requests with JSON body containing 'is_db' key and true/false value.
If is_db value is true, the app should send a response with the content of a file located in a 'staging' dir, insert it's content to a database record and move the file to 'done' dir.
If is_db value is false only send the response with the file's content but don't insert it to the db and don't move the file to 'done' dir.

## Design
In order to facilitate the requirements of the assignment, I've built and containerized a Python application that can connect to and insert new records into a MySQL database. In addition I've set up a NGINX server to set inbound rules and perform health checks (not implemented yet)

## Installation
Clone repo, enter it and use docker-compose file to spin up the app

```bash
git clone https://github.com/amihaiba/medAware-project.git
cd medAware-project
docker-compose up -d
```

## Usage
Use `curl` to send a POST request with `is_db` and `file_name` keys
```bash
curl -X POST 127.0.0.1 -H 'Content-Type: application/json' -d '{"is_db":<0|1>,"file_name":"<file1.txt|file2.txt|file3.txt>"}'
```
Specify which file you want in the `file_name` value and set `is_db` to 1 if you want it to be inserted to the db and moved to `done` directory.

To enter the containers:

Application container:
```
docker exec -ti med-app /bin/bash
```
MySQL database container:
```
docker exec -ti med-app-mysql mysql -u med_user -pmed_pass
```
NGINX container:
```
docker exec -ti med-app-nginx /bin/bash
```
