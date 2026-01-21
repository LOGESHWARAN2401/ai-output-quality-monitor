import time
import random
import pandas as pd
from datetime import datetime
import os

QUERIES = [
    "What is machine learning?",
    "Explain overfitting",
    "What is data science?",
    "Difference between AI and ML",
    "What is cross validation?"
]

MODELS = ["Model_A", "Model_B"]

def generate_response(query, model):
    start = time.time()

    if model == "Model_A":
        response = f"This is a detailed explanation of {query} with examples."
    else:
        response = f"Short answer: {query}."

    latency = (time.time() - start) * 1000
    cost = round(random.uniform(0.002, 0.01), 4)

    return {
        "query": query,
        "response": response,
        "model": model,
        "timestamp": datetime.now(),
        "latency_ms": latency,
        "cost": cost
    }

def run_logging():
    rows = []
    for q in QUERIES:
        for m in MODELS:
            rows.append(generate_response(q, m))

    os.makedirs("data", exist_ok=True)
    pd.DataFrame(rows).to_csv("data/logs_temp.csv", index=False)

if __name__ == "__main__":
    run_logging()
