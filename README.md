# 🤖 AMAZON PRODUCT TRACKER

In this project I have created a web scrapping bot with a local database to track de products prices. It has a CLI menu to interact with the app.

___

# 📝 Features
- **Check changes:** check if any of the products in the database have change the price.
- **Show database products:** print all the products on the database.
- **Add product:** add a new product to track to the database.
- **Delete product:** delete a product of the database to stop tracking it.
- **Edit product:** edit anything from a product of the database.
- **Clear products list:** delete all products of the database to stop tracking them.

# ⬇ How to install
1. Clone the repository
````bash
git clone sdf
````
2. Navigate to the folder
````bash
cd amazon-products-tracker
````
3. Create virtual enviroment
````bash
virtualenv venv
````
4. Activate virtual enviroment:
- **Windows:** `venv\Scripts\activate`
- **MacOS/Linux:** `source venv/bin/activate`
5. Install dependencies
````bash
pip install -r requirements.txt
````
6. Execute the project
````bash
python main.py
7. Deactivate virtual enviroment
````bash
deactivate
````

If you want to see how it works and you are using vscode I recommend using the **SQLite** extension.

# 👨‍🏫 How to use
The app has a CLI menu to use the app but you can just use the methods and functions by yourself.
````python
# Scrapper methods
scrapper = web_scrapper.web_scraper()
scrapper.obtener_precio('https://productlink.com')

# DB manager methods
db_manager = database_manager.database('products.db')
db_manager.create_db()
db_manager.create_table()
db_manager.drop_table()
db_manager.create_db()
db_manager.create_table()
db_manager.add_row('name', 'link', 11.11)
db_manager.delete_row('name')
db_manager.edit_row('name', 'new_name', 'new_link', 22.22)
db_manager.clear_table()
db_manager.select_all_rows()

# Main functions
check_changes()
show_products()
add_row()
delete_row()
edit_row()
clear_rows()
````

# 📈 Future improvements
In the future this app will evolucionate and get better:
- Interface with Tkinter
- Graphics with stadistics

# 📂 File tree and modules
- gitignore
- README.md
- modules
	- web_scrapper.py
	- db_manager.py
- main.py
- products.db
	- products

# 📚 Libraries stack
- **selenium**: web scrapping
- **sqlite3**: local database
- **time**: web scrapping waiting
- **colorama**: color styled print products

# 🟨 Classes and methods
- **`web_scrapper`**: does web scrapping operations.

	- **Attributes**
		- `driver_path`: `'path/to/chromedriver'`.
		- `driver`: `webdriver.Chrome()`.

	- **Methods**
		- `get_price`: returns the price of a product given the link.
		- `destruct_driver`: destructs the driver to save memory (`self.driver.quit()`).

- **`database`**: manages database actions.

	- **Attributes**
		- `db_name`: the name of the database file.

	- **Methods**
		- `create_db`: creates the database if doesn't exists
		- `create_table`: creates a new table if doesn't exists.
		- `drop_table`: deletes the table *products*.
		- `add_row`: adds a new row to the table.
		- `delete_row`: deletes a row given the id.
		- `edit_row`: edits the data of a row.
		- `clear_table`: deletes all the rows of the table.
		- `select_all_rows`: returns all the rows of the table.

____
By [Santi](https://github.com/saantii-17/)