import sqlite3 as sql

class database:
    def __init__(self, name):
        self.db_name = name 

    def create_db(self):
        conn = sql.connect(self.db_name)
        conn.commit()
        conn.close()

    def create_table(self):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            link TEXT,
            price REAL
            )"""
        )
        conn.commit()
        conn.close()

    def drop_table(self):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS products")
        conn.commit()
        conn.close()

    def add_row(self, name, link, price):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        instruction = "INSERT INTO products (name, link, price) VALUES (?, ?, ?)"
        cursor.execute(instruction, (name, link, price))
        conn.commit()
        conn.close()

    def delete_row(self, id):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        instruction = "DELETE FROM products WHERE id = ?"
        cursor.execute(instruction, (id,))
        conn.commit()
        conn.close()

    def edit_row(self, id, new_name, new_link, new_price):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        instruction = "UPDATE products SET name = ?, link = ?, price = ? WHERE id = ?"
        cursor.execute(instruction, (new_name, new_link, new_price, id))
        conn.commit()
        conn.close()

    def clear_table(self):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        instruction = "DELETE FROM products"
        cursor.execute(instruction)
        conn.commit()
        conn.close()

    def select_all_rows(self):
        conn = sql.connect(self.db_name)
        cursor = conn.cursor()
        instruction = "SELECT * FROM products"
        cursor.execute(instruction)
        rows = cursor.fetchall()
        conn.commit()
        conn.close()
        return rows


if __name__ == '__main__':
    db_manager = database('products.db')

    # db_manager.create_db()
    # db_manager.create_table()
    # db_manager.drop_table()
    # db_manager.add_row('name', 'link', 33.33)
    # rows = db_manager.select_all_rows()
    # db_manager.edit_row(1, 'name', 'link', 33.33)
    # db_manager.delete_row(1)
    # db_manager.clear_table()