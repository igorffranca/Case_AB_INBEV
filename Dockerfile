# Use an official Apache Spark image as the base
FROM bitnami/spark:3.5.5

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script into the container
COPY etl/ etl/
COPY main.py .

# Command to run the script
CMD ["spark-submit", "--master", "local[*]", "main.py"]