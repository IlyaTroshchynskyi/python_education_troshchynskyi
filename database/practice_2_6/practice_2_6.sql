--Написать 3 представления для таблицы products, для таблиц order_status и order,
--для таблиц products и category.


CREATE OR REPLACE VIEW view_products AS
SELECT * FROM products;

SELECT * FROM view_products;
DROP VIEW view_products;


CREATE OR REPLACE VIEW order_status_orders AS
SELECT * FROM orders INNER JOIN order_status ON
orders.order_status_order_status_id = order_status.order_status_id
ORDER BY order_status_id ASC;

SELECT * FROM order_status_orders;
DROP VIEW order_status_orders;

CREATE OR REPLACE VIEW products_category AS
SELECT product_title, product_description, price
FROM products INNER JOIN categories ON
products.category_id = categories.category_id;

SELECT * FROM products_category;
DROP VIEW products_category;

--Создать материализированное представление для "тяжелого" запроса на свое усмотрение.
--Не забыть сделать запросы для удаления представлений.
-- Return query where name of persons have the same numbers in names


CREATE MATERIALIZED VIEW users_users AS
SELECT l.first_name, first FROM users l
INNER JOIN (SELECT first_name as first FROM users ) r ON
l.first_name LIKE 'first_name 1%5%';


SELECT * FROM users_users;
DROP MATERIALIZED VIEW users_users;


-- query where total in table carts for each cart != sum of products in this cart
CREATE MATERIALIZED VIEW comparison AS
SELECT first_name, cart_product.carts_cart_id, MAX(total),
SUM(price), COUNT(first_name)
FROM test_users INNER JOIN carts ON
test_users.user_id = carts.users_user_id INNER JOIN cart_product ON
carts.cart_id = cart_product.carts_cart_id INNER JOIN products ON
cart_product.products_product_id = products.product_id
GROUP BY first_name, cart_product.carts_cart_id
HAVING MAX(total) != SUM(price);

SELECT * FROM comparison;
DROP MATERIALIZED VIEW comparison;
DROP VIEW comparison;

--Query where products have been sold using nested query.
CREATE MATERIALIZED VIEW product_sold AS
SELECT product_title FROM products WHERE product_id IN
(SELECT products_product_id FROM cart_product WHERE carts_cart_id IN
(SELECT cart_id FROM carts WHERE cart_id IN
(SELECT carts_cart_id FROM orders WHERE order_status_order_status_id IN
(SELECT order_status_id FROM order_status WHERE status_name='Finished'))));

SELECT * FROM product_sold;
DROP MATERIALIZED VIEW product_sold;