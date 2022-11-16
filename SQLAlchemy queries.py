from models import Users, Properties, Orders, Roles
from database import session




# 1 - List all the orders in the system.

print('Query 1 results')
result_1 = session.query(*Orders.__table__.columns)
for row in result_1:
        print("order id: {} property_id: {} user id: {}  document name: {}  order status:{}".format(row.order_id, row.prop_id, row.user_id, row.doc_name, row.order_status))


#2 - List all the pending orders in the system.
print('Query 2 results')

result_2 = session.query(Orders).filter(Orders.order_status=='pending')
for row in result_2:
    print("order id: {}  property id: {}  user id: {}  document name: {}  order status: {}".format(row.order_id, row.prop_id, row.user_id, row.doc_name, row.order_status))


# 3 - List all the completed orders in the system created by client with id = CLIENT_USER_ID
print('Query 3 results')
result_3 = session.query(Orders).filter(Orders.order_status=='complete', Orders.user_id==10)
for row in result_3:
    print("order id: {} property id: {} user id: {} document name: {} order status: {}".format(row.order_id, row.prop_id, row.user_id, row.doc_name, row.order_status))


# 4 - List all the completed orders in the system where client requested a document from a property that was added from
# Administrator user with id = ADMIN_USER_ID
print('Query 4 results')
result_4 = session.query(Orders.order_id, Orders.order_status, Properties.user_id).join(Properties, Properties.prop_id==Orders.prop_id).filter(Properties.user_id==4, Orders.order_status=='complete')
for row in result_4:
    print("order id: {}".format(row.order_id))


# 5 - In a single query, show the following order info from client with id = CLIENT_USER_ID: order_id, document name, order
#status, property id, property address
print('Query 5 results')
result_5 = session.query(Orders.order_id, Orders.doc_name, Orders.order_status, Properties.prop_id, Properties.prop_address).join(Properties).filter(Orders.user_id==10)

for row in result_5:
    print('order id: {} document name: {} order status: {} property id: {} property address: {}'.format(row.order_id, row.doc_name, row.order_status, row.prop_id, row.prop_address))


# 6 - In the info of query 5 include also the email of the administrator that added the property in the system
print('Query 6 results')
result_6 = session.query(Orders.order_id,Orders.doc_name, Orders.order_status, Properties.prop_id, Properties.prop_address, Users.email).join(Properties, Properties.prop_id==Orders.order_id).join(Users, Properties.user_id==Users.user_id).filter(Orders.user_id==10)

for row in result_6:
    print('order id: {} document name: {} order status: {} property id: {} property address: {} admin_email: {}'.format(row.order_id, row.doc_name, row.order_status, row.prop_id, row.prop_address, row.email))
