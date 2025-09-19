# 📊 Project 3 — Marketing & Business Dashboards

A portfolio-ready project using **Power BI**, **Tableau**, and **Excel** to build interactive dashboards for marketing KPIs.  
It demonstrates skills in **data modelling**, **business framing**, **SQL transforms**, and **data storytelling**.

---

## 🚀 What This Project Does

- 📥 **ETL pipeline**: generate clean marketing dataset (channels, campaigns, conversions, spend, revenue).  
- 🗂 **SQL transforms**: structured tables for BI tools (DuckDB).  
- 📊 **KPIs in dashboards**: Revenue, Conversions, CAC, ROAS, CVR.  
- 📈 **Interactive visuals**: Time series, bar charts, segment matrices, and slicers.  
- 🧑‍💼 **Business framing**: marketing performance insights (what’s working, what’s not).  

---

## 🧰 Tech Stack

- **Python**: pandas, duckdb  
- **SQL**: transforms with DuckDB  
- **Power BI Desktop**  
- **Tableau Public**  
- **Excel** (optional export for recruiters)  

---

## 📁 Repository Structure

```
marketing-business-dashboards/
├── README.md                   # Project overview (this file)
├── requirements.txt            # Python dependencies
├── data/
│   ├── raw/                    # initial synthetic or sample datasets
│   ├── processed/              # transformed tables (duckdb)
│   └── exports/                # csv exports for BI
├── outputs/
│   └── screenshots/            # PNGs of dashboards
└── scripts/
    ├── generate_data.py        # build synthetic campaign data
    ├── run_sql_transforms.py   # create BI tables in DuckDB
    ├── export_for_bi.py        # export clean tables to CSV (for Power BI/Tableau)
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

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Generate synthetic marketing data

```bash
python scripts/generate_data.py
```

This will create a base dataset of campaigns, channels, spend, and conversions.

---

### 4. Run SQL transforms in DuckDB

```bash
python scripts/run_sql_transforms.py
```

This builds a `warehouse.duckdb` in `data/processed/` with fact and dimension tables.

---

### 5. Export tables for BI

```bash
python scripts/export_for_bi.py
```

Exports clean CSVs into `data/exports/` for use in **Power BI**, **Tableau**, or **Excel**.

---

### 6. Build dashboards

#### In **Power BI Desktop**:

- Load `data/exports/facts.csv` and `data/exports/dimensions.csv`  
- Build visuals:  
  - **KPI cards**: Total Revenue, Conversions, ROAS, CAC, CVR  
  - **Bar chart**: by channel & campaign  
  - **Line/area**: Revenue or Conversions over time  
  - **Matrix**: Channel × Campaign  
  - **Slicers**: channel, campaign, date range  

#### In **Tableau Public**:

- Connect to the same CSVs  
- Create worksheets for KPIs, bar charts, and time series  
- Assemble an interactive dashboard with filters (channel, campaign, date).  

---

## 📊 Example Dashboard 

![Power BI Dashboard](outputs/screenshots/powerbi_dashboard.png)

![Tableau Dashboard]<img width="1201" height="858" alt="image" src="https://github.com/user-attachments/assets/6a5cc7c4-1df3-4efd-833f-5608aff05535" />

---

## 🎯 Why This Project Matters

This project shows that you can:  

- Design **realistic business KPIs** (CAC, ROAS, CVR).  
- Transform and model data using **SQL + DuckDB**.  
- Build **professional dashboards** in both **Power BI** and **Tableau**.  
- Communicate insights with **clear business framing**.  

---

## 🔒 Notes

- `warehouse.duckdb` and large CSV exports are excluded from GitHub.  
- Only scripts, README, and small exports are committed.    

---

## 📄 Licence

MIT Licence – free to use and adapt.


