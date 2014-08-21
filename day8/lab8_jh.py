import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = sqlalchemy.create_engine('sqlite:////Users/Jona/Documents/Uni/WashU2/4625-Programming/python-washu-2014/day8/geog.db', echo=False)

Base = declarative_base() 

# Schemas
class Region(Base):
  __tablename__ = 'regions'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  departments = relationship("Department")

  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return "<Region('%s')>" % self.id 

class Department(Base):
  __tablename__ = 'departments'

  id = Column(Integer, primary_key=True)
  deptname = Column(String)
  region_id = Column(Integer, ForeignKey('regions.id')) 
  towns = relationship("Town")

  def __init__(self, deptname):
    self.deptname = deptname 

  def __repr__(self):
    return "<Department('%s')>" % self.id 

class Town(Base):
  __tablename__ = 'towns'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  population = Column(Integer)
  dept_id = Column(Integer, ForeignKey('departments.id'))

  def __init__(self, name, population):
    self.name = name 
    self.population = population

  def __repr__(self):
    return "<Town('%s')>" % (self.name)

class Distance(Base):
  __tablename__ = 'distances'

  id = Column(Integer, primary_key=True)
  towndepart = Column(String, ForeignKey('towns.name'))
  townarrive = Column(String, ForeignKey('towns.name'))
  # could also use id's 
  distance = Column(Integer)

  td = relationship("Town", 
    primaryjoin= towndepart == Town.name)
  ta = relationship("Town", 
    primaryjoin = townarrive == Town.name)
  
  def __init__(self, distance):
    self.distance = distance 

  def __repr__(self):
    return "<Distance('%s', '%s', '%s')>" % (self.towndepart, self.townarrive, self.distance)



#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# Create regions
reg1 = Region('Region 1')
reg2 = Region('Region 2')
reg3 = Region('Region 3')
session.add_all([reg1, reg2, reg3])

# Create departments, nested in regions
dept1 = Department('Department 1')
reg1.departments.append(dept1)

dept2 = Department('Department 2')
reg1.departments.append(dept2)

dept3 = Department('Department 3')
reg3.departments.append(dept3)

dept4 = Department('Department 4')
reg2.departments.append(dept4)

session.add_all([dept1, dept2, dept3, dept4])

# TODO: Create towns, nested in departments
a = Town("A", 110000)
dept1.towns.append(a)

b = Town("B", 80000)
dept3.towns.append(b)

c = Town("C", 300000)
dept3.towns.append(c)

d = Town("D", 50000)
dept2.towns.append(d)

e = Town("E", 113000)
dept2.towns.append(e)

f = Town("F", 70000)
dept1.towns.append(f)

session.add_all([a,b,c,d,e,f])

ae = Distance(50)
ae.td, ae.ta = a, e 

af = Distance(60)
af.td, af.ta = a, f 

bc = Distance(50)
bc.td, bc.ta = b, c 

bd = Distance(60)
bd.td, bd.ta = b, d 

cb = Distance(50)
cb.td, cb.ta = c, b 

db = Distance(60)
db.td, db.ta = d, b 

de = Distance(30)
de.td, de.ta = d, e 

ea = Distance(50)
ea.td, ea.ta = e, a 

eb = Distance(60)
eb.td, eb.ta = e, b 

ed = Distance(30)
ed.td, ed.ta = e, d 

ef = Distance(100)
ef.td, ef.ta = e, f 

fa = Distance(60)
fa.td, fa.ta = f, a 

session.add_all([ae, af, bc, bd, cb, db, de, ea, eb, ed, ef, fa])

session.commit()

# Some example querying
print "\n******\nPrint Towns and Populations\n******\n"
for town in session.query(Town).order_by(Town.id):
  print town.name, town.population

# TODO: 
# 1. Display, by department, the cities having more than 100000 inhabitants.
print "\n******\nTODO 1\n******\n"
for town in session.query(Town).filter(Town.population > 100000).order_by(Town.dept_id):
  print town.name, town.population, "Department: ", town.dept_id

# 2. Display the list of all the one-way connections between two cities for which the population of one of the 2 cities is lower than 80000 inhabitants. 
print "\n******\nTODO 2\n******\n"
for town, dist in session.query(Town, Distance).filter(Town.population < 80000).filter(or_(Distance.townarrive==Town.name, Distance.towndepart==Town.name)).order_by(Distance.distance):
  print "Population of", town.name, ":", town.population, "Distance from", dist.towndepart, "to", dist.townarrive, ":", dist.distance
  
# 3. Display the number of inhabitants per department (bonus: do it per region as well). 
print "\n******\nTODO 3\n******\n"
pop1 = 0
pop2 = 0
pop3 = 0
pop4 = 0
for town in session.query(Town).order_by(Town.dept_id):
  if town.dept_id==1: pop1 += town.population
  if town.dept_id==2: pop2 += town.population
  if town.dept_id==3: pop3 += town.population
  if town.dept_id==4: pop4 += town.population  
  #print town.name, town.population, "Department: ", town.dept_id
print "Population of Department 1: %i" % pop1
print "Population of Department 2: %i" % pop2
print "Population of Department 3: %i" % pop3
print "Population of Department 4: %i" % pop4
# hint: use func.sum