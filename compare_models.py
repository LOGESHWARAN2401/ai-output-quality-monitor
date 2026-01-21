from src.metrics import response_length, uncertainty_flag

def compare(df):
    df["length"] = df["response"].apply(response_length)
    df["uncertainty"] = df["response"].apply(uncertainty_flag)

    return df.groupby("model").agg({
        "length": "mean",
        "latency_ms": "mean",
        "cost": "mean",
        "uncertainty": "mean"
    }).reset_index()
