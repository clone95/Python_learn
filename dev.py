from db import DataBase

db = DataBase()

db.create_engine()
db.drop_all_tables()
db.create_all_tables()



data = {"customer_id":3432, "customer_name":'mareethfgfggheco'}

db.insert_one('customer', data)
result = db.query_all('customer')
print(result)