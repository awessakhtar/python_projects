from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

@app.route("/")
 
def index():
    top_geo = get_geo()
    top_smaa = get_smaa()
    top_express = get_express()
    return render_template("index.html", top_geo = top_geo, top_smaa = top_smaa, top_express = top_express)

    
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