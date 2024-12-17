# Base Image
FROM python:3.11-slim

# Set Working Directory
WORKDIR /app

# Copy Project Files
COPY . .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Port
EXPOSE 5000

# Run Flask Application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
