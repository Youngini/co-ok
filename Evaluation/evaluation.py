#상품점수 score
#상세평가 detailed_eval

class Evaluation:
	def __init__(self, score, detailed_eval):
		self.score = score
		self.detailed_eval = detailed_eval

	def setScore(self, score):
		self.score = score

	def setDetailed_eval(self, detailed_eval):
		self.detailed_eval = detailed_eval

	def getScore(self):
		return self.score

	def getDetailed_eval(self):
		return self.detailed_eval

    