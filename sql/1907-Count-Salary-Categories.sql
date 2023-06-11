SELECT category, MAX(accounts_count) AS accounts_count
FROM (
    SELECT category, COUNT(account_id) AS accounts_count
    FROM (
        SELECT *,
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income > 50000 THEN 'High Salary'
            ELSE 'Average Salary'
        END AS category
        FROM Accounts
        ) AS Accounts
    GROUP BY category
    UNION
    SELECT 'Low Salary', 0
    UNION
    SELECT 'Average Salary', 0
    UNION
    SELECT 'High Salary', 0
    ) AS c
GROUP BY category;