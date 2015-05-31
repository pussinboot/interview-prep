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
# just kidding, there's fun ways to  insert and delete and find things

###
# Here is a tree node, useful for all sorts of trees
class TreeNode():
	def __init__(self,key,val,left=None,right=None):
		self.key = key
		self.val = val
		self.left = left
		self.right = right
	def get_left(self):
		return self.left
	def set_left(self,newleft):
		self.left = newleft
	def get_right(self):
		return self.right
	def set_right(self,newright):
		self.right = newright
	def get_val(self):
		return self.val
	def set_val(self,newval):
		self.val = newval
	def get_key(self):
		return self.key
	def compare_to(self,node):
		return self.val - node.get_val()

###
# BST
class BST():
	def __init__(self):
		self.root = None
	def insert(self,node):
		if self.root is None:
			self.root = node
		else:
			cur = self.root
			while True:
				#compare till you find right spot
				comparison = curr.compare_to(node)
				if comparison > 0:
					if curr.get_left() is None:
						curr.set_left(node)
						break
					else:
						curr = curr.get_left()
				else:
					if curr.get_right() is None:
						curr.set_right(node)
						break
					else:
						curr = curr.get_right()


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
