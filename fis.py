from aggregation import AggregationMethods
from defuzzification import DefuzzificationMethods
from rule import Rule
from membership import Pi, Triangular
import matplotlib.pyplot as pl

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

rules = {
	
}

memb = {
	
}

s = FuzzyInferenceSystem('mamdani', 'centroid')
vals = {

}

y, lx, ly = s.infer(rules, vals, memb, (0, 10))
print(y)
pl.plot(lx, ly)
pl.show()