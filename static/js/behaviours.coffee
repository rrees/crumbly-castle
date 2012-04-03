
$ ->
	load_players = ->
		character_id = $('#player-data').data 'character-id'
		$('#player-data').load("/player/#{character_id} #other-players")
		setTimeout load_players, 2000

	load_players()