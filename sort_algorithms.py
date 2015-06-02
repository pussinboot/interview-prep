###
##
# sorts
import random
# array to sort
tosort = [1,2,3,5,7,9,20,18]
random.shuffle(tosort)
# sorted array
correct = [1, 2, 3, 5, 7, 9, 18, 20]

def exch(a,i,j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp
	return a

##
# selection
def selection_sort(a):
	for i in range(len(a)):
		for j in range(i,len(a)):
			if a[i] > a[j]:
				a = exch(a,i,j)
	return a
print('selection sort works?',correct == selection_sort(tosort))

##
# insertion
def insertion_sort(a):
	for i in range(1,len(a)):
		for j in range(0,i):
			if a[i] < a[j]:
				a = exch(a,i,j)
	return a
print('insertion sort works?',correct == insertion_sort(tosort))

##
# shell
def shell_sort(a):
	gap = len(a) // 2
	while gap > 0:
		for i in range(gap,len(a)):
			j = i
			while j >= gap and a[j-gap] > a[i]:
				a = exch(a,i,j-gap)
				j -= gap
			gap //= 2
	return a
print('shell sort works?',correct == shell_sort(tosort))

##
# merge
def merge_sort(a):
	if len(a) <= 1:
		return a
	# split in halves
	m = len(a)//2
	l = merge_sort(a[:m])
	r = merge_sort(a[m:])
	# merge them back together
	return merge(l,r)
	
def merge(a,b):
	alim = len(a)
	blim = len(b)
	# not in place
	tor = []
	i, j = 0,0
	while True:
		if i >= alim:
			tor.extend(b[j:])
			break
		elif j >= blim:
			tor.extend(a[i:])
			break
		elif a[i] < b[j]:
			tor.append(a[i])
			i += 1
		else: # if a[i] > b[j]
			tor.append(b[j])
			j += 1
	return tor

print('merge sort works?',correct == merge_sort(tosort))

##
# quick
def quick_sort(a):
	return partition(a,0,len(a)-1)
def partition(a,start,stop):
	l,r = start, stop
	if r - l > 0:
		p = a[l]
		while l <= r:
			while a[l] < p:
				l += 1
			while a[r] > p:
				r -= 1
			if l <= r:
				a = exch(a,l,r)
				l += 1
				r -= 1
		a = partition(a,start,r)
		a = partition(a,l,stop)
	return a

print('quick sort works?',correct == quick_sort(tosort))

##
# heap
# nah