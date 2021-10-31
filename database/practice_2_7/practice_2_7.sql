--1. Создать функцию, которая сетит shipping_total = 0 в таблице order,
-- если город юзера равен x. Использовать IF clause.


create or replace function set_shipping_total_zero(
   city_name varchar
)
returns void
language plpgsql
as $$
declare
    row_order record;
begin
    for row_order in
		(SELECT * FROM users
		INNER JOIN carts ON users.user_id = carts.users_user_id
		INNER JOIN orders ON carts.cart_id = orders.carts_cart_id
		)
	loop
    if row_order.city = city_name then
        UPDATE orders SET shipping_total = 0 WHERE carts_cart_id IN
			(
				SELECT cart_id FROM users
				INNER JOIN carts ON users.user_id = carts.users_user_id
				WHERE city = city_name
			);
    end if;
	end loop;
end;$$;


SELECT * FROM set_shipping_total_zero('city 18');

SELECT city, shipping_total FROM users
		INNER JOIN carts ON users.user_id = carts.users_user_id
		INNER JOIN orders ON carts.cart_id = orders.carts_cart_id
		WHERE city = 'city 18'
drop function if exists set_shipping_total_zero;


--2. Написать 2 любые хранимые процедуры с использованием условий, циклов и транзакций.

--update price no more than 30 grn
create or replace procedure increase_product_price(
	start_id int,
	end_id int,
    ratio float
)
language plpgsql
as $$
declare
    new_price float;
	old_price float;
begin
	for counter in start_id..end_id
	loop
	SELECT price into old_price FROM products WHERE product_id = counter;
	UPDATE products SET price = price * ratio WHERE
	product_id = counter
	returning price
    into new_price;
	if new_price - old_price < 30 then
		commit;
	else
		rollback;

	end if;
	end loop;
end;$$;


call increase_product_price(1, 5, 1.3);
drop procedure increase_product_price;
SELECT product_title, price FROM products
WHERE product_id < 6;



create or replace procedure update_product_title(
	prod_id integer,
	new_prod_title varchar)
language plpgsql
as $$
declare
	new_product_title varchar;
begin
	UPDATE products SET product_title = new_prod_title
	WHERE product_id = prod_id;

	SELECT product_title into new_product_title FROM products
	WHERE product_id = prod_id;
	if LENGTH(new_product_title) > 20 then
		rollback;
	end if;
end;$$;

call update_product_title(1, 'dasfasdcascasdasfasdfasdasfasdfsadfasf');
drop procedure update_product_title;
SELECT product_title FROM products WHERE product_id = 1;