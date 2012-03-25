import uuid

from flask import Flask, render_template, redirect, request

import graph
import forms

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('index.html', form=forms.NewPlayer())

@app.route('/player', methods=['POST'])
def new_player():
	form = forms.NewPlayer(request.form)
	if form.validate():
		player_id = uuid.uuid4().hex
		return redirect('/player/' + player_id)

	return render_template('index.html', form=form)

@app.route('/player/<player_id>')
def game(player_id):
	return render_template('game.html', player = player_id)


if __name__ == '__main__':
	app.run(debug = True)