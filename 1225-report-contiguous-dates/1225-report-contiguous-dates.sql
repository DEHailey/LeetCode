# Write your MySQL query statement below
SELECT 'failed' AS period_state, MIN(fail_date) AS start_date, MAX(fail_date) AS end_date
FROM (SELECT fail_date, ROW_NUMBER()OVER() AS rnk
      FROM Failed
      WHERE YEAR(fail_date)=2019)temp
GROUP BY DATE_SUB(fail_date,INTERVAL rnk day)

UNION ALL

SELECT 'succeeded' AS period_state, MIN(success_date) AS start_date, MAX(success_date) AS end_date
FROM (SELECT success_date, ROW_NUMBER() OVER() AS rnk
      FROM Succeeded
      WHERE YEAR(success_date)=2019)temp
GROUP BY DATE_SUB(success_date, INTERVAL rnk day)

ORDER BY start_date;