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
BASE_CVR = 0.028
CTV_LIFT  = 0.012   # if a journey contains CTV, add this to prob of convert

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

# Events: prob depends on whether CTV present
ev_rows = []
cost_map = {"Search":1.6,"Social":1.1,"CTV":3.2,"Display":0.9,"Email":0.25}
for u, g in touches.groupby("user_id"):
    p = BASE_CVR + (CTV_LIFT if (g["channel"]=="CTV").any() else 0.0)
    conv = np.random.rand() < p
    revenue = (np.random.gamma(2.2, 45.0)+25.0) if conv else 0.0
    last = g.sort_values("timestamp").tail(1).iloc[0]
    cost = cost_map.get(last["channel"], 1.0) * (1 + np.random.rand()*0.5)
    ev_rows.append([u, int(conv), revenue, last["channel"], last["campaign"], cost])
events = pd.DataFrame(ev_rows, columns=["user_id","converted","revenue","last_touch_channel","last_touch_campaign","cost"])

touches.to_csv(RAW / "touches.csv", index=False)
events.to_csv(RAW / "events.csv", index=False)
print("✅ Wrote data_raw/touches.csv & events.csv")
