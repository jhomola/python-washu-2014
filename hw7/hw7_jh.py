import sqlalchemy, csv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/Jona/Documents/Uni/WashU2/4625-Programming/python-washu-2014/hw7/hw7_jh.db', echo=False)

Base = declarative_base()

# Schemas
class Scrapes(Base):
	__tablename__ = 'scrapes'

	id = Column(Integer, primary_key=True)
	is_post = Column(Integer)
	publish_date = Column(String)
	author = Column(String)
	post_title = Column(String)
	comment_count = Column(Integer)
	source = Column(String)

	def __init__(self, is_post, publish_date, author, post_title, comment_count, source):
		self.is_post = is_post
		self.publish_date = publish_date
		self.author = author
		self.post_title = post_title
		self.comment_count = comment_count
		self.source = source

	def __repr__(self):
		return "Blogpost %i" % self.id 

class Follower(Base):
	__tablename__ = 'followers'
	
	id = Column(Integer, primary_key=True)
	user_id = Column(String)
	follower_count = Column(Integer)
	
	def __init__(self, user_id, follower_count):
		self.user_id = user_id
		self.follower_count = follower_count
	
	def __repr__(self):
		return "Twitter User %s" % self.user_id
		
class Active(Base):
	__tablename__ = 'active'
	
	id = Column(Integer, primary_key=True)
	user_id = Column(String)
	twentieth_tweet = Column(String)
	
	def __init__(self, user_id, twentieth_tweet):
		self.user_id = user_id
		self.twentieth_tweet = twentieth_tweet
	
	def __repr__(self):
		return "Twitter User %s" % self.user_id
		
#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

#Blogposts
#reg1 = Region('Region 1')
#reg2 = Region('Region 2')
#reg3 = Region('Region 3')
#session.add_all([reg1, reg2, reg3])

reader1 = csv.DictReader(open("hw5sorted_jh.csv"))
blog_scrapes = []
for line in reader1:
	blog_scrapes.append(Scrapes(line["is_post"], line["publish_date"], line["author"], line["post_title"], line["comment_count"], line["url"]))
session.add_all(blog_scrapes)


reader2 = csv.DictReader(open("twitter_active.csv"))
active = []
for line in reader2:
	active.append(Active(line["user_id"], line["20th_tweet"]))
session.add_all(active)


reader3 = csv.DictReader(open("twitter_popular.csv"))
popular = []
for line in reader3:
	popular.append(Follower(line["user_id"], line["followers"]))
session.add_all(popular)


session.commit()


# Some example querying
print "\n******\nPrint first 12 scraped post titles with author\n******\n"		
# As discussed in class, this includes some 'None's because of faulty html debugging in python
for post in session.query(Scrapes).filter(Scrapes.id < 13).order_by(Scrapes.id):
  if post.author != None: print post.author, post.post_title
  
print "\n******\nPrint all posts not by Gelman\n******\n"
for post in session.query(Scrapes).filter(Scrapes.author != "Andrew").order_by(Scrapes.id):
  print post.author, post.post_title
  
print "\n******\nPrint ten least active accounts, sorted activity\n******\n"
for account in session.query(Active).order_by(Active.twentieth_tweet)[0:10]:
  print account.user_id, account.twentieth_tweet
  
print "\n******\nPrint ten least followed accounts, sorted by number of followers\n******\n"
for account in session.query(Follower).order_by(Follower.follower_count)[0:10]:
  print account.user_id, account.follower_count
  
print "\n******\nPrint all accounts and number of followers, if over 1000 followers\n******\n"
for account in session.query(Follower).filter(Follower.follower_count > 1000).order_by(Follower.follower_count):
  print account.user_id, account.follower_count