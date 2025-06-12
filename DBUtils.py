import psycopg2

class DBUtils:
    def __init__(self, host="localhost", port=5432, database="books", user="bookrex", password="secretpassword"):
        self.conn=psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password,
        )
    
    def create_table(self, table_name, schema):
        pass

    def update_table(self, table_name, data):
        pass
        
    def read_table(self, table_name, data):
        pass
        
    def delete_table(self, table_name, data):
        pass
