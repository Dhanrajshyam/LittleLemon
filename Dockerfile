# ---------- STAGE 1: Builder ----------

# Base image: Python 3.13 slim version for a minimal footprint
FROM python:3.13-slim AS builder

# Set working directory for all subsequent commands
WORKDIR /app

# Python environment variables:
# Prevents Python from writing .pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures Python output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1

# Install system dependencies:
# libpq-dev: Required for psycopg2 (PostgreSQL adapter)
# gcc: Required for compiling some Python packages
# Upgrade pip to latest version
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --upgrade pip

# Copy requirements file first to leverage Docker cache
COPY requirements.txt .
# Install Python dependencies without storing pip cache
RUN pip install --user --no-cache-dir -r requirements.txt

# ---------- STAGE 2: Final image ----------
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
    
WORKDIR /app
    
# Add only necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
    
# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
    
# Copy only needed files
COPY . .

# Document that the container listens on port 8000
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x  /app/entrypoint.prod.sh

# Set the entrypoint script as the default command
# This will run migrations, collect static files, and start Gunicorn
CMD ["/app/entrypoint.prod.sh"]

# -----------Health Check------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD curl --fail http://localhost:8000/health/ || exit 1

# Readme
# Let's examine the key components of this Dockerfile:

#     The FROM instruction selects a minimal Python base image that includes only essential components needed to run Python applications.
    
#     WORKDIR /app establishes the working directory inside the container where all subsequent commands will execute.
    
#     The environment variables set by ENV statements optimize Python's behavior in containers:
    
#     PYTHONDONTWRITEBYTECODE=1 prevents Python from creating .pyc files
#     PYTHONUNBUFFERED=1 ensures Python output is sent directly to the terminal without buffering.
#     RUN pip install --upgrade pip ensures we have the latest version of pip for package installation.
    
#     The system dependencies installation combines two commands to minimize layers. Here, libpq-dev is required for PostgreSQL support through psycopg2, while gcc is needed to compile certain Python packages.
    
#     COPY requirements.txt . copies just the requirements file first, allowing Docker to cache the dependency installation layer.
    
#     RUN pip install --no-cache-dir -r requirements.txt installs all Python dependencies without storing pip's cache.
    
#     COPY . . copies all remaining application code into the container after dependencies are installed.
    
#     EXPOSE 8000 documents that the container listens on port 8000, though this is primarily for documentation purposes.
    
#     Finally, RUN chmod +x /app/entrypoint.prod.sh makes the entrypoint script executable, and CMD ["/app/entrypoint.prod.sh"] sets it as the default command when the container starts.
    
#     With the Dockerfile complete, you're ready to build your Docker image in the next step.