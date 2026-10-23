FROM python:3.11-slim

# Install I2C tools and smbus2 dependencies
RUN apt-get update && apt-get install -y \
    python3-smbus \
    i2c-tools \
    && pip install flask smbus2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Expose port 8081 for servo API
EXPOSE 8081

CMD ["python", "main.py"]
