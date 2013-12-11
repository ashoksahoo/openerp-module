from openerp.osv import osv, fields

class ashok_c(osv.osv):
	"""docstring for ashok"""

	_name = 'ashok.sahoo'
	_description = "Hello from OpenERP"
	_columns = {
		'title' : fields.char('Title', size=30, required=True),
		'note' : fields.text('Note'),
		'note_date' : fields.date('Date'),
		'no1' : fields.integer('No_1', required=True),
		'no2' : fields.integer('No_2', required=True),
		'no3' : fields.integer('No_3', readonly= True),
	}
	def create(self, cr, uid, vals, context=None):
		vals['no3'] = vals.get('no1') + vals.get('no2')
		return super(ashok_c, self).create(cr, uid, vals, context=context)
ashok_c()
