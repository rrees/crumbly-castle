
locations = [
	("courtyard", {
		"name" : "The courtyard",
		"description" : "The ancient walls of  the castle loom over the large courtyard. A motley collection of huts and tents sits on top of the ancient cobbles.",
		}),
	("gatehouse", {
		"name" : "The gatehouse",
		"description" : "The drawbridge has collapsed into the chasm that surrounds the castle. Only the birds can leave the castle this way now."
		}),
	("throne-room", {
		"name" : "Abandoned throne room",
		"description" : "Ghosts and echoes of courtiers and great men and women are all that are left of this once grand throne room. Shafts of light now play on the podium where the throne once sat."
		}),
	("shrine", {
		"name" : "A holy shrine",
		"description" : "Even the most desperate can find consolation in faith. Though little more than an eroded statuette standing on a silk cloth-covered block there is a tranquility here as well as the sense of the possibility of a force greater than yourself."
		}),
	("statue-hall", {
		"name" : "The hall of statues",
		"description" : "The best works have all been smashed or looted, instead what remains is some perverse survival of the crooked and worthless. Rats can be heard scuttling behind the remaining pedestals."
		}),
]

routes = [
	("courtyard",
		"gatehouse",
		"The rotting timbers of a portcullis are no obstacle to entering the gatehouse",
		),
	("gatehouse", "courtyard",
		"The courtyard lies beyond the broken portcullis"),

	("courtyard", "shrine",
		"An alcove in the great wall has been festooned by coloured ribbons"),
	("shrine", "courtyard",
		"The open alcove leads to the courtyard"),

	("statue-hall", "courtyard",
		"The light of the courtyard shines through the door-less entrance"),
	("courtyard", "statue-hall",
		"Once great doors led to the castle's hall, now the entrance is open to all"),

	("statue-hall", "throne-room",
		"A carved entrance leads to the throne room"),
	("throne-room", "statue-hall",
		"The main entrance in the room leads to the statue hall"),
]