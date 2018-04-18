#!/usr/bin/python
# -*- coding: UTF-8 -*-

def search_binary( mylist, item):
	low = 0
	high = len(mylist)-1

	while 1:
		mid = (low + high)/2
		guess = list1[mid]

		if guess == item:
			return mid - 1
		elif guess > item:
			high = mid + 1
		elif guess < item:
			low = mid

	return mid

list1 = [1,2,3,4,5]
a = search_binary(list1, 1)

print a 
