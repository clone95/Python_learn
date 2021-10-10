from sqlalchemy import *
import logging
from attr import attrs, attrib
import pandas as pd

@attrs
class DataBase(object):

    engine_string = attrib(default='sqlite:///cryptofinance.sqlite')
    
    def create_engine(self):
        self.engine = create_engine(self.engine_string)
        self.connection = self.engine.connect()

    def create_all_tables(self):
        self.metadata_obj = MetaData()

        try:
            self.customer = Table('customer', self.metadata_obj,
                Column('customer_id', Integer, primary_key=True),
                Column('customer_name', String(16), nullable=False),
            )

            self.product = Table('product', self.metadata_obj,
                Column('product_id', Integer, primary_key=True),
            )
            
            self.subscription = Table('subscription', self.metadata_obj,
                Column('subscription_id', Integer, primary_key=True),
                Column('customer_id', Integer, ForeignKey("customer.customer_id"), nullable=False),
                Column('product_id', Integer, ForeignKey("product.product_id"), nullable=False),

            )

            self.metadata_obj.create_all(self.engine)

            return True

        except Exception as e:
            logging.error(f"create_all_tables(): {e}")
            return False


    def drop_all_tables(self):
        self.metadata_obj = MetaData()

        try:
            self.metadata_obj.drop_all(self.engine)
            return True
        except Exception as e:
            logging.error(f"drop_all_tables(): {e}")
            return False

    
    def get_all_tables(self):

        try:
            for t in self.metadata_obj.sorted_tables:
                print(t.name)
        except Exception as e:
            logging.error(f"get_all_tables(): {e}")
            return False

    
    def insert_one(self, table_name, data):
        try:
            table_string = "self." + table_name
            query = insert(eval(table_string)).values(**data) 
            ResultProxy = self.connection.execute(query)
        except Exception as e:
            logging.error(f"insert_one(): {e}")
            return False


    def query_all(self, table_name):
        try:
            table_string = "self." + table_name
            results = self.connection.execute(select([eval(table_string)])).fetchall()
            return pd.DataFrame(results)
        except Exception as e:
            logging.error(f"query_all(): {e}")
            return False
        
