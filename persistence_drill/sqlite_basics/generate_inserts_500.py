
with open("insert_500.sql", "w") as f:
    for i in range(4, 504):  # Assuming IDs 1-3 already exist
        company_name = f"Company_{i}"
        f.write(f"INSERT INTO COMPANIES (company_name, id) VALUES ('{company_name}', {i});\n")

print("Generated insert_500.sql")
