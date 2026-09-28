1. Build the Docker image

docker build -t python-frontend-app .

<img width="1733" height="156" alt="image" src="https://github.com/user-attachments/assets/4b867b45-c541-4c17-a555-2fcc53ccfccf" />



2. Run the application

docker run -d --name python-frontend-app -p 8080:5000 python-frontend-app

3. Check the container

docker ps

<img width="1883" height="141" alt="image" src="https://github.com/user-attachments/assets/7720e5cb-d232-480d-aef5-2345fab0265f" />

docker logs python-frontend-app

4. Open the application

In your browser, visit:

http://YOUR-EC2-PUBLIC-IP:8080
