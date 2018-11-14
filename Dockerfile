# Use an official Python runtime as a parent image
FROM python:3.6.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN jupyter-nbextension install rise --py --sys-prefix && jupyter-nbextension enable rise --py --sys-prefix
# Make port 80 available to the world outside this container
EXPOSE 8888

# Run app.py when the container launches
# --ip='*' --port=8888 --no-browser
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]