# import the required libaries and frameworks
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def index():
    #create SqL connection
    with sqlite3.connect("tasks.db") as cur:
        #create Sql cursor
        db = cur.cursor()
        
        if request.method == "GET":
            # create table of tasks
            db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, tasks TEXT)")
        
        elif request.method == "POST":
            if "addtask" in request.form:
                newtask = request.form["newtask"]
            
                db.execute("INSERT INTO tasks (tasks) VALUES (?)", (newtask,))
                            
            elif "delete" in request.form:
                delete()

    task_list = db.execute("SELECT * FROM tasks").fetchall()
    print(task_list)        
    return render_template("index.html", tasks = task_list)


@app.route("/", methods = ["POST"])
def delete():
    with sqlite3.connect("tasks.db") as cur:
        #create Sql cursor
        db = cur.cursor()        
        id = request.form.get("name")
        print(id)
        if id:
            print(id)
            db.execute("DELETE FROM tasks WHERE id=?", id)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)