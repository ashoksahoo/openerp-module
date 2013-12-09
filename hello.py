 from osv import osv, fields

class idea(osv.Model):
	"""docstring for idea"""
	# def __init__(self, arg):
	# 	super(idea, self).__init__()
	# 	self.arg = arg

	_name = 'idea.idea'
	_columns = {
		'name' : fields.char('Title', size=64, required=True, translate= True),
		'state' : fields.selection([('draft','Draft'),('confirmed','Confirmed'),]'State', required= True, readonly = True),
		'description' : fields.text('Description', readonly= True, states = {'draft':[('readonly', False)]})
		'active' : fields.boolean('Active'),
		'invent_date' : fields.date('Invent date'),
		'inventor_id' : fields.many2one('res.partner', 'Inventor'),
		'inventor_country_id' : fields.related('inventor_id', 'country', readonly = True, type = 'many2one')
		'vote_ids': fields.one2many('idea.vote','idea_id','Votes'),
		'sponsor_ids': fields.many2many('res.partner','idea_sponsor_rel',
		'idea_id','sponsor_id','Sponsors'),
		'score': fields.float('Score',digits=(2,1)),
		'category_id' = many2one('idea.category', 'Category'),
		}
		




 class idea(osv.Model):
 idea
 _name = 'idea.idea'
 _columns = {
 'name': fields.char('Title', size=64, required=True, translate=True),
 'state': fields.selection([('draft','Draft'),
 ('confirmed','Confirmed')],'State',required=True,readonly=True),
 # Description is read-only when not draft!
 'description': fields.text('Description', readonly=True,
 states={'draft': [('readonly', False)]} ),
 'active': fields.boolean('Active'),
 'invent_date': fields.date('Invent date'),
 # by convention, many2one fields end with '_id'
 'inventor_id': fields.many2one('res.partner','Inventor'),
 'inventor_country_id': fields.related('inventor_id','country',
 readonly=True, type='many2one',
 relation='res.country', string='Country'),
 # by convention, *2many fields end with '_ids'

class idea2(osv.Model):
	_inherit = 'idea.idea'
	def _score_calc(self,cr,uid,ids,field,arg,context=None):
		res = {}
		# This loop generates only 2 queries thanks to browse
		for idea in self.browse(cr,uid,ids,context=context):
			sum_vote = sum([v.vote for v in idea.vote_ids])
			avg_vote = sum_vote/len(idea.vote_ids)
			res[idea.id] = avg_vote
		return res
	_columns = {
	# Replace static score with average of votes
	'score':fields.function(_score_calc,type='float')
}

