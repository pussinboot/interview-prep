#######
# # #
#
# implementation of a few data structures as practice to prepare for interview(s)
# along with some notes : )

###
# here is a node, very useful for implementing all sorts of things
class Node():
	def __init__(self,key,val,next=None):
		self.key = key
		self.val = val
		self.next = None
	def get_val(self):
		return self.val
	def set_val(self,newval):
		self.val = newval
	def get_key(self):
		return self.key
	def get_next(self):
		return self.next
	def set_next(self,newnext):
		self.next = newnext

###
# Queue - FIFO
class Queue():
	def __init__(self):
		self.head = None
	def enqueue(self,node):
		if self.head is None:
			self.head = node
		else:
			last = self.head
			while last.get_next() is not None:
				last = last.get_next()
			last.set_next(node)
	def dequeue(self):
		tor = self.head
		if self.head is not None: 
			self.head = self.head.get_next()
		return tor
###
# Stack - LIFO
class Stack():
	def __init__(self):
		self.head = None
	def push(self,node):
		if self.head is None:
			self.head = node
		else:
			curhead = self.head
			node.set_next(curhead)
			self.head = node
	def pop(self):
		tor = self.head
		self.head = self.head.get_next()
		return tor

# fun example of stack
# 2 stack expression evaluator

###
# Linked List
# useless to implement just look at any of the above 2...
		
###
# BST

###
# 2-3 Tree

###
# Red Black BST

###
# Heap

###
# Trie

###
# Hash Table
