# Write your MySQL query statement below
with 

cte1 as (select query_name, 
sum(rating/position) as quality_score,
count(*) as total_count
from Queries
group by query_name),

cte2 as (select query_name, 
count(*) as count_poor_queries
from Queries
where rating < 3
group by query_name)

select c1.query_name, 
coalesce(round((c1.quality_score/c1.total_count), 2), 0.00) as quality, 
coalesce(round((c2.count_poor_queries/c1.total_count)*100, 2), 0.00) as poor_query_percentage
from cte1 as c1 left join cte2 as c2
on c1.query_name = c2.query_name