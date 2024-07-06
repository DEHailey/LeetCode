# Write your MySQL query statement below
select project_id, employee_id
from (
    select 
        p.project_id, 
        p.employee_id,
        rank() over(partition by project_id order by experience_years desc) as rnk
    from Project p
    join Employee e
    on p.employee_id = e.employee_id
) temp
where rnk = 1
