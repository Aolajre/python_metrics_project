# python_metrics_project

# This project is all about building a metrics flask application from scratch using python3 and various requirements
3Creating Dockerfile
#Building DockerImage
#Running Docker Container
#Docker Commands
Create ECR repository using Python Boto3 and pushing Docker Image to ECR
Using Kubernetes and Creating EKS cluster and Nodegroups
Creating Kubernetes Deployments and Services using Python!

## **Part 1: Deploying the Flask application locally**

### **Step 2: Install dependencies**

The application uses the **`psutil`** and **`Flask`, Plotly, boto3** libraries. Install them using pip:

pip3 install -r requirements.txt


### **Step 3: Run the application**

To run the application, navigate to the root directory of the project and execute the following command:

$ python3 app.py


This will start the Flask server on **`localhost:5000`**. Navigate to [http://localhost:5000/](http://localhost:5000/) on your browser to access the application.

## **Part 2: Dockerizing the Flask application**

### **Step 1: Creating a Dockerfile**

Create a **`Dockerfile`** in the root directory of the project with the following contents:

Use the official Python image as the base image
FROM python:3.9-slim-buster

Set the working directory in the container
WORKDIR /app

Copy the requirements file to the working directory
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

Copy the application code to the working directory
COPY . .

Set the environment variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

Expose the port on which the Flask app will run
EXPOSE 5000

Start the Flask app when the container is run
CMD ["flask", "run"]


### **Step 2: Building the Docker image**

To build the Docker image, execute the following command:

$ docker build -t <image_name> .


### **Step 3: Running the Docker container**

To run the Docker container, execute the following command:

$ docker run -p 5000:5000 <image_name>


This will start the Flask server in a Docker container on **`localhost:5000`**. Navigate to [http://localhost:5000/](http://localhost:5000/) on your browser to access the application.

## **Part 3: Pushing the Docker image to ECR**

### **Step 1: Create an ECR repository**

Create an ECR repository using Python:

import boto3

Create an ECR client
ecr_client = boto3.client('ecr')

Create a new ECR repository
repository_name = 'my-ecr-repo' response = ecr_client.create_repository(repositoryName=repository_name)

Print the repository URI
repository_uri = response['repository']['repositoryUri'] print(repository_uri)


### **Step 2: Push the Docker image to ECR**

Push the Docker image to ECR using the push commands on the console:

$ docker push <ecr_repo_uri>:


## **Part 4: Creating an EKS cluster and deploying the app using Python**

### **Step 1: Create an EKS cluster**

Create an EKS cluster and add node group

### **Step 2: Create a node group**

Create a node group in the EKS cluster.

### **Step 3: Create deployment and service**

Once you run this file by running “python3 my_kubernetes.py” deployment and service will be created.
Check by running following commands:
kubectl get deployment -n default (check deployments)
kubectl get service -n default (check service)
kubectl get pods -n default (to check the pods)
Once your pod is up and running, run the port-forward to expose the service

kubectl port-forward service/<service_name> 5000:5000
