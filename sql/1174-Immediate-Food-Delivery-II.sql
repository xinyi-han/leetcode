SELECT ROUND(SUM(d.order_date = d.customer_pref_delivery_date)/COUNT(d.customer_id)*100, 2) AS immediate_percentage
FROM Delivery d
INNER JOIN (
    SELECT customer_id, MIN(order_date) AS order_date
    FROM Delivery
    GROUP BY customer_id
    ) AS f
ON d.customer_id = f.customer_id
AND d.order_date = f.order_date;