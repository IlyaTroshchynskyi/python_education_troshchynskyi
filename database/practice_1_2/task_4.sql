--Return all clients from certain city and street

create or replace function customers_by_address (
	city_input varchar,
	street_name_input varchar
)
returns table (
	city varchar,
	street_name varchar,
	customer_name varchar
)
language plpgsql
as $$
declare
    rec record;
begin
	for rec in (

	    SELECT * FROM customers
        INNER JOIN customers_address ON customers.address_id = customers_address.customers_address_id
        WHERE customers_address.city = city_input AND customers_address.street_name = street_name_input
        ) loop
        customer_name := rec.customer_name;
        city := rec.city;
		street_name := rec.street_name;
        return next;
	end loop;
end; $$;

SELECT * FROM customers_by_address('Poltava', 'Street 8781');






create or replace function get_most_popular_date(input_year integer)
   returns text as $$
declare
	 output_ text default '';
	 rec  record;
	 popular_date cursor(p_year integer)
		 for select date_rent, COUNT(*) as c
		 from orders
		 where EXTRACT(YEAR FROM date_rent) = input_year
		 GROUP BY date_rent ORDER BY c DESC
		 LIMIT 1;
begin
   open popular_date(input_year);
   output_ := 'Output: ';

   loop
      fetch popular_date into rec;
      exit when not found;

     output_ := output_  || rec.date_rent || '-----------' || rec.c;
   end loop;
   close popular_date;
   return output_;
end; $$
language plpgsql;

select get_most_popular_date(2017);

