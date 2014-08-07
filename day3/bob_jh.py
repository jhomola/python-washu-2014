class Bob():	
	def __init__(self, ask):
		self.ask = ask

	def say(self=""):
		ask_caps= self.ask.upper()
		if "?" in self.ask:
			return "Sure"
		elif len(self.ask)<1:
			return "Fine. Be that way!"
		elif ask_caps==self.ask:
			return "Woah, chill out!"
		else:
			return "Whatever"


quest = Bob("")
print quest.say()

		