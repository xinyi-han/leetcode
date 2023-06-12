SELECT rid as id, COUNT(DISTINCT aid) AS num
FROM (
    SELECT requester_id as rid, accepter_id as aid
    FROM RequestAccepted
    UNION
    SELECT accepter_id as rid, requester_id as aid
    FROM RequestAccepted
    ) AS RequestAccepted
GROUP BY id
ORDER BY num DESC
LIMIT 1;