FROM python:3.10-slim

WORKDIR /app

COPY ../../requirements.txt .

RUN python -m pip install --upgrade uv \
  && python -m uv pip install --system -r=requirements.txt 

ENV OTEL_EXPORTER_OTLP_INSECURE=true

COPY src/dice_player/app.py .

EXPOSE 8081

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081"]
