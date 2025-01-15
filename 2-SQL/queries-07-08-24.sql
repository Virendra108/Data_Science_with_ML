/*CHALLENGE 1:- 
to give platinum to customers having payments 40 or more tha it */
select customer_id,count(*) from payment group by customer_id having count(*)>=40;

/*CHALLENGE 2:-
customer id having spent $100 or  more with staff_id member 2 */
select customer_id, sum(amount) from payment where staff_id=2 group by customer_id having sum(amount)>100;

select amount as rental_price from payment;
select sum(amount)as net_revenue from payment;
select count(amount)as num_trasactions from payment;
select count(*)as num_trasaction from payment;
select customer_id,sum(amount)from payment group by customer_id;
select customer_id,sum(amount)as total_spent from payment group by customer_id;
select customer_id,sum(amount)from payment group by customer_id having sum(amount)>100;
select customer_id,sum(amount)as total_spent from payment group by customer_id;
select customer_id,sum(amount)as total_spent from payment group by customer_id having total_spent>100; /*error*/
select customer_id,amount from payment where amount>2;
select customer_id,amount as new_name from payment where new_name>2;/*error*/


select * from payment;
select * from customer;
select payment.payment_id,payment.customer_id,customer.first_name from payment inner join customer on payment.customer_id=customer.customer_id;

select payment.payment_id,payment.customer_id,customer.first_name from customer inner join payment on payment.customer_id=customer.customer_id;

select * from customer full outer join payment on customer.customer_id=payment.customer_id;


select * from film;
select * from inventory;
select film.film_id,film.title,inventory.inventory_id from film left join inventory on inventory.film_id=film.film_id;
select film.film_id,film.title,inventory.inventory_id,inventory.store_id from film left join inventory on inventory.film_id=film.film_id;
select film.film_id,film.title,inventory.inventory_id,inventory.store_id from film left join inventory on inventory.film_id=film.film_id where inventory.film_id is null;

select film.film_id,film.title,inventory.inventory_id,inventory.store_id from film right join inventory on inventory.film_id=film.film_id;
select film.film_id,film.title,inventory.inventory_id,inventory.store_id from inventory right join film on inventory.film_id=film.film_id;
select film.film_id,film.title,inventory.inventory_id,inventory.store_id from film right join inventory on inventory.film_id=film.film_id where inventory.film_id is null;
