import sqlite3
class DatabaseHandler:
    
    def __init__(self, database_path, table_name):
        self.database_path = database_path
        self.table_name = table_name

    def create_database(self):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        create_table_query = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary REAL NOT NULL);"""
        
        cursor.execute(create_table_query)
        
        conn.commit()
        conn.close()


    def insert_data(self, new_employee):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        add_data_query = f"INSERT INTO {self.table_name} (name, department, salary) VALUES (?, ?, ?)"
        cursor.execute(add_data_query, new_employee)
        conn.commit()
        conn.close()

    def view_data(self):
        
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        get_data_query = f"SELECT * FROM {self.table_name}"
        cursor.execute(get_data_query)
        all_data = cursor.fetchall()
        
        for row in all_data:
            print(f"ID          : {row[0]}")
            print(f"Name        : {row[1]}")
            print(f"Department  : {row[2]}")
            print(f"Salary      : {row[3]}")
            print("-" * 30)
        conn.close()

        return all_data

    def search_data(self, required_name):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        search_data_query = f"""SELECT * FROM {self.table_name} WHERE name = ?"""

        cursor.execute(search_data_query, (required_name,) )
        result = cursor.fetchone()

        
        conn.close()

        return result

    def update_data(self, value, condition):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()

        update_data_query = f"UPDATE {self.table_name} SET department = ? WHERE id = ?"
        new_values = (value, condition)
        cursor.execute(update_data_query, new_values)
        
        
        conn.commit()
        conn.close()

    def delete_data(self, name_to_delete):
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        delete_data_query = f"DELETE FROM {self.table_name} WHERE id = ?"
        
        cursor.execute(delete_data_query, (name_to_delete, ))
        conn.commit()
        conn.close()

