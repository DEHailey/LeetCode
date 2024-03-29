# Write your MySQL query statement below
select Employee.name, Bonus.bonus
from Employee 
left outer join bonus on Employee.empId = Bonus.empId
where bonus < 1000 or bonus is null