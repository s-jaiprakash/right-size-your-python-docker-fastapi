FROM python:3.10-slim

WORKDIR /app
COPY benchmark_script.py .
COPY data/orders.csv .
RUN pip install pandas psutil

CMD ["python", "benchmark_script.py"]
