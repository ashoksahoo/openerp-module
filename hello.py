from osv import osv, fields

class hello(osv.Model):
	"""docstring for hello"""
	# def __init__(self, arg):
	# 	super(hello, self).__init__()
	# 	self.arg = arg

	_name = 'hello.hello'
	_columns = {
		'name' : fields.char('Title', size=64, required=True, translate= True),
		'state' : fields.selection([('draft','Draft'),('confirmed','Confirmed')],'State', required= True, readonly = True),
		'description' : fields.text('Description', readonly= True, states = {'draft':[('readonly', False)]}) ,
		'active' : fields.boolean('Active'),
		'invent_date' : fields.date('Invent date'),
		'inventor_id' : fields.many2one('res.partner', 'Inventor'),
		'inventor_country_id' : fields.related('inventor_id', 'country', readonly = True, type = 'many2one'),
		'vote_ids': fields.one2many('hello.vote','hello_id','Votes'),
		'sponsor_ids': fields.many2many('res.partner','hello_sponsor_rel','hello_id','sponsor_id','Sponsors'),
		'score': fields.float('Score',digits=(2,1)),
		'category_id': fields.many2one('hello.category', 'Category'),
		}
	_defaults = {
		'active' : True,
		'state' : 'draft',
		}
	def _check_name(self,cr,uid, ids):
		for hello in self.browse(cr,uid,ids):
			if 'spam' in hello.name: return False
		return True
	_sql_constraints= [('name_uniq','unque(name)', 'Ideas must be unique!')]
	_constraints = [(_check_name, 'Please avoid spam in hellos!',['name'])]

class hello2(osv.Model):
	_inherit = 'hello.hello'
	def _score_calc(self,cr,uid,ids,field,arg,context=None):
		res = {}
		# This loop generates only 2 queries thanks to browse
		for hello in self.browse(cr,uid,ids,context=context):
			sum_vote = sum([v.vote for v in hello.vote_ids])
			avg_vote = sum_vote/len(hello.vote_ids)
			res[hello.id] = avg_vote
		return res
	_columns = {
	# Replace static score with average of votes
	'score':fields.function(_score_calc,type='float')
}

