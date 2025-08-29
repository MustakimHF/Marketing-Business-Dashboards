#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
raw_t = pd.read_csv(ROOT / "data" / "data_raw" / "touches.csv")
raw_e = pd.read_csv(ROOT / "data" / "data_raw" / "events.csv")

print("touches:", raw_t.shape, "events:", raw_e.shape)
print("top channels:", raw_t['channel'].value_counts().head(5).to_dict())
print("conversion rate:", raw_e['converted'].mean())
