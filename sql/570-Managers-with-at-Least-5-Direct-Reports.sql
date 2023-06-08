SELECT m.name
FROM Employee e
-- LEFT JOIN Employee m
INNER JOIN Employee m
ON e.managerId = m.id
GROUP BY m.id
HAVING COUNT(e.id) >= 5;