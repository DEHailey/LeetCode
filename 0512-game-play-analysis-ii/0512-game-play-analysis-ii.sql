# Write your MySQL query statement below
SELECT player_id, device_id
FROM (
    SELECT player_id, device_id,
           ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date) AS rnk
    FROM Activity
)t
WHERE rnk = 1
