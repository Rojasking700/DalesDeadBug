from app import app
from flask import render_template 

@app.route('/')
@app.route('/index')
def index():
    title = "Dales Dead Bug "

    return render_template('index.html', title=title)