import time
from opentelemetry import trace
from random import randint, uniform


tracer = trace.get_tracer("diceroller.tracer")


def roll():
    with tracer.start_as_current_span("roll_dice_call"):
        time.sleep(uniform(0, 1))
        return randint(1, 6)