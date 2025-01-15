/*1.	Write a SQL statement to create a simple table countries,
including columns country_id,country_name and region_id which already exist. */
create table countries(
	country_id int unique primary key,
	country_name varchar(100),
	region_id varchar(50)
);

/*2.	Create the two tables Sales and products and insert some sample data into them.
Sales table columns: 
sale_id	product_id	quantity_sold	sale_date	total_price

Products table columns:
product_id	product_name	category	unit_price

Filter the Sales table to show only sales with a total_price greater than $100.
*/

create table product(
	product_id varchar(50) unique primary key,
	product_name varchar(100) not null,
	category varchar(50),
	unit_price float not null
);

create table Sales(
	sale_id SERIAL unique primary key,
	product_id varchar(50) ,
	quantity_sold int not null,
	sale_date date not null,
	total_price float not null,
	FOREIGN KEY (product_id) REFERENCES product(product_id)
);

insert into product (product_id, product_name, category, unit_price) values
('A01', 'Product 1', 'Category A', 10.00),
('A02', 'Product 2', 'Category B', 25.00),
('A03', 'Product 3', 'Category A', 50.00),
('J04', 'Product 4', 'Category C', 75.00),
('A05', 'Product 5', 'Category B', 100.00);
insert into sales (product_id, quantity_sold, sale_date, total_price) values
('A01', 5, '2024-08-01', 50.00),
('A02', 10, '2024-08-02', 250.00),
('A03', 3, '2024-08-03', 150.00),
('J04', 1, '2024-08-04', 75.00),
('A05', 2, '2024-08-05', 200.00);

select * from sales where total_price >100;


/*3.	Retrieve the total_price of all sales, rounding the values to two decimal places.*/
select sale_id,total_price from sales;


/*4.	Calculate the total revenue generated from sales of products in the ‘Electronics’ category.*/
select sum(s.total_price) as total_revenue
from sales s
join product p on s.product_id = p.product_id
where p.category = 'Category A';

/*5.	Retrieve the product_name and category from the Products table, ordering the results by 
category in ascending order.*/

select product_name, category from product order by category;