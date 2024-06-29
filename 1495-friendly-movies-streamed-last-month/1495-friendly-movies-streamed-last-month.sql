# Write your MySQL query statement below
select distinct c.title
from Content c
join TVProgram p
on c.content_id = p.content_id
where c.Kids_content = 'Y'
and c.content_type = 'Movies'
and year(p.program_date) = 2020
and month(p.program_date) = 6