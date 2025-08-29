-- Order touches and derive simple session index per user
CREATE OR REPLACE TABLE touches_sessionised AS
SELECT
  user_id,
  touch_order,
  CAST(timestamp AS TIMESTAMP) AS ts,
  channel,
  campaign,
  ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY timestamp) AS session_idx
FROM raw_touches;
