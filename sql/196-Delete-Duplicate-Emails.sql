DELETE FROM Person
WHERE id NOT IN (
    SELECT *
    FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
        ) AS t
    );

-- You can't specify target table 'Person' for update in FROM clause
--DELETE FROM Person
--WHERE id NOT IN (
--    SELECT MIN(id) AS id
--    FROM Person
--    GROUP BY email
--    );