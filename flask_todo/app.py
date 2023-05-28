# import libraries url_for will direct to specific used in case of css loading etc
from flask import Flask, render_template, request, url_for, redirect
# pip install SQL Alchemy
from flask_sqlalchemy import SQLAlchemy
# for adding date time added the task
from datetime import datetime

# setup db object from documention of sql alchemy
db = SQLAlchemy()
# set up flask applicattion
app = Flask(__name__)
# application of flask configure for db. 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
# following line will initiate database
db.init_app(app)

# follwing classs will create a table name todo
class Todo(db.Model):
    # each coloum along with type and property 
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200) , nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    # special funciotn called reperesentaiton fuction. it is helpfull during query to the db
    # if reper not set the query results not readable
    def __repr__(self):
        return '<Task %r' % self.id
# it will create all above tables with the context of the applicaiton
with app.app_context():
    db.create_all()

# flask application for data transfer to and from html as follows
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        # to be failsafe in case of any error
        try:
            # the query is in temp memory of db. commit db save it permenantly
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "There is a problme Check your code"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks = tasks)

@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "there is a problem deleting the task from database"

@app.route('/update/<int:id>', methods = ["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method =="POST":
        task.content = request.form["content"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There is an error updating the task look at your code and figure it out"
    else:
        return render_template("update.html", task = task)


if __name__=="__main__":
    app.run(debug=True)