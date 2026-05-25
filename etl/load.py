from pathlib import Path

def save_model(df, output_dir: str, name: str = "model.csv"):
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_dir / name, index=False)
