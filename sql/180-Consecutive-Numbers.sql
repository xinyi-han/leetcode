SELECT DISTINCT f.num AS ConsecutiveNums
FROM Logs f
LEFT JOIN Logs s
ON f.id + 1 = s.id
LEFT JOIN Logs t
ON f.id + 2 = t.id
WHERE f.num = s.num
AND f.num = t.num;