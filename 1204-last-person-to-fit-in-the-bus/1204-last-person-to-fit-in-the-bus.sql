# Write your MySQL query statement below

WITH SortedQueue AS (
    SELECT 
        person_name, 
        turn, 
        weight,
        SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM 
        Queue
)
SELECT 
    person_name
FROM 
    SortedQueue
WHERE 
    cumulative_weight <= 1000
ORDER BY 
    turn DESC
LIMIT 1;
