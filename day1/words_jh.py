file = open('words.txt')

for line in file:
  word = line.strip()
  print word
  
def has_no_e(wordtest):
	return "e" not in wordtest
	
def uses_only(string, check):
  test = []
  for letter in string:
	test.append(letter in check)
  print sum(test) == len(string)
  
def uses_all(string, check):
  test = []
  for letter in check:
	test.append(letter in string)
  print sum(test) == len(string)
  
def is_abecedarian(string):
  test = []
  for i in range(len(string)):
	if i < (len(string)-1):
		test.append(string[i] < string[i+1])
  print sum(test) == len(string)-1
