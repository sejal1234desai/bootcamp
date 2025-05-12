SQLite Operations Project

This project demonstrates 20 essential SQLite database operations using Python, ranging from basic CRUD to complex transactional logic. Each operation is implemented as a separate Python script.

1. create_tables.py

Creates the products table in the SQLite database.

Columns: id, name, price.

2. insert_product.py

Inserts a new product into the products table.

3. fetch_products.py

Fetches and displays all products from the database.

4. update_product.py

Updates the name and price of a specific product using its ID.

5. delete_product.py

Deletes a product by ID from the database.

6. exception_handling.py

Demonstrates exception handling while inserting products.

Avoids crashing the program on errors.

7. search_function.py

Searches for products whose name contains a given keyword.

8. create_with_input.py

Takes user input and inserts the product into the database.

9. join_query.py

Creates a categories table and joins it with products.

Displays product names along with their category names.

10. data_validation.py

Validates product data before inserting.

Ensures name is not empty and price is a positive number.

11. transactions.py

Demonstrates a basic transaction by inserting multiple products.

Rolls back if any insert fails.

12. aggregation.py

Calculates and displays the total value of all products.

Uses SQL aggregation (SUM) on price.

13. export_to_csv.py

Exports all product data to a CSV file (products.csv).

14. batch_insert.py

Inserts multiple products at once in a single transaction.

15. transaction_insert_customers.py

Inserts multiple records into a customers table using transactions.

Rolls back on failure.

16. transaction_update_multiple_tables.py

Updates records in both orders and order_details tables within a transaction.

Ensures consistency using rollback on failure.

17. transaction_batch_insert.py

Batch-inserts multiple products using a single transaction.

Rolls back the entire batch if any insertion fails.

18. banking_transaction.py

Simulates a bank transfer using an accounts table.

Deducts funds from one account and adds to another atomically.

19. inventory_transaction.py

Implements inventory tracking with products and inventory_log tables.

Updates inventory count and logs changes in a single transaction.

20. inventory_price_transaction.py

Performs a complex transaction: adjusts inventory quantity and updates the product price.

Logs changes to the inventory_log.

How to Run

Make sure you have Python and SQLite installed.

Activate your virtual environment if you have one.

Run each file using:
python filename.py

Use sqlite3 store.db to inspect the database manually.

CSV file will be generated in the same directory when you run export_to_csv.py.

