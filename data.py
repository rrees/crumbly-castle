
locations = [
	("courtyard", {
		"name" : "The courtyard",
		"description" : "The ancient walls of  the castle loom over the large courtyard. A motley collection of huts and tents sits on top of the ancient cobbles",
		}),
	("gatehouse", {
		"name" : "The gatehouse",
		"description" : "The drawbridge has collapsed into the chasm that surrounds the castle. Only the birds can leave the castle this way now."
		})
]

routes = [
	("courtyard",
		"gatehouse",
		"The rotting timbers of a portcullis are no obstacle to entering the gatehouse",
		),
	("gatehouse", "courtyard",
		"The courtyard lies beyond the broken portcullis"),
]