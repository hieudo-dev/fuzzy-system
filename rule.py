class Rule:
	def __init__(self, rule, consequent, opOr, opAnd, opNot):
		self.rule = rule.split(' ')
		self.consequent = consequent
		self.opOr = opOr
		self.opAnd = opAnd
		self.opNot = opNot

	def Evaluate(self, values):
		ruleValues = []
		for token in self.rule:
			if token != '&' and token != '|' and token != '~':
				ruleValues.append(values[token])
			else:
				ruleValues.append(token)

		negated = False
		tokenList = []
		for token in ruleValues:
			if token == '&' or token == '|':
					tokenList.append(token)
			elif token == '~':
					negated = True
			else:
				if negated:
					tokenList.append(self.opNot(token))
					negated = False
				else:
					tokenList.append(token)

		result = tokenList[0]
		if len(tokenList) > 1 and tokenList[1] == '&':
			op = self.opAnd
		else:
			op = self.opOr
		for i in range(2, len(tokenList)-2, 2):
			result = op(result, tokenList[i])
			if tokenList[i+1] == '&':
				op = self.opAnd
			else:
				op = self.opOr
		return op(result, tokenList[len(tokenList)-1])