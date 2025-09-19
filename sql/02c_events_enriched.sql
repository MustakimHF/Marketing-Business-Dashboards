-- Attach conversion_ts to events
CREATE OR REPLACE TABLE events_enriched AS
SELECT
  e.*,
  lt.conversion_ts
FROM raw_events e
LEFT JOIN last_touch_ts lt USING (user_id);


