1. Build the Docker image

docker build -t python-frontend-app .

<img width="1733" height="156" alt="image" src="https://github.com/user-attachments/assets/4b867b45-c541-4c17-a555-2fcc53ccfccf" />



2. Run the application

docker run -d --name python-frontend-app -p 8080:5000 python-frontend-app

3. Check the container

docker ps

<img width="1883" height="141" alt="image" src="https://github.com/user-attachments/assets/7720e5cb-d232-480d-aef5-2345fab0265f" />

docker logs python-frontend-app

Ensure your EC2 Security Group allows inbound TCP port 8080 from your IP address

<img width="1481" height="294" alt="image" src="https://github.com/user-attachments/assets/6974dca7-8b65-4522-b2ff-fa6206a746a5" />



4. Open the application

In your browser, visit:

http://YOUR-EC2-PUBLIC-IP:8080

<img width="1574" height="819" alt="image" src="https://github.com/user-attachments/assets/7f14dcf9-f1b1-4cb1-9bcf-305f891439e6" />

