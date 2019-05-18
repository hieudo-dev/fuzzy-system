import numpy as np

class AggregationMethods:
	@staticmethod
	def Mamdani(rules, values, domain, mbersFuncs):
		results = []
		for rule in rules:
			results.append(rule.Evaluate({key: mbersFuncs[key](value) for key, value in values.items()}))

		lx = []
		ly = []
		for x in np.arange(domain[0], domain[1]+0.2, 0.2):
			lx.append(x)
			y = 0
			for i in range(len(rules)):
				y = max(y, min(mbersFuncs[rules[i].consequent](x), results[i]))
			ly.append(y)
		return lx, ly

	@staticmethod
	def Larsen(rules, values, domain, mbersFuncs):
		results = []
		for rule in rules:
			results.append(rule.Evaluate({key: mbersFuncs[key](value) for key, value in values.items()}))

		lx = []
		ly = []
		for i in range(len(rules)):
			for x in np.arange(domain[0], domain[1]+0.2, 0.2):
				y = mbersFuncs[rules[i].consequent](x)
				z = y*results[i]
				if not x in lx:
					lx.append(x)
					ly.append(z)
				else:
					i_x = lx.index(x)
					ly[i_x] = ly[i_x] if ly[i_x] > z else z
		return lx, ly
