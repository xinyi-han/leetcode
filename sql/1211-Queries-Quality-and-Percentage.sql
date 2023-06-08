SELECT DISTINCT Queries.query_name, ROUND(q.quality/n.num, 2) AS quality, ROUND(IFNULL(p.poor, 0)/n.num*100, 2) AS poor_query_percentage
FROM Queries
LEFT JOIN (
    SELECT query_name, SUM(rating/position) AS quality
    FROM Queries
    GROUP BY query_name
    ) AS q
ON Queries.query_name = q.query_name
LEFT JOIN (
    SELECT query_name, COUNT(rating) AS poor
    FROM Queries
    WHERE rating < 3
    GROUP BY query_name
    ) AS p
ON Queries.query_name = p. query_name
LEFT JOIN (
    SELECT query_name, COUNT(rating) AS num
    FROM Queries
    GROUP BY query_name
    ) AS n
ON Queries.query_name = n.query_name;