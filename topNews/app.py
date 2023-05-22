from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import sqlite3


app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])

def index():
    # upon initial acess serve log in page
    if request.method == "GET":
        return render_template("Login.html")

    # when username and password are enter validate from db    
    elif request.method == "POST":
    
        #get username from html page form to validate with database
        username = request.form.get("username")
            
        # Check if the username and password exist in the database
        with sqlite3.connect("users.db") as db:
            cur = db.cursor()
            cur.execute("SELECT username FROM users WHERE username = ?", (username,))
            username_exists = cur.fetchone()
    
            cur.execute("SELECT password FROM users WHERE username = ?", (username,))
            password_exists = cur.fetchone() is not None
            cur.close()

    if username_exists is None:
        if request.method == "POST":
            register()                
            return render_template("register.html")
    else:
        render_template("login.html")
        
    
        # If the username and password exist in the database, then return a message indicating that the user is already registered
        if username_exists and password_exists:
            #Redirect to index.html page
            top_geo = get_geo()
            top_smaa = get_smaa()
            top_express = get_express()
            return render_template("index.html", top_geo = top_geo, top_smaa = top_smaa, top_express = top_express)
           
                 

@app.route("/register")
def register():
    with sqlite3.connect("users.db") as db:
        cur = db.cursor()
        username = request.form["username"]
        password = request.form["password"]
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        cur.close()
        return ("login.html")



def get_geo():     
    url = "https://www.geo.tv/"
    page = requests.get(url)
    soup =  BeautifulSoup(page.content, "html.parser")
    # print(soup.text)
    top_geo = []
    headings = soup.find_all("div", class_ = ("m_except"))
    for heading in headings:
        top_geo.append(heading.text)
    return top_geo


def get_smaa():
    url = "https://www.samaaenglish.tv/"
    page = requests.get(url)
    soup =  BeautifulSoup(page.content, "html.parser")
    # print(soup.text)
    top_smaa = []
    headings = soup.find_all("a", class_ = ("story__link"))
    for heading in headings:
        top_smaa.append(heading.text)
    return top_smaa


def get_express():
    url = "https://tribune.com.pk/"
    page = requests.get(url)
    soup =  BeautifulSoup(page.content, "html.parser")
    # print(soup.text)
    top_express = []
    headings = soup.find_all("div", class_ = ("related-content-text"))
    for heading in headings:
        top_express.append(heading.text)
    
    return (top_express)


if __name__ == '__main__':
    app.run(debug=True)