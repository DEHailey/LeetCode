# Write your MySQL query statement below
select ifnull(e2.unique_id, null) as unique_id, e1.name as name
from Employees e1
left join EmployeeUNI e2
on e1.id = e2.id
