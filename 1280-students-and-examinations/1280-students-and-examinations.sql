# Write your MySQL query statement below
select s.student_id, s.student_name, sub.subject_name, ifnull(temp.attended_exams,0) as attended_exams
from Students s
cross join Subjects sub
left join(
    select student_id, subject_name, count(*) as attended_exams
    from Examinations
    group by student_id, subject_name
) temp
on s.student_id = temp.student_id and sub.subject_name = temp.subject_name
order by student_id, subject_name