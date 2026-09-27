# Python Frontend DevOps App

A beginner-friendly web app using Python + Flask, with an HTML/CSS frontend.

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000

## Run with Docker
```bash
docker build -t python-frontend-app .
docker run -d --name python-frontend-app -p 8080:5000 python-frontend-app
docker ps
docker logs python-frontend-app
```
Open http://localhost:8080

## Run on EC2
1. Copy or clone this project onto EC2.
2. Ensure Docker is installed and running.
3. Run the Docker commands above from this project directory.
4. Add an EC2 Security Group inbound rule for TCP 8080, preferably limited to your IP for testing.
5. Open http://YOUR-EC2-PUBLIC-IP:8080

The app listens on container port 5000; Docker maps EC2 port 8080 to container port 5000. This is a learning demo, not a production monitoring tool.
