class School():
	def __init__(self, schoolname):
		self.schoolname = schoolname
		self.db = {}
		
	def add(self, kidsname, grade):			# add kid either to new or existing grade
		if grade not in self.db.keys(): 
			self.db[grade] = {kidsname}
		else: self.db[grade].add(kidsname)
	
	def grade(self, testgrade):				# list existing students in a grade or return none
		if testgrade not in self.db:
			return None
		return self.db[testgrade]
	
	def sort(self):							# sort students by grade and name
		students_sort = {}
		for grade in sorted(self.db.keys()):
			students_sort[grade] = tuple(sorted(self.db[grade]))
		return students_sort