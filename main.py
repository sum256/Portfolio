from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/skill')
def skill():
    return render_template('skill.html')
@app.route('/result')
def result():
    return render_template('result.html')

