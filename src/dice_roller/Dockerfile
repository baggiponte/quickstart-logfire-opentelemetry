FROM python:3.10-slim

WORKDIR /app

COPY ../../requirements.txt .

RUN python -m pip install --upgrade uv \
  && python -m uv pip install --system -r=requirements.txt

ENV OTEL_EXPORTER_OTLP_INSECURE=true

COPY src/dice_roller/app.py .
COPY src/dice_roller/roll.py .

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
