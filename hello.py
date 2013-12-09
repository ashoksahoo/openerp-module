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
	}
		




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

