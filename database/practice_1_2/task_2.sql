
--Get info about clients who gave more profit for company
BEGIN;
--CREATE INDEX ON customers(customer_id); no sense
--CREATE INDEX ON cars(car_id); no sense
DROP INDEX customers_customer_id_idx;
EXPLAIN ANALYZE
SELECT customer_id, customer_name, COUNT(*), SUM(orders.rent_period * car_model.price) as sum_orders
FROM customers
INNER JOIN orders USING(customer_id)
INNER JOIN cars USING(car_id)
INNER JOIN car_model USING(model_id)
GROUP BY customer_id, customer_name
ORDER BY sum_orders DESC
LIMIT 20
COMMIT;
ROLLBACK;


--Get information about count cars in each branch

BEGIN;
--CREATE INDEX ON branches(branch_id); no sense
EXPLAIN ANALYZE
SELECT branches.branch_id, branch_name, city, COUNT(*) as count_cars FROM branches
INNER JOIN branches_address  ON branches.branch_id=branches_address.branch_address_id
INNER JOIN cars USING(branch_id)
GROUP BY branches.branch_id, branch_name, city
ORDER BY count_cars DESC
COMMIT;
ROLLBACK;


--Get info about customers who hasn't done orders


SELECT customer_name, order_id FROM customers
LEFT JOIN orders USING(customer_id)
WHERE order_id IS NULL
