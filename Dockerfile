FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ src/
COPY run_workflow.py .
RUN useradd -m -u 1000 devforge && chown -R devforge:devforge /app
USER devforge
ENTRYPOINT ["python", "run_workflow.py"]
