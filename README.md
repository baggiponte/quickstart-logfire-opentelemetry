# Logfire + OpenTelemetry
This project is a proof of concept for using OpenTelemetry in Python. It consists of two services: a dice roller and a
dice player. The dice roller service generates a random number between 1 and 6, simulating the roll of a dice.
The dice player service calls the dice roller service twice, simulates a game where the player wins if the sum of the
two rolls is 7 or 11.

## Launch the service

1. Clone the repository to your local machine.
2. Launch the services using:

```bash
docker compose up --build
```

3. Open the Jaeger GUI on `localhost:16686`
4. Select the `dice_player` in the dropdown:
5. Visit this endpoint: `http://localhost:8081/play`
6. Go back to Jaeger and click on `Find Traces`
