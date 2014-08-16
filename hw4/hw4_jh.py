class Node:
	def __init__(self, _value=None, _next=None):
		self.value = int(_value)
		self.next = _next
	
	def __str__(self):
		return str(self.value)

		

class LinkedList:
	def __init__(self):		# Initialize list and start a counter for the length
		self.head = None
		self.tail = None
		self.length = 0
	
	def length(self):		# Print the length counter
		return self.length
		
	def addNode(self, new_value):		# Add a new node at the end of the list and increase length
		# O(1) complexity
		node = Node(new_value)
		if self.head == None: self.head = node
		if self.tail != None: self.tail.next = node
		self.tail = node
		self.length += 1
	
	def addNodeAfter(self, new_value, after_node):		# add Node after by counting up the pointers until the desired position
		# O(n) complexity
		if after_node > self.length:
			print "Cannot add after node outside the list!"
		else:
			node = self.head
			count = 1
			while count is not after_node:
				node = node.next
				count += 1
			node.next = Node(new_value, node.next)
			
	def addNodeBefore(self, new_value, before_node):	# same as above with position-1
		# O(n) complexity
		if before_node > self.length+1:
			print "Cannot add before node outside the list!"
		else: self.addNodeAfter(new_value, before_node-1)
	
	def removeNode(self, node_to_remove):				# similar as above, to remove node
		# O(n) complexity
		if node_to_remove > self.length:
			print "Cannot remove node outside the list!"
		else:
			prev = None
			node = self.head
			count = 1
			while (node != None) and (count < node_to_remove):
				prev = node
				node = node.next
				count += 1
			if prev == None: self.head = node.next
			else: prev.next = node.next
			self.length -= 1
	
	def removeNodesByValue(self, value):			# again traverse through list until desired value found, then remove
		# O(n) complexity
		node = self.head
		if node.value == value:
			self.removeNode(node)
			if self.head is not None: self.removeNodesByValue(value)
			else: return None
		while node.next is not None:
			if node.next.value == value:
				node.next = node.next.next
			node = node.next
			if node is None: break
	
	def reverse(self):							# reverse by removing the head and moving it to the end
		# O(n) complexity
		for i in range(self.length-1):
			count = self.length
			node = self.head
			self.removeNode(self.head)
			self.addNodeBefore(node.value, count)
			count -= 1
	
	def __str__(self):
		# O(n) complexity
		node = self.head
		output = ""
		while node is not None:
			if node.next is not None: output += str(node.value) + ", "
			else: output += str(node.value)
			node = node.next
		return output
	
	def hasCycle(self):			# checks for cycles by traversing through the list and controlling whether number of steps increases list length at any point
		# O(n) complexity
		count = 0
		node = self.head
		while 1==1:
			node = node.next
			count += 1
			if count > self.length: 
				print "This linked list has a cycle!"
				break
			if node.next is None:
				print "This linked list does not have a cycle!"
				break