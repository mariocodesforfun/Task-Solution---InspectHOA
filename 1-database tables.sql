CREATE TABLE roles(
role_id int PRIMARY KEY NOT NULL,
role_name varchar(255) NOT NULL,
role_description varchar(255) NOT NULL
)

CREATE TABLE users(
user_id int  PRIMARY KEY NOT NULL,
first_name varchar(255) NOT NULL,
last_name varchar(255) NOT NULL,
email varchar(255) NOT NULL,
account_password varchar (255) NOT NULL,
role_id int FOREIGN KEY REFERENCES roles(role_id) NOT NULL
)

CREATE TABLE properties(
prop_id int  PRIMARY KEY NOT NULL,
user_id int FOREIGN KEY REFERENCES users(user_id),
prop_address varchar(255) NOT NULL,
prop_city varchar(255) NOT NULL,
prop_state varchar(255) NOT NULL, 
prop_email varchar(255) NOT NULL
)

CREATE TABLE orders(
order_id int PRIMARY KEY NOT NULL,
prop_id int FOREIGN KEY REFERENCES properties(prop_id) NOT NULL,
user_id int FOREIGN KEY REFERENCES users(user_id) NOT NULL, 
doc_name varchar(255) NOT NULL,
order_status varchar(255) NOT NULL, 
)






