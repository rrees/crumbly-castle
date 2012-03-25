import wtforms

class NewPlayer(wtforms.Form):
	name = wtforms.TextField()
	description = wtforms.TextAreaField()