FROM python:3.13-slim

WORKDIR /app

# Copy project files
# Firt `.` means to get the files from the current (root) directory and second `.` means to copy them to the working directory (`/app`) of the container
COPY . .

# Install uv package manager
RUN pip install uv

# Sync dependencies from lock file
RUN uv sync

# Expose port
EXPOSE 8000

# Run the application, host is domain and exposed port is route
CMD ["uv", "run", "fastapi", "dev", "main.py", "--host", "0.0.0.0"]
