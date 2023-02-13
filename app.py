import cgi
import os

import jinja2
from flask import Flask, redirect, render_template, request

template_dir = os.path.join(os.path.dirname(__file__),'Pages')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/home.html')
def home():
   template = jinja_env.get_template('home.html')
   return template.render()

@app.route('/analysis.html')
def analysis1():
   template = jinja_env.get_template('analysis.html')
   return template.render()

@app.route('/Sources.html')
def Sources():
   template = jinja_env.get_template('Sources.html')
   return template.render()

@app.route('/Sources2')
def Sources2():
   template = jinja_env.get_template('Sources2.html')
   return template.render()

if __name__ == '__main__':
   app.run(debug=True)