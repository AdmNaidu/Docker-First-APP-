1. Build the Docker image

docker build -t python-frontend-app .

2. Run the application

docker run -d --name python-frontend-app -p 8080:5000 python-frontend-app

3. Check the container

docker ps
docker logs python-frontend-app

4. Open the application

In your browser, visit:

http://YOUR-EC2-PUBLIC-IP:8080