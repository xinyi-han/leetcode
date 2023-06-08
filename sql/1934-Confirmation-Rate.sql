SELECT s.user_id,
CASE
    WHEN c.confirmed > 0 THEN ROUND(c.confirmed/t.total, 2)
    ELSE ROUND(0, 2)
END AS confirmation_rate
FROM Signups s
LEFT JOIN (
    SELECT user_id, COUNT(*) AS confirmed
    FROM Confirmations
    WHERE action = 'confirmed'
    GROUP BY user_id
    ) AS c
ON s.user_id = c.user_id
LEFT JOIN (
    SELECT user_id, COUNT(*) AS total
    FROM Confirmations
    GROUP BY user_id
    ) AS t
ON s.user_id = t.user_id;