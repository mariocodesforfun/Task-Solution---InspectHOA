--Q1
SELECT* FROM orders;

--Q2
SELECT* FROM orders
WHERE order_status = 'pending';

--Q3

SELECT* FROM orders
where user_id = 10 AND order_status = 'complete';

--Q4


select order_id from orders
left join properties 
on orders.prop_id = properties.prop_id
where properties.user_id=4 and order_status = 'complete'



--Q5
--way1:
SELECT orders.order_id, orders.doc_name, orders.order_status, properties.prop_id, properties.prop_address
FROM orders, properties 
WHERE orders.prop_id = properties.prop_id AND orders.user_id = 10;

--way2:
SELECT orders.order_id, orders.doc_name, orders.order_status, properties.prop_id, properties.prop_address
FROM orders
left join properties
on orders.prop_id = properties.prop_id
where orders.user_id=10;



--Q6 
SELECT orders.order_id, orders.doc_name, orders.order_status, properties.prop_id, properties.prop_address, users.email as admin_email 
FROM orders, properties, users
WHERE orders.prop_id = properties.prop_id AND properties.user_id=users.user_id AND orders.user_id = 10;