# Write your MySQL query statement below
select c1.name as country
from Person
join Country c1
on substring(phone_number,1,3) = country_code
join Calls
on id in (caller_id, callee_id)
group by country
having avg(duration) > (select avg(duration) from Calls)