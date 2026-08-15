# Write your MySQL query statement below
select *, if(z < x+y and z > abs(x-y), "Yes", "No") as triangle
from Triangle
