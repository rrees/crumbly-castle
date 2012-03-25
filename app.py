import uuid

from flask import Flask, render_template, redirect, request

import graph
import forms

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('index.html', form=forms.NewPlayer())

if __name__ == '__main__':
	app.run(debug = True)