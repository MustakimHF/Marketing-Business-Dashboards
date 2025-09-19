#!/usr/bin/env python3
"""
Generate synthetic marketing data:
- data_raw/touches.csv    (multi-touch journeys)
- data_raw/events.csv     (conversions, revenue, channel cost)
"""
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "data_raw"
RAW.mkdir(parents=True, exist_ok=True)

np.random.seed(42)

N_USERS = 6000
CHANNELS = ["Search", "Social", "CTV", "Display", "Email"]
CAMPAIGNS = ["Brand", "Prospecting", "Retargeting"]

BASE_CVR = 0.028          # base conversion rate
CTV_LIFT  = 0.012         # lift if journey contains CTV

# introduce meaningful variance
CAMP_MULT = {"Brand": 1.00, "Prospecting": 0.70, "Retargeting": 1.60}
CHAN_MULT = {"Search": 1.20, "Social": 0.90, "CTV": 1.10, "Display": 0.60, "Email": 1.40}
REV_SCALE = {"Search": 55, "Social": 40, "CTV": 70, "Display": 30, "Email": 45}
COST_BASE = {"Search": 1.8, "Social": 1.3, "CTV": 3.6, "Display": 0.7, "Email": 0.2}

# Touches
rows = []
for u in range(1, N_USERS+1):
    k = np.random.randint(1, 6)  # 1-5 touches
    start = pd.Timestamp("2025-06-01")
    for i in range(k):
        dt = start + pd.Timedelta(days=np.random.randint(0, 60), hours=np.random.randint(0,24))
        ch = np.random.choice(CHANNELS, p=[0.33,0.25,0.12,0.2,0.1])
        camp = np.random.choice(CAMPAIGNS, p=[0.5,0.35,0.15])
        rows.append([u, i+1, dt, ch, camp])

touches = pd.DataFrame(rows, columns=["user_id","touch_order","timestamp","channel","campaign"])
touches = touches.sort_values(["user_id","timestamp"]).reset_index(drop=True)

# Events per user
ev_rows = []
for u, g in touches.groupby("user_id"):
    has_ctv = (g["channel"] == "CTV").any()
    base = BASE_CVR + (CTV_LIFT if has_ctv else 0.0)
    last = g.sort_values("timestamp").iloc[-1]

    p = base * CAMP_MULT.get(last["campaign"], 1.0) * CHAN_MULT.get(last["channel"], 1.0)
    p = np.clip(p, 0.005, 0.25)
    conv = np.random.rand() < p

    revenue = (np.random.gamma(2.2, REV_SCALE[last["channel"]]) + 25.0) if conv else 0.0
    cost = COST_BASE.get(last["channel"], 1.0) * np.random.uniform(0.8, 1.6)

    ev_rows.append([u, int(conv), revenue, last["channel"], last["campaign"], cost])

events = pd.DataFrame(ev_rows, columns=["user_id","converted","revenue","last_touch_channel","last_touch_campaign","cost"])

RAW.mkdir(parents=True, exist_ok=True)
touches.to_csv(RAW / "touches.csv", index=False)
events.to_csv(RAW / "events.csv", index=False)
print("✅ Wrote data_raw/touches.csv & events.csv")
