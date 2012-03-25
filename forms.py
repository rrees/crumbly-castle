import wtforms

class NewPlayer(wtforms.Form):
	name = wtforms.TextField("Character's Name", [wtforms.validators.Required()])
	description = wtforms.TextAreaField("Description", [wtforms.validators.Required()])