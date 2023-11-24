# Use the official PostgreSQL image as the parent image
FROM ubuntu/postgres:latest

# Add Python and Git
RUN apt update && apt install -y python3 python3-pip git

# Create a new directory for the application
RUN mkdir /app

# Clone the repository into the /app directory
RUN git clone https://github.com/csc510-team5/ClassMateBot.git /app

# Install any needed packages specified in requirements.txt
# RUN python3 -m venv venv
# RUN source venv/bin/activate
RUN pip install -r /app/requirements.txt

# Set the working directory to /app
WORKDIR /app
