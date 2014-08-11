from random import *

class Portfolio():

	def __init__(self):					# Creates empty new portfolio with no funds and no investments
		self.cash = 0.00
		self.history = "New Portfolio started. \t \t Balance: $0.00"
		self.investments = {"Stock" : {}, "Mutual Funds" : {}, "Bonds" : {}}

	def addCash(self, moneyin):			# Adds cash and displays new balance
		self.cash += int(moneyin*100)/100.00
		self.history += "\n Added $%.2f. \t \t Balance: $%.2f" %((int(moneyin*100)/100.00), self.cash)
		
	def withdrawCash(self, moneyout):	# Withdraws cash and displays new balance
		self.cash -= int(moneyout*100)/100.00
		self.history += "\n Withdrew $%.2f. \t \t Balance: $%.2f" %(int(moneyout*100)/100.00, self.cash)
		
	def invest(self, shares, investmenttype):	# Sets up a generic buying method for different investment classes specified below
		if investmenttype in self.investments[investmenttype.TypeName()]:
			self.investments[investmenttype.TypeName()][investmenttype] += shares
		else: self.investments[investmenttype.TypeName()][investmenttype] = shares
		self.history += "\n Purchased $%.2f of %s." % ((shares*investmenttype.price), investmenttype.ticker)
		self.withdrawCash(shares*investmenttype.price)
		
	def sell(self, shares, investmenttype):		# Sets up a generic selling method for different investment classes specified below
		self.investments[investmenttype.TypeName()][investmenttype] -= shares
		self.history += "\n Sold %.2f shares of %s." % (shares, investmenttype.ticker)
		self.addCash(shares*investmenttype.SellFor())
	
	# While the generic functions work for Mutual Funds and Bonds, Stocks can only be purchased/sold in whole units
	buyMutualFunds = buyBonds = invest
	sellMutualFunds = sellBonds = sell	
	def buyStock(self, shares, investmenttype): self.invest(int(shares), investmenttype)
	def sellStock(self, shares, investmenttype): self.sell(int(shares), investmenttype)
	
	def history(self): print self.history		# Printing the history that is created with every transaction
		
	def __str__(self):							# Creating the normal print output
		portprint = "Cash:\t$%.2f \n" % self.cash
		for i in self.investments:
			portprint += "%s: \n" %i
			if not self.investments[i]: portprint += "\t None \n"
			for j in self.investments[i]: portprint += "\t" + str(self.investments[i][j]) + "\t" + str(j.ticker) + "\n"
		return portprint

		
		
		
class InvestmentType():			# Class structures for the different types of investment
	def __init__(self, price, ticker):
		self.price = price
		self.ticker = ticker
		
		
class Stock(InvestmentType):
	def __init__(self, price, ticker):
		InvestmentType.__init__(self, price, ticker)
		
	def TypeName(self): return "Stock"
	
	def SellFor(self): return int(100*uniform(self.price*.5, self.price*1.5))/100.00
	
	
class MutualFunds(InvestmentType):
	def __init__(self, ticker):
		InvestmentType.__init__(self, 1.0, ticker)
		
	def TypeName(self): return "Mutual Funds"
	
	def SellFor(self): return int(100*uniform(self.price*.9, self.price*1.2))/100.00
	
	
class Bonds(InvestmentType):
	def __init__(self, price, ticker):
		InvestmentType.__init__(self, price, ticker)
		
	def TypeName(self): return "Bonds"
	
	def SellFor(self): return int(100*uniform(self.price*.7, self.price*1.35))/100.00 	# New hypothetical price distribution for bonds