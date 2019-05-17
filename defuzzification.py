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
	def BisectorDiscrete(sample, mbership):
		def middle_index(i, l, old_l=float('-inf'), old_r=float('inf')):
			rigthSum = sum([l[idx] for idx in range(i, len(l))])
			leftSum = sum(l) - rigthSum

			if rigthSum == leftSum or abs(old_l-old_r) <= abs(leftSum-rigthSum) or i+1 >= len(l) or i-1 < 0:
				return i
			elif rigthSum > leftSum:
				return middle_index(i+1, l, leftSum, rigthSum)
			return middle_index(i-1, l, leftSum, rigthSum)

		result = middle_index(int(len(mbership)/2), mbership)
		return sample[result]

	@staticmethod
	def LastMaximum(sample, mbership):
		return DefuzzificationMethods.FirstMaximum(sample, mbership)

	@staticmethod
	def FirstMaximum(sample, mbership):
		sample.reverse()
		mbership.reverse()
		return sample[mbership.index(max(mbership))]

	@staticmethod
	def MeanMaximum(sample, mbership):
		max_val = max(mbership)
		sum = 0
		max_cnt = 0
		for i in range(len(mbership)):
			if mbership[i] == max_val:
				sum += sample[i]
				max_cnt+=1
		return sum / max_cnt