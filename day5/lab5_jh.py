from math import *
from itertools import *

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

square = {}
n = 256


for i in range(1,n):
  if(i % sqrt(n) != 0): square = makeLink(square, i, i+1)
  if (i < (n - sqrt(n) + 1)): square = makeLink(square, i, (i + int(sqrt(n))))

# Show our graph
print square

# How many nodes?
print len(square)

# How many edges?
print sum([len(square[node]) for node in square.keys()])/2 

# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

makeLink(movies, dh, rd) # Wag the Dog
makeLink(movies, rd, ms) # Marvin's Room
makeLink(movies, dh, ss) # Midnight Mile
makeLink(movies, dh, jr) # Hook
makeLink(movies, dh, kb) # Sleepers
makeLink(movies, ss, jr) # Stepmom
makeLink(movies, kb, jr) # Flatliners
makeLink(movies, kb, ms) # The River Wild
makeLink(movies, ah, ms) # Devil Wears Prada
makeLink(movies, ah, jr) # Valentine's Day

print movies

# How many nodes in movies?
nodesMovies = len(movies)

# How many edges in movies?
edgesMovies = sum([len(movies[node]) for node in movies.keys()])/2
print "There are %d nodes and %d edges in the Movie tree" % (nodesMovies, edgesMovies)

def tour(graph, nodes):
	tour_list = []
	for i in range(len(nodes)):
		node = nodes[i] 
		if node in graph.keys():
      		#print node 
			tour_list.append(node)
		else:
      		#print "Node not found!"
			break 
		if i+1 < len(nodes):
			next_node = nodes[i+1]
		if next_node in graph.keys():
			if next_node in graph[node].keys():
				pass 
			else:
          #print "Can't get there from here!"
				break 
	#print tour_list
	if len(tour_list) == 7: print tour_list
	if len(tour_list) == 7: 
		return tour_list
	else: pass



# TODO: find an Eulerian tour of the movie network and check it 

perm_Movies = list(permutations(movies.keys()))

all_paths = []

for i in range(len(perm_Movies)):
	if (tour(movies, perm_Movies[i]) != None): all_paths.append(tour(movies, perm_Movies[i]))

#print all_paths