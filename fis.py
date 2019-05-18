from aggregation import AggregationMethods
from defuzzification import DefuzzificationMethods
from rule import Rule
from membership import Pi, Triangular
import matplotlib.pyplot as pl
import numpy as np

class FuzzyInferenceSystem:
	methods = {
		'mamdani': AggregationMethods.Mamdani,
		'larsen': AggregationMethods.Larsen,
		'centroid': DefuzzificationMethods.Centroid,
		'bisector': DefuzzificationMethods.BisectorDiscrete,
		'meanmax': DefuzzificationMethods.MeanMaximum,
		'lastmax': DefuzzificationMethods.LastMaximum,
		'firstmax': DefuzzificationMethods.FirstMaximum,
	}

	def __init__(self, aggrMethod, defuzMethod):
		self.aggrMethod = self.methods[aggrMethod]
		self.defuzMethod = self.methods[defuzMethod]

	def infer(self, rules, inputs, mbersMethods, domain):
		_rules = [Rule(rule, implication, max, min, lambda x: 1-x) for rule, implication in rules.items()]
		lx, ly = self.aggrMethod(_rules, inputs, domain, mbersMethods)
		return self.defuzMethod(lx, ly), lx, ly

def plotMbers(mbership, l, r):
	ly = []
	for i in np.arange(l, r, 0.2):
		ly.append(mbership(i))
	pl.plot(np.arange(l,r, 0.2), ly)
	pl.show()

food = 6.5			# 1 -> 10
service = 9.8 		# 1 -> 10

rules = {
	'GoodService & GoodFood': 'HighTip',
	'AverageService & GoodFood': 'HighTip',
	'BadService & GoodFood': 'MediumTip',
	'AverageService': 'MediumTip',
	'BadService & BadFood': 'LowTip',
	'GoodService & BadFood': 'LowTip'
}

memb = {
	'BadFood': Triangular(-1, 5, 0),
	'AverageFood': Triangular(0, 10, 5),
	'GoodFood': Triangular(5, 11, 10),
	'BadService': Triangular(-1, 5, 0),
	'AverageService': Triangular(0, 10, 5),
	'GoodService': Triangular(5, 11, 10),
	'LowTip': Triangular(-1, 13, 0),
	'MediumTip': Triangular(0, 25, 13),
	'HighTip': Triangular(13, 26, 25)
}

s = FuzzyInferenceSystem('mamdani', 'meanmax')
vals = {
	'GoodService': service,
	'AverageService': service,
	'BadService': service,
	'GoodFood': food,
	'BadFood': food,
}

# print(memb['GoodFood'](10), memb['GoodService'](10), memb['HighTip'](25))
# plotMbers(memb['HighTip'], 0, 25)
# print(memb['HighTip'](25))

y, lx, ly = s.infer(rules, vals, memb, (0, 25))
print(y)
pl.plot(lx, ly)
pl.show()