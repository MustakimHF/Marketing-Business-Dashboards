#!/usr/bin/env python3
"""
Creates a single Excel file with all BI tabs to speed up Tableau/Power BI import.
"""
from pathlib import Path
import duckdb, pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB   = ROOT / "data" / "data_processed" / "warehouse.duckdb"
XLSX = ROOT / "exports" / "excel" / "marketing_export.xlsx"
XLSX.parent.mkdir(parents=True, exist_ok=True)

con = duckdb.connect(str(DB))
tabs = {
    "touches_sessionised": con.execute("SELECT * FROM touches_sessionised").fetchdf(),
    "events":              con.execute("SELECT * FROM raw_events").fetchdf(),
    "channel_campaign_summary": con.execute("SELECT * FROM channel_campaign_summary").fetchdf()
}
with pd.ExcelWriter(XLSX, engine="openpyxl") as xw:
    for name, df in tabs.items():
        df.to_excel(xw, sheet_name=name[:31], index=False)

con.close()
print(f"📘 Wrote {XLSX}")
