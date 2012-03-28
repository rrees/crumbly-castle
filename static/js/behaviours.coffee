
$ ->
	load_players = ->
		character_id = $('#player-data').data 'character-id'
		console.log character_id
		$('#player-data').load("/player/#{character_id} .characters")
		setTimeout load_players, 2000
	
	load_players()