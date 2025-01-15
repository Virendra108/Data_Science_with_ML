-10-07-2024
select * from customer;
select customer_id from customer;
select customer_id,
case
	when (customer_id<=100)then 'Premium'
	when (customer_id between 100 and 200)then 'Plus'
	else 'Normal'
END
from customer;

select customer_id,
case
	when (customer_id<=100)then 'Premium'
	when (customer_id between 100 and 200)then 'Plus'
	else 'Normal'
END as customer_class
from customer;

select customer_id,
case customer_id
	when 2 then 'winner'
	when 5 then 'second place'
	else 'Normal'
END as raffle_results
from customer;

select * from film;
select rental_rate from film;

select rental_rate,
case rental_rate
	when 0.99 then 1
	when 2.99 then 3
	when 4.99 then 5
END as round_off
from film;

select
sum(case rental_rate
		when 0.99 then 1
		else 0
	end)as number_of_bargains
from film;