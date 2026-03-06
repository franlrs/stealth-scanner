FROM python:3.11-slim

# Install system dependencies required for low-level network packet manipulation [cite: 2]
RUN apt-get update && apt-get install -y libpcap-dev tcpdump && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt [cite: 3]

# Copy project files
COPY . .

# Default command
CMD ["python", "scanner.py"]