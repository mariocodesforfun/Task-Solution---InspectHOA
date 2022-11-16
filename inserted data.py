#data to be stored in database tables

from models import Roles, Users, Properties, Orders
admin_role = Roles(role_id=1, role_name = 'admin', role_description='Can add new properties' )
client_role = Roles(role_id=2, role_name='client', role_description='can submit orders')

user_data = [
Users(user_id=2, first_name='John', last_name='Smith', email="johnsmith@gmail.com", account_password='keyboard123', role_id=1),
Users(user_id=3, first_name='George', last_name='Williams', email="georgewilliams@gmail.com", account_password='playsmart4563', role_id=2),
Users(user_id=4, first_name='James', last_name='Gordon', email="jamesgordon@gmail.com", account_password='laptop2343', role_id=1),
Users(user_id=5, first_name='Clay', last_name='Thompson', email="claythompson@gmail.com", account_password='basketball2343', role_id=2),
Users(user_id=6, first_name='Jeffereson', last_name='Mat', email="jeffersonmat@gmail.com", account_password='ilovefood62374', role_id=1),
Users(user_id=7, first_name='Peter', last_name='Novak', email="peternovak@gmail.com", account_password='thereisnospace2345', role_id=2),
Users(user_id=8, first_name='Manuel', last_name='Waser', email="manuelwaser@gmail.com", account_password='football342', role_id=2),
Users(user_id=9, first_name='Mike', last_name='Josh', email="mikejosh@gmail.com", account_password='noonehere123', role_id=2),
Users(user_id=10, first_name='Tom', last_name='Corey', email="tomcorey@gmail.com", account_password='playtennis324', role_id=2),
Users(user_id=11, first_name='Ken', last_name='Jordan', email="kenjordan@gmail.com", account_password='player1234', role_id=1)
]

properties_data = [
    Properties(prop_id=1, user_id=2, prop_address='Arlenski11', prop_city='Sofia', prop_state='Bulgaria', prop_email='sofiaestate@gmail.com'),
    Properties(prop_id=2, user_id=4, prop_address='2313 32nd Street', prop_city='Brooklyn', prop_state='New York', prop_email='investinproperties@gmail.com'),
    Properties(prop_id=3, user_id=4, prop_address='2312 Broadway', prop_city='Manhattan', prop_state='New York', prop_email='buymodernestate@gmail.com'),
    Properties(prop_id=4, user_id=6, prop_address='1231 Strase', prop_city='Berlin', prop_state='Germany', prop_email='deutscheproperty@gmail.com'),
    Properties(prop_id=5, user_id=6, prop_address='11 Square', prop_city='Santa Clara', prop_state='California', prop_email='properproperty@gmail.com'),
    Properties(prop_id=6, user_id=4, prop_address='42nd Street', prop_city='Detroit', prop_state='Michigan', prop_email='classicrealestate@gmail.com'),
]


orders_data = [
    Orders(order_id=1, prop_id=1, user_id=10, doc_name='ByLawDocument', order_status='complete'),
    Orders(order_id=2, prop_id=2, user_id=10, doc_name='Certificate', order_status='complete'),
    Orders(order_id=3, prop_id=2, user_id=7, doc_name='FirstFloorPlan', order_status='pending'),
    Orders(order_id=4, prop_id=3, user_id=3, doc_name='CC&Rs', order_status='complete'),
    Orders(order_id=7, prop_id=4, user_id=5, doc_name='Rules&Regulations', order_status='complete'),
    Orders(order_id=8, prop_id=3, user_id=5, doc_name='WholePropertyPlan', order_status='pending')
]

