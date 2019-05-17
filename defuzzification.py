import numpy as np

class DefuzzificationMethods:
	@staticmethod
	def Centroid(sample, mbership):
		sum = 0
		den = 0
		for i in range(len(sample)):
			sum += sample[i]*mbership[i]
			den += mbership[i]
		return sum/den

	@staticmethod
	def Bisector(x, y):
		# result, _, _ = middle_index(int(len(y)/2), y)
		# return x[result]
		pass

	@staticmethod
	def LastMaximum(sample, mbership):
		return DefuzzificationMethods.FirstMaximum(sample, mbership)

	@staticmethod
	def FirstMaximum(sample, mbership):
		sample.reverse()
		mbership.reverse()
		return sample[mbership.index(max(mbership))]

	@staticmethod
	def MeanMaximum(x, y):
		max_l = max(y)
		values = []
		for i in range(len(y)):
			if y[i] == max_l:
					values.append(x[i])
		return np.average(values)