-- Create virtual tables over CSVs
CREATE OR REPLACE TABLE raw_touches AS
SELECT * FROM read_csv_auto('data/data_raw/touches.csv');

CREATE OR REPLACE TABLE raw_events AS
SELECT * FROM read_csv_auto('data/data_raw/events.csv');
