# Write your MySQL query statement below
select distinct b.name as Department, a.name as Employee, a.salary as Salary 
from Employee as a join Department as b
on a.departmentID = b.id
where a.salary = (select max(salary) from Employee where departmentId = a.departmentId)
