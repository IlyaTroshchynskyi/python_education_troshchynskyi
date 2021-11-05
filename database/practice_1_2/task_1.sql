DROP TABLE car_model;
CREATE TABLE car_model
(
    model_id serial PRIMARY KEY,
    model VARCHAR(100),
    price float
);


do $$
begin
   for counter in 1..50001 loop
	INSERT INTO car_model (model, price) SELECT 'BMW' || counter, ROUND(random() * 100);
   end loop;
end; $$;

SELECT * FROM car_model;

DROP TABLE branches_address;
CREATE TABLE branches_address
(
    branch_address_id serial PRIMARY KEY,
    city VARCHAR(100),
    street_name VARCHAR(255),
    street_number VARCHAR(20)
);

do $$
begin
   for counter in 1..21 loop
	INSERT INTO branches_address (city, street_name, street_number)
	SELECT CASE (RANDOM() * 8)::INT
      WHEN 0 THEN 'Kiev'
      WHEN 1 THEN 'Kharkiv'
      WHEN 2 THEN 'Odessa'
      WHEN 3 THEN 'Dnipro'
      WHEN 4 THEN 'Lviv'
      WHEN 5 THEN 'Poltava'
      WHEN 6 THEN 'Krivoy Rog'
      WHEN 7 THEN 'Kherson'
      WHEN 8 THEN 'Nikopol'
    END, 'Street ' || ROUND(random() * 1000),  ROUND(random() * 1000);
   end loop;
end; $$;

SELECT * FROM branches_address;

DROP TABLE branches;
CREATE TABLE branches
(
    branch_id serial PRIMARY KEY,
    branch_name VARCHAR(100),
    telephone VARCHAR(20),
    address_id integer REFERENCES branches_address (branch_address_id)
);


do $$
begin
   for counter in 1..21 loop
	INSERT INTO branches (branch_name, telephone, address_id)
	SELECT
 'Branch_name ' || ROUND(random() * 1000),
 CASE (RANDOM() * 6)::INT
      WHEN 0 THEN '066'
      WHEN 1 THEN '067'
      WHEN 2 THEN '099'
      WHEN 3 THEN '093'
      WHEN 4 THEN '097'
      WHEN 5 THEN '098'
      WHEN 6 THEN '063'
    END  || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT ||
    (RANDOM() * 9)::INT || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT, counter;
   end loop;
end; $$;



SELECT * FROM branches;



DROP TABLE cars;
CREATE TABLE cars
(
    car_id serial PRIMARY KEY,
    car_number VARCHAR(15),
    model_id integer REFERENCES car_model (model_id),
    branch_id integer REFERENCES branches (branch_id)
);


do $$
begin
   for counter in 1..100001 loop
	INSERT INTO cars (car_number, model_id, branch_id)
	SELECT  'AX' || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT
	 || (RANDOM() * 9)::INT, (RANDOM() * 49999+1)::INT, (RANDOM() * 19+1)::INT;
   end loop;
end; $$;

SELECT * FROM cars;



DROP TABLE customers_address;
CREATE TABLE customers_address
(
    customers_address_id serial PRIMARY KEY,
    city VARCHAR(100),
    street_name VARCHAR(255),
    street_number VARCHAR(20)
);


do $$
begin
   for counter in 1..500001 loop
	INSERT INTO customers_address (city, street_name, street_number)
	SELECT CASE (RANDOM() * 8)::INT
      WHEN 0 THEN 'Kiev'
      WHEN 1 THEN 'Kharkiv'
      WHEN 2 THEN 'Odessa'
      WHEN 3 THEN 'Dnipro'
      WHEN 4 THEN 'Lviv'
      WHEN 5 THEN 'Poltava'
      WHEN 6 THEN 'Krivoy Rog'
      WHEN 7 THEN 'Kherson'
      WHEN 8 THEN 'Nikopol'
    END, 'Street ' || ROUND(random() * 10000),  ROUND(random() * 10000);
   end loop;
end; $$;


SELECT * FROM customers_address;





DROP TABLE customers;
CREATE TABLE customers
(
    customer_id serial PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_telephone VARCHAR(20),
    address_id integer REFERENCES customers_address (customers_address_id)
);

do $$
begin
   for counter in 1..500001 loop
	INSERT INTO customers (customer_name, customer_telephone, address_id)
	SELECT  'Petr ' || counter,
      CASE (RANDOM() * 6)::INT
      WHEN 0 THEN '066'
      WHEN 1 THEN '067'
      WHEN 2 THEN '099'
      WHEN 3 THEN '093'
      WHEN 4 THEN '097'
      WHEN 5 THEN '098'
      WHEN 6 THEN '063'
    END  || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT ||
    (RANDOM() * 9)::INT || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT || (RANDOM() * 9)::INT,
     (RANDOM() * 499999+1)::INT;
   end loop;
end; $$;




DROP TABLE orders;
CREATE TABLE orders
(
    order_id serial PRIMARY KEY,
    date_rent TIMESTAMP(2) NOT NULL,
    rent_period integer NOT NULL,
    car_id integer REFERENCES cars (car_id),
    customer_id integer REFERENCES customers (customer_id)
);

do $$
begin
   for counter in 1..1000001 loop
	INSERT INTO orders (date_rent, rent_period, car_id, customer_id)
	SELECT TO_TIMESTAMP(CASE (RANDOM() * 3)::INT WHEN 0 THEN '2017' WHEN 1 THEN '2018'
      WHEN 2 THEN '2019'
      WHEN 3 THEN '2020' END  || '-' || (RANDOM() * 12)::INT || '-' || (RANDOM() * 28)::INT, 'YYYY-MM-DD'),
    (RANDOM() * 30)::INT, (RANDOM() * 99999 +1)::INT, (RANDOM() * 499999+1)::INT;
   end loop;
end; $$;

SELECT * FROM orders;