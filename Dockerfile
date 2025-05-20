# 1. Select base image from which we build the container
# FROM python:3.11.9-slim-buster
FROM python:3.11.9

# 2. Set environment variables both at build and at run time
# In this case, we make sure Python output is visible in Docker logs.
ENV PYTHONBUFFERED=1

# 3. Copy application code into the container
COPY . /app

# 4. Set working directory from now on (like cd ...)
WORKDIR /app

# 5. Install python dependencies
RUN python3 -m pip install -r requirements.txt

# 6. Set defautl command when container starts
# In this case, we run our "main.py" script.
ENTRYPOINT ["python3", "main.py"]