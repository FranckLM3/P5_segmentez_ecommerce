# Use python as base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Use working directory /app/model
WORKDIR /api

# Copy all the content of current directory to working directory
COPY ./api /api

# Copy and install required packages
COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Set env variables for Cloud Run
ENV PORT 80
ENV HOST 0.0.0.0

EXPOSE 80:80

# Run flask app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]