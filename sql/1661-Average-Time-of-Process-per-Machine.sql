SELECT machine_id, ROUND(AVG(processing_time), 3) AS processing_time
FROM (
    SELECT s.machine_id, s.process_id, (e.timestamp - s.timestamp) AS processing_time
    FROM Activity s
    INNER JOIN Activity e
    ON s.machine_id = e.machine_id
    AND s.process_id = e.process_id
    WHERE s.activity_type = 'start'
    AND e.activity_type = 'end'
    ) AS Temp
GROUP BY machine_id;
