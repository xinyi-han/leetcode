SELECT *
FROM (
    SELECT s1.id,
    CASE
        WHEN s2.id IS NOT NULL THEN s2.student
        ELSE s1.student
    END AS student
    FROM Seat s1
    LEFT JOIN Seat s2
    ON s1.id + 1 = s2.id
    WHERE s1.id % 2 = 1
    UNION
    SELECT s1.id, s2.student
    FROM Seat s1
    INNER JOIN Seat s2
    ON s1.id - 1 = s2.id
    WHERE s1.id % 2 = 0
    ) AS Seat
ORDER BY id;