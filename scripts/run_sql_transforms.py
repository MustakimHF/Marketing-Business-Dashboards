#!/usr/bin/env python3
"""
Runs DuckDB SQL files to build processed tables into warehouse.duckdb,
then exports clean BI-ready CSVs.
"""
from pathlib import Path
import duckdb
import pandas as pd  # only for export

ROOT = Path(__file__).resolve().parents[1]
SQL  = ROOT / "sql"
DB   = ROOT / "data" / "data_processed" / "warehouse.duckdb"
DB.parent.mkdir(parents=True, exist_ok=True)

con = duckdb.connect(str(DB))

for name in [
    "01_create_tables.sql",
    "02_sessionise.sql",
    "02b_last_touch_ts.sql",
    "02c_events_enriched.sql",
    "03_channel_campaign_summary.sql"
]:
    q = (SQL / name).read_text(encoding="utf-8")
    con.execute(q)
    print(f"✅ Ran {name}")

# Export BI tables as CSVs
EXPORT = ROOT / "exports" / "csv"
EXPORT.mkdir(parents=True, exist_ok=True)

tables = {
    "touches_sessionised": "touches_sessionised.csv",
    "events_enriched":     "events.csv",  # keeps the same filename for Power BI
    "channel_campaign_summary": "channel_campaign_summary.csv",
}
for tbl, out in tables.items():
    df = con.execute(f"SELECT * FROM {tbl}").fetchdf()
    df.to_csv(EXPORT / out, index=False)
    print(f"💾 Exported {tbl} → exports/csv/{out}")

con.close()
print(f"🏁 DuckDB at {DB}")
