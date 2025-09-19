-- Derive a per-user "conversion timestamp" = last touch time
CREATE OR REPLACE TABLE last_touch_ts AS
SELECT
  user_id,
  MAX(ts) AS conversion_ts
FROM touches_sessionised
GROUP BY 1;
