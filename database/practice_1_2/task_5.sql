create or replace procedure update_date_rent(
	order_id_input integer,
	date_rent_input TIMESTAMP(2))
language plpgsql
as $$
declare
	new_date_rent TIMESTAMP(2);
begin
	UPDATE orders SET date_rent = date_rent_input
	WHERE order_id = order_id_input;

	SELECT date_rent into new_date_rent FROM orders
	WHERE order_id = order_id_input;
	if new_date_rent > now() then
		commit;
	else
		rollback;
	end if;
end;$$;


call update_date_rent(1, '2021-11-04');
drop procedure update_date_rent;
SELECT date_rent FROM orders WHERE order_id = 1;



--Check if car is free and then  add to database
create or replace procedure check_if_car_free(
    date_rent_input TIMESTAMP(2),
	rent_period_input integer,
	car_id_input integer,
	customer_id_input integer)

language plpgsql
as $$
declare
	new_date_rent  TIMESTAMP(2);
begin

    SELECT date_rent into new_date_rent FROM orders
	WHERE date_rent=date_rent_input AND
	car_id=car_id_input;

    if not found then
	INSERT INTO orders (date_rent, rent_period, car_id, customer_id)
	VALUES (date_rent_input, rent_period_input, car_id_input, customer_id_input);
		commit;
	else
		raise 'The date % is not available for car_id %', date_rent_input, car_id_input;
	    rollback;
	end if;
end;$$;

call check_if_car_free('2021-11-05', 1, 1, 1);
drop procedure check_if_car_free;
SELECT * FROM orders ORDER BY order_id DESC LIMIT 1;