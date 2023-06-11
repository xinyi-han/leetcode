SELECT DISTINCT c1.visited_on, SUM(c2.amount) AS amount, ROUND(SUM(c2.amount)/7, 2) AS average_amount
FROM Customer c1
INNER JOIN Customer c2
ON DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6
GROUP BY c1.visited_on, c1.customer_id
HAVING COUNT(DISTINCT c2.visited_on) >= 7
ORDER BY c1.visited_on;