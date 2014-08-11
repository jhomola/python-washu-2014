import unittest
from hw2_jh import *

class hw2Test(unittest.TestCase):
	def setUp(self):
		self.portfolio = Portfolio()
		self.stocka = Stock(10, "AAPL")
		self.stockb = Stock (11.11, "XOM")
		self.muta = MutualFunds("SPY")
		self.mutb = MutualFunds("PTTRX")
		self.bonda = Bonds(12, "US10")
		self.bondb = Bonds(15, "UK30")
		
	def test_new_portfolio(self):
		self.assertEqual(0.00, self.portfolio.cash)
		
	def test_add_withdraw(self):
		self.portfolio.addCash(123)
		self.assertEqual(123.00, self.portfolio.cash)
		self.portfolio.addCash(1.11)
		self.assertEqual(124.11, self.portfolio.cash)
		self.portfolio.withdrawCash(2.11)
		self.assertEqual(122.00, self.portfolio.cash)
		self.portfolio.withdrawCash(123)
		self.assertEqual(-1.00, self.portfolio.cash)
		
	def test_ticker_and_prices(self):
		self.assertEqual("AAPL", self.stocka.ticker)
		self.assertEqual(11.11, self.stockb.price)
		self.assertEqual("SPY", self.muta.ticker)
		self.assertEqual(1, self.mutb.price)
		self.assertEqual("US10", self.bonda.ticker)
		self.assertEqual(15, self.bondb.price)
		
	def test_invest_and_sell(self):
		self.portfolio.addCash(1000)
		self.portfolio.buyStock(10, self.stocka)
		self.assertEqual({self.stocka: 10}, self.portfolio.investments["Stock"])
		self.assertEqual(1000.00-10*10, self.portfolio.cash)
		
		self.portfolio.buyMutualFunds(7.7, self.mutb)
		self.assertEqual({self.mutb: 7.7}, self.portfolio.investments["Mutual Funds"])
		self.assertEqual(900.00-7.7*1, self.portfolio.cash)
		
		self.portfolio.buyBonds(8, self.bondb)
		self.assertEqual({self.bondb: 8}, self.portfolio.investments["Bonds"])
		self.assertEqual(892.30-8*15, self.portfolio.cash)
		
		self.portfolio.sellStock(5, self.stocka)
		self.assertEqual({self.stocka: 5}, self.portfolio.investments["Stock"])
		self.assertTrue(self.portfolio.cash <= 772.30 + 5*10*1.5 and 772.30 + 5*10*.5  <= self.portfolio.cash)
		
	def test_history(self):
		self.portfolio.addCash(1000)
		self.portfolio.buyStock(13, self.stockb)
		self.portfolio.sellStock(7, self.stockb)
		self.portfolio.withdrawCash(37.77)
		self.assertTrue("New Portfolio started" in self.portfolio.history)
		self.assertTrue("Added $1000.00" in self.portfolio.history)
		self.assertTrue("Purchased $144.43 of XOM" in self.portfolio.history)
		self.assertTrue("Sold 7.00 shares of XOM" in self.portfolio.history)
		
	def test_print(self):
		self.portfolio.addCash(500)
		self.portfolio.buyStock(5, self.stocka)
		self.portfolio.buyMutualFunds(15, self.mutb)
		self.portfolio.buyBonds(33, self.bonda)		
		self.assertTrue("AAPL" in self.portfolio.__str__())
		self.assertTrue("PTTRX" in self.portfolio.__str__())
		self.assertTrue("US10" in self.portfolio.__str__())
		self.assertTrue("5" in self.portfolio.__str__())
		self.assertTrue("15" in self.portfolio.__str__())
		self.assertTrue("33" in self.portfolio.__str__())
		self.assertTrue("$39.00" in self.portfolio.__str__())
		
		
		
if __name__ == '__main__':
	unittest.main()
