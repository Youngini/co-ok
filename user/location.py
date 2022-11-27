class Location:
	def __init__(self, roadNameAddress, detailedAddress, zipCode):
		self.roadNameAddresss = roadNameAddress
		self.detailedAddress = detailedAddress
		self.zipCode = zipCode
	
	def setRoadNameAddress(self, roadNameAddress):
		self.roadNameAddress = roadNameAddress

	def setDetailedAddress(self, detailedAddress):
		self.detailedAddress = detailedAddress

	def setZipCode(self, zipCode):
		self.zipCode = zipCode

	def getRoadNameAddress(self):
		return self.roadNameAddress

	def getDetailedAddress(self):
		return self.detailedAddress

	def getZipcode(self):
		return self.zipCode
