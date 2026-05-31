select distinct email as Email
from Person as p
where (select count(*) from Person where email = p.email) > 1