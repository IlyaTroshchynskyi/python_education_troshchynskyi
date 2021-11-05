Get the number of users by city
DROP VIEW count_clients_by_city;
CREATE OR REPLACE VIEW count_clients_by_city AS
SELECT city, COUNT(*) FROM customers
INNER JOIN customers_address ON customers.address_id = customers_address.customers_address_id
GROUP BY city


Get price range statistics
DROP VIEW statistic_by_price;
CREATE OR REPLACE VIEW statistic_by_price AS
SELECT SUM(CASE WHEN price < 30 THEN 1 ELSE 0 END) as range_less_30,
SUM(CASE WHEN price >= 30 AND price < 60 THEN 1 ELSE 0 END),
SUM(CASE WHEN price >= 60 THEN 1 ELSE 0 END) as range_more_60  FROM car_model
INNER JOIN cars USING (model_id)



--GET all data from database
DROP MATERIALIZED VIEW all_data;
CREATE MATERIALIZED VIEW all_data AS
SELECT customers.*, orders.date_rent, orders.rent_period, cars.car_number, car_model.model,
car_model.price, branches.branch_name, branches.telephone, branches_address.city as city_branch,
branches_address.street_name as street_branch,
branches_address.street_number as branch_street_number,
customers_address.city, customers_address.street_name, customers_address.street_number FROM customers
INNER JOIN orders  USING(customer_id)
INNER JOIN cars  USING(car_id)
INNER JOIN car_model  USING(model_id)
INNER JOIN branches  USING(branch_id)
INNER JOIN branches_address  ON branches.branch_id=branches_address.branch_address_id
INNER JOIN customers_address  ON customers.address_id = customers_address.customers_address_id