SELECT r.contest_id, ROUND(COUNT(r.contest_id)/u.num*100, 2) AS percentage
FROM Register r
JOIN (
    SELECT COUNT(*) AS num
    FROM Users
    ) AS u
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;