import pandas as pd
from compare_models import compare

def generate_report():
    df = pd.read_csv("data/logs.csv")
    summary = compare(df)

    best = df.sort_values("length", ascending=False).head(5)
    worst = df.sort_values("length", ascending=True).head(5)

    with open("reports/evaluation_report.md", "w") as f:
        f.write("# AI Output Quality Evaluation Report\n\n")
        f.write("## Model Comparison Summary\n")
        f.write(summary.to_markdown(index=False))
        f.write("\n\n## Top 5 Best Responses\n")
        f.write(best[["query","model","response"]].to_markdown(index=False))
        f.write("\n\n## Top 5 Worst Responses\n")
        f.write(worst[["query","model","response"]].to_markdown(index=False))

if __name__ == "__main__":
    generate_report()
