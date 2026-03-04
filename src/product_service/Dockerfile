# Final image: use lightweight Python
FROM python:latest

WORKDIR /app

COPY main.py /app/
COPY openapi.yaml /app/

RUN  pip3 install --no-cache-dir connexion[uvicorn]

CMD ["python3", "/app/main.py"]
