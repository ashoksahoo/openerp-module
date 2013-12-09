from osv import osv, fields

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
	
	# _columns = {
	# 	'name' : fields.char('Title', size=64, required=True, translate= True),
	# 	'description' : fields.text('Description', readonly= True) ,
	# 	}
	# def _check_name(self,cr,uid, ids):
	# 	for hello in self.browse(cr,uid,ids):
	# 		if 'spam' in hello.name: return False
	# 	return True
	# _sql_constraints= [('name_uniq','unque(name)', 'Name must be unique!')]
	# _constraints = [(_check_name, 'Please avoid spam in names!',['name'])]


