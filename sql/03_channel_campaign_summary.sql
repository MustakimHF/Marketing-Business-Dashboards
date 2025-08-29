-- Aggregate performance by channel & campaign
CREATE OR REPLACE TABLE channel_campaign_summary AS
SELECT
  t.channel,
  t.campaign,
  COUNT(*)                         AS touches,
  SUM(e.converted)                 AS conversions,
  SUM(e.revenue)                   AS revenue,
  SUM(e.cost)                      AS cost,
  CASE WHEN SUM(e.cost)=0 THEN NULL
       ELSE SUM(e.revenue)/SUM(e.cost)
  END                              AS roas,
  AVG(e.converted::INT)            AS cvr
FROM touches_sessionised t
JOIN raw_events e USING (user_id)
GROUP BY 1,2
ORDER BY revenue DESC;
