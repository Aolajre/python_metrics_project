# Use Official light weight image from Registry
FROM python:3.10-slim-buster

# Set the working directory of the container
WORKDIR /app

# Copy the requirements depends to the working directory
COPY requirements.txt .

# Upgrade pip and Install the required Python packages using the requiments.txt file 
RUN pip3 install --no-cache-dir -r requirements.txt 

# Copy the application code into the working directory 
COPY . .

# Setting the required environmental variables for the Flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port with which the Flask app will run on
EXPOSE 5000

# Using CMD executables, start the flask app when the container is running
CMD ["flask", "run"]