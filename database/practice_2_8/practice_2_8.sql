--Сравнить цену каждого продукта n с средней ценой продуктов в категории
--продукта n. Использовать window function. Таблица результата должна
--содержать такие колонки: category_title, product_title, price, avg

SELECT category_title, product_title, price,
price - AVG(price) OVER (PARTITION BY products.category_id) as difference
FROM products INNER JOIN categories ON
products.category_id = categories.category_id


--2. Добавить 2 любых триггера и обработчика к ним, использовать транзакции.

--Check that updated date can't be less than created date

CREATE OR REPLACE FUNCTION check_create_update_order()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	IF NEW.updated_at < OLD.created_at THEN
	RAISE EXCEPTION 'The date of updated order is less than date of created. It is impossible';
	END IF;

	RETURN NEW;
END;$$;

DROP TRIGGER validate_date_updated_at;
CREATE TRIGGER validate_date_updated_at
	BEFORE UPDATE
	ON orders
	FOR EACH ROW
	EXECUTE PROCEDURE check_create_update_order();


UPDATE orders SET updated_at = '2018-12-27' WHERE order_id = 2



--Table for statistics. Trigger will count how much time was updated the order.
CREATE TABLE order_statistics
(
    id serial PRIMARY KEY,
	order_id integer NOT NULL,
    updated integer
);


CREATE OR REPLACE FUNCTION check_insert_order()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	INSERT INTO order_statistics(order_id, updated)
		 VALUES(NEW.order_id, 0);
	RETURN NEW;
END;$$;

DROP TRIGGER insert_statistics;
CREATE TRIGGER insert_statistics
	AFTER INSERT
	ON orders
	FOR EACH ROW
	EXECUTE PROCEDURE check_insert_order();


CREATE OR REPLACE FUNCTION check_update_order()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
	UPDATE order_statistics SET updated = updated + 1 WHERE order_id = OLD.order_id;
	RETURN NEW;
END;$$;

DROP TRIGGER update_statistics;
CREATE TRIGGER update_statistics
	AFTER UPDATE
	ON orders
	FOR EACH ROW
	EXECUTE PROCEDURE check_update_order();


INSERT INTO orders(order_id, carts_cart_id, order_status_order_status_id, shipping_total,
total, created_at, updated_at)
VALUES (1501, 1500, 1, 40, 300, '2017-12-06', '2017-12-09');

SELECT * FROM order_statistics;

BEGIN;

UPDATE orders SET updated_at = '2017-12-29' WHERE order_id = 1501;

UPDATE orders SET updated_at = '2017-12-30' WHERE order_id = 1501;

ROLLBACK;
COMMIT;