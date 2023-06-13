SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary
FROM Employee e1
INNER JOIN Department d
ON e1.departmentId = d.id
LEFT JOIN Employee e2
ON e1.salary < e2.salary
AND e1.departmentId = e2.departmentId
GROUP BY e1.id
HAVING COUNT(DISTINCT e2.salary) < 3;

-- Time Limit Exceeded
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
INNER JOIN Department d
ON e.departmentId = d.id
WHERE (e.salary, e.departmentId) IN (
    (SELECT MAX(salary) AS salary, departmentId
    FROM Employee
    GROUP BY departmentId)
    UNION
    (SELECT MAX(salary) AS salary, departmentId
    FROM Employee
    WHERE (salary, departmentId) NOT IN (
        SELECT MAX(salary) AS salary, departmentId
        FROM Employee
        GROUP BY departmentId
        )
    GROUP BY departmentId)
    UNION
    (SELECT MAX(salary) AS salary, departmentId
    FROM Employee
    WHERE (salary, departmentId) NOT IN (
        (SELECT MAX(salary) AS salary, departmentId
        FROM Employee
        GROUP BY departmentId)
        UNION
        (SELECT MAX(salary) AS salary, departmentId
        FROM Employee
        WHERE (salary, departmentId) NOT IN (
            SELECT MAX(salary) AS salary, departmentId
            FROM Employee
            GROUP BY departmentId
            )
        GROUP BY departmentId)
        )
    GROUP BY departmentId)
    );