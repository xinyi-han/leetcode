-- Three straight lines can form a triangle if the longest line is less than the sum of the two shorter lines.
SELECT x, y, z,
CASE
    WHEN longest = 'x' AND y + z > x THEN 'Yes'
    WHEN longest = 'y' AND x + z > y THEN 'Yes'
    WHEN longest = 'z' AND x + y > z THEN 'Yes'
    ELSE 'No'
END AS triangle
FROM (
    SELECT x, y, z,
    CASE
        WHEN x > y AND x > z THEN 'x'
        WHEN y > x AND y > z THEN 'y'
        ELSE 'z'
    END AS longest
    FROM Triangle
    ) AS Triangle;