create table account(
	user_id serial primary key,
	username varchar(50) unique not null,
	password varchar(50) not null,
	email varchar(250) unique not null,
	created_on timestamp not null,
	last_login timestamp
);

create table job(
	job_id serial primary key,
	job_name varchar(200) unique not null
);

create table account_job(
	user_id integer references account(user_id)
);

create table account_job1(
	user_id integer references account(user_id),
	job_id integer references job(job_id),
	hire_data timestamp
);
select * from account;
insert into account (username,password,email,created_on)values('Jose','Password','jose@email.com',current_timestamp);
insert into job(job_name)values ('Astronaut');
select * from job; --since serial was metioned it take ob_id value by default serially
insert into job(job_name)values ('President');

insert into account_job1(user_id,job_id,hire_data) values (1,1,current_timestamp);
select * from account_job1;
insert into account_job1(user_id,job_id,hire_data) values (10,10,current_timestamp); -- gives error because we said serial thre and according to it should be 2 not 10

insert into job(job_name) values('Data Scientist');
select * from job;
update account set last_login = current_timestamp where last_login is null;
update account set last_login = current_timestamp;
update account set last_login = created_on;
select * from account;
select * from account_job1;
update account_job1 set hire_data = account.created_on from account where account_job1.user_id = account.user_id;
select * from account_job1;