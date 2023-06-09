SELECT ROUND(COUNT(s.event_date)/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM Activity a
LEFT JOIN (
    SELECT player_id, ADDDATE(MIN(event_date), INTERVAL 1 DAY) AS event_date
    FROM Activity
    GROUP BY player_id
    ) AS s
ON a.player_id = s.player_id
AND a.event_date = s.event_date;