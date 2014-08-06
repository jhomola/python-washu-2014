def binarify(num): 
  """convert positive integer to base 2"""
  if num<=0: return '0'
  x = 0
  y = 2
  while y>1:
	y = num / 2**x
	x = x+1
  digits = ["1"]
  num = num - 2**(x-1)
  for i in range(x-2,-1,-1):
	if num / 2**i == 1:
		digits.append("1")
		num = num - 2**i 
	else:
		digits.append("0")
  return ''.join(digits)

def int_to_base(num, base):
  """convert positive integer to a string in any base"""
  if num<=0:  return '0' 
    x = 0
  y = 2
  while y>1:
	y = num / base**x
	x = x+1
  digits = ["1"]
  num = num - base**(x-1)
  for i in range(x-2,-1,-1):
	if num / base**i != 0:
		qqq = num / base**i
		qqq = str(qqq)
		digits.append(qqq)
		num = num - base**i 
	else:
		digits.append("0")
  return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0
  result = 0
  length = len(string)
  for i in range(length):
	result = result + int(string[i]) * base ** (length-i-1)
  return result 

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  result = int_to_base(tmp, base1)
  return result 

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  result = int_to_base(tmp, base1)
  return result 

def romanify(num):
  """given an integer, return the Roman numeral version"""
  result = ""
  return result