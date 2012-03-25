import uuid

from flask import Flask, render_template, redirect, request

import graph
import forms
import data

from utils import first

app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('index.html', form=forms.NewPlayer())

@app.route('/setup')
def setup():
	for location_name, location_data in data.locations:
		graph.create_unique_node('locations', 'location', location_name, location_data)

	for start, finish, description in data.routes:
		graph.link(graph.location(start),
			graph.location(finish),
			"Route",
			{"description" : description})

	return redirect('/')

@app.route('/player', methods=['POST'])
def new_player():
	form = forms.NewPlayer(request.form)
	if form.validate():
		player_id = uuid.uuid4().hex

		player_data = {"id" : player_id}
		player_data.update(form.data)

		player = graph.create_unique_node('characters', 'character', player_id, player_data)

		graph.link(player, graph.random_location(), "Location")
		return redirect('/player/' + player_id)

	return render_template('index.html', form=form)

@app.route('/player/<player_id>')
def game(player_id):
	player = graph.player(player_id)

	other_players = [rel.start for rel in player.location.relationships.incoming(['Location']) if not rel.start == player]

	exits = [(rel.get("description", "A stone path"), rel.end.id) for rel in player.location.relationships.outgoing(['Route'])]

	return render_template('game.html',
			player = player.properties,
			location = player.location,
			other_players = other_players,
			exits = exits)

@app.route('/player/<player_id>/location/<new_node_id>')
def move(player_id, new_node_id):
	player = graph.player(player_id)

	if int(new_node_id) in [rel.end.id for rel in player.location.relationships.outgoing(['Route'])]:
		graph.unlink(player, 'Location')
		graph.link(player, graph.node_by_id(new_node_id), 'Location')

	return redirect('/player/' + player_id)


if __name__ == '__main__':
	app.run(debug = True)