# 📊 Project 3 — Marketing Attribution & Experimentation Toolkit

An end-to-end portfolio project demonstrating **data engineering**, **SQL modelling**, and **business intelligence** skills.  
It uses **Python**, **DuckDB SQL**, and **BI tools (Power BI, Tableau, Excel)** to create a pipeline for marketing analytics.

---

## 🚀 What This Project Does

- 📥 **ETL pipeline**: generate and clean synthetic marketing data (channels, campaigns, conversions, spend, revenue).  
- 🗂 **SQL transforms**: build sessionised, aggregated, and fact/dimension tables in DuckDB.  
- 📊 **Attribution models**: first-touch, last-touch, linear, time-decay.  
- 🧪 **Experimentation**: run A/B test modules (conversion uplift, CAC/ROAS comparisons).  
- 📈 **Interactive dashboards**: track KPIs such as Revenue, Conversions, CAC, ROAS, CVR.  
- 🧑‍💼 **Business framing**: communicate insights into campaign efficiency and channel performance.  

---

## 🧰 Tech Stack

- **Python**: pandas, duckdb  
- **SQL**: transformations and modelling with DuckDB  
- **Power BI Desktop**  
- **Tableau Public**  
- **Excel** (optional recruiter-friendly exports)  

---

## 📁 Repository Structure

```
marketing-attribution-toolkit/
├── README.md                   # Project overview (this file)
├── requirements.txt            # Python dependencies
├── data/
│   ├── raw/                    # initial synthetic datasets
│   ├── processed/              # warehouse.duckdb + transformed tables
│   └── exports/                # CSV/Excel exports for BI
├── outputs/
│   └── screenshots/            # PNGs of dashboards
└── scripts/
    ├── generate_synthetic_data.py   # build synthetic campaign + event data
    ├── run_sql_transforms.py        # apply SQL scripts to create BI-ready tables
    ├── export_for_bi.py             # export clean tables to CSV for BI tools
    ├── attribution.py               # implement attribution models
    └── experiments.py               # run A/B tests and statistical checks
```

---

## ▶️ How to Run

### 1. Create a virtual environment

**Windows PowerShell**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate synthetic data

```bash
python scripts/generate_synthetic_data.py
```

This creates base datasets of user journeys (touchpoints, channels, campaigns, spend, conversions).

### 4. Run SQL transforms

```bash
python scripts/run_sql_transforms.py
```

This builds a `warehouse.duckdb` with fact and dimension tables (sessionised touches, events, channel/campaign summaries).

### 5. Export tables for BI

```bash
python scripts/export_for_bi.py
```

Exports clean CSVs into `data/exports/` for use in **Power BI**, **Tableau**, or **Excel**.

### 6. Build dashboards

#### In **Power BI Desktop**:

- Load the exported CSVs (`touches_sessionised.csv`, `events.csv`, `channel_campaign_summary.csv`).  
- Build visuals:  
  - **KPI cards**: Total Revenue, Conversions, ROAS, CAC, CVR  
  - **Bar chart**: Revenue by channel & campaign  
  - **Line chart**: Revenue or Conversions over time  
  - **Matrix**: Channel × Campaign with conditional formatting  
  - **Slicers**: date, channel, campaign  

#### In **Tableau Public**:

- Connect to the same CSVs.  
- Create worksheets for KPIs, bar charts, and time series.  
- Assemble an interactive dashboard with filters (date, channel, campaign).  

---

## 📊 Example Dashboards

### Power BI
<img width="1515" height="850" alt="powerbi_dashboard" src="https://github.com/user-attachments/assets/b24566e9-b799-4f0c-9f4f-e3075248be23" />

### Tableau 
<img width="1201" height="858" alt="tableau_dashboard" src="https://github.com/user-attachments/assets/6a5cc7c4-1df3-4efd-833f-5608aff05535" />

---

## 🎯 Why This Project Matters

This project shows that you can:  

- Design **realistic marketing KPIs** (CAC, ROAS, CVR).  
- Generate and transform data with **Python + SQL**.  
- Model user journeys and attribution with **data warehouse logic**.  
- Build **interactive dashboards** in **Power BI** and **Tableau**.  
- Present insights in a way that’s relevant to real business stakeholders.  

---

## 🔒 Notes

- `warehouse.duckdb` and large CSV exports are excluded from GitHub.  
- Only scripts, README, and small example exports are committed.    

---

## 📄 Licence

MIT Licence – free to use and adapt.
