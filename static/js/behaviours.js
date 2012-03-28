(function() {

  $(function() {
    var load_players;
    load_players = function() {
      var character_id;
      character_id = $('#player-data').data('character-id');
      console.log(character_id);
      $('#player-data').load("/player/" + character_id + " .characters");
      return setTimeout(load_players, 2000);
    };
    return load_players();
  });

}).call(this);
