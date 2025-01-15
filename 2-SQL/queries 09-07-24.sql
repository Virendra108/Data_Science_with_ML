select *from customer;
select * from address inner join customer on address.address_id = customer.address_id where district='california';
select district,email from address inner join customer on address.address_id = customer.address_id where district='california';

/* a customer walks in and huge fan of actoe 'nick wahlberg' and wants know in which movies he is */
select * from film;
select * from actor;
select * from film_actor;
select * from actor inner join film_actor on actor.actor_id=film_actor.actor_id;
select * from actor inner join film_actor on actor.actor_id=film_actor.actor_id inner join film on film_actor.film_id = film.film_id;
select title,first_name,last_name from actor inner join film_actor on actor.actor_id=film_actor.actor_id inner join film on film_actor.film_id = film.film_id;
select title,first_name,last_name from actor inner join film_actor on actor.actor_id=film_actor.actor_id inner join film on film_actor.film_id = film.film_id where first_name='Nick' and last_name='Wahlberg';


select * from payment;