# Write your MySQL query statement below

with employee_department as(
    select d.id,
        d.name as Department,
        salary as Salary,
        e.name as Employee,
        DENSE_RANK() OVER(PARTITION BY d.id ORDER BY salary desc) as rnk
    from Department d
    join Employee e
    on d.id = e.departmentId
)
select Department, Employee, Salary
from employee_department
where rnk <= 3
