FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ src/
COPY run_workflow.py .
ENTRYPOINT ["python", "run_workflow.py"]
