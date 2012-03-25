
import os
import random

from neo4jrestclient.client import GraphDatabase

from utils import first

GRAPH_URL = os.environ.get('NEO4J_REST_URL', "http://localhost:7474/db/data/")
credentials = None

if 'NEO4J_LOGIN' in os.environ and 'NEO4J_PASSWORD' in os.environ:
	credentials = (os.environ['NEO4J_LOGIN'], os.environ['NEO4J_PASSWORD'])

if credentials:
	db = GraphDatabase(GRAPH_URL, username = credentials[0], password = credentials[1])
else:
	db = GraphDatabase(GRAPH_URL)

def create_unique_node(index_name, index_key, index_id, properties = None):
	if not index_name in db.nodes.indexes.keys():
		db.nodes.indexes.create(index_name)

	index = db.nodes.indexes.get(index_name)

	node = first(index[index_key][index_id])

	if not node:
		node = db.nodes.create()

		if properties:
			for key, value in properties.items():
				node[key] = value

		index.add(index_key, index_id, node)

	return node

def node(index_name, index_key, index_id):
	index = db.nodes.indexes.get(index_name)

	if not index: return None

	lookup_results = index[index_key][index_id]

	if lookup_results:
		return first(index[index_key][index_id])

	return None

def link(a, b, relationship_name, relationship_data = None):
	existing_links = [node for node in a.relationships.outgoing([relationship_name]) if node.end == b]
	if not existing_links:
		rel = a.relationships.create(relationship_name, b)
		if relationship_data:
			for key, value in relationship_data.items():
				rel[key] = value
	return a

def unlink(a, relationship_name):
	[rel.delete() for rel in a.relationships.outgoing([relationship_name])]

def location(name):
	return node('locations', 'location', name)

def random_location():
	locations = [node for node in db.nodes.indexes.get('locations').query("location", "*")]
	return random.choice(locations)

def player(player_id):
	player = node('characters', 'character', player_id)

	return player