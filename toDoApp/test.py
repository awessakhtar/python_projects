import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS test (task TEXT)")

while True:
    task_value = input("Enter a task here: ")
    cur.execute("INSERT INTO test VALUES (?)", [task_value])
    new_task = cur.execute("SELECT * FROM test").fetchall()
    for task in new_task:
        print(task[0])
    if task_value == "q":
        break
    

