import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/Selenium')
def sel_content():
    title = "High Selenium Foods"
    return render_template("Bar_high_Se.html",title=title)
    
@app.route('/Fiber')
def fib_content():
    title = "High Fiber Foods"
    return render_template("Bar_high_fiber.html",title=title)   
    
if __name__ == '__main__':
    app.run() 