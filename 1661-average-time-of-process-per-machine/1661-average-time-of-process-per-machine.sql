# Write your MySQL query statement below
SELECT 
    machine_id, 
    ROUND(SUM(CASE WHEN activity_type='start' THEN timestamp*-1 ELSE timestamp end) / COUNT(DISTINCT process_id),3) as processing_time
FROM Activity
GROUP BY machine_id

