import psycopg2

conn = psycopg2.connect(
    dbname="new_db",
    user="postgres",
    password="admin@billy",
    host="localhost",
    port="5432",
)
# Create a cursor object to execute SQL queries
cur = conn.cursor()
# Example query
cur.execute("select * from information_schema.columns where table_name = 'employees';")
rows = cur.fetchall()
print(rows)
# Close the connection
cur.close()
conn.close()
