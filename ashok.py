from openerp.osv import osv, fields

class ashok(osv.osv):
	"""docstring for ashok"""

	_name = 'ashok'
	_description = "Hello from OpenERP"
	_columns = {
		'title' : fields.char('Title', size=30, required=True),
		'note' : fields.text('Note'),
		'note_date' : fields.date('Date'),
	}
ashok()
	
