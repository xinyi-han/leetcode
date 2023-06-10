SELECT p.product_id, p.new_price AS price
FROM Products p
INNER JOIN (
    SELECT product_id, MAX(change_date) AS change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
    ) AS t
ON p.product_id = t.product_id
AND p.change_date = t.change_date
UNION
SELECT p.product_id, 10
FROM Products p
WHERE p.product_id NOT IN (
    SELECT DISTINCT product_id
    FROM Products
    WHERE change_date <= '2019-08-16'
    );