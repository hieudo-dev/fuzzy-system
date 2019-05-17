from aggregation import AggregationMethods
from defuzzification import DefuzzificationMethods
from rule import Rule
from membership import Pi, Triangular

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
		_rules = [Rule(rule, implication, max, min, lambda x: 1-x) for rule, implication in rules]
		lx, ly = self.aggrMethod(_rules, inputs, domain, mbersMethods)
		return self.defuzMethod(lx, ly), lx, ly
