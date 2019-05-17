from aggregation import Mamdani, Larsen
from defuzzification import DefuzzificationMethods
import membership

class FuzzificationInferenceSystem:
	methods = {
		'mamdani': Mamdani,
		'larsen': Larsen,
		'centroid': DefuzzificationMethods.Centroid,
		'bisector': DefuzzificationMethods.Bisector,
		'meanmax': DefuzzificationMethods.MeanMaximum,
		'lastmax': DefuzzificationMethods.LastMaximum,
		'firstmax': DefuzzificationMethods.FirstMaximum,
	}

	def __init__(self, aggrMethod, defuzMethod):
		self.aggrMethod = self.methods[aggrMethod]
		self.defuzMethod = self.methods[defuzMethod]

	def infer(self, rules, input, mbersMethod):
		pass