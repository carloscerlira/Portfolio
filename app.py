import requests
from flask import Flask, render_template, url_for, request
import sys
sys.path.append('data/projects')
from genProjects import projectsData
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', projectsData=projectsData)

@app.route('/example')
def example():
    return render_template('exampleTemplate.html', projectsData=projectsData)

if __name__ == '__main__':
    app.run(debug=True)