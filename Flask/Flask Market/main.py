#Running on http://127.0.0.1:5000

from flask import Flask, render_template
app =Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')
