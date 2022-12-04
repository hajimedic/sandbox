#!/usr/bin/python3
# coding: utf-8
import random

# inputs
init_args = [random.randrange(1000) for _ in range(10)]


# sorting 1 (mergesort)
# ref. https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%B8%E3%82%BD%E3%83%BC%E3%83%88
print('init_args:\t', init_args)

def split(args: list) -> list:
	index = int(len(args) / 2)
	return args[:index], args[index:]

def merge(args1: list, args2: list) -> list:
	results = []

	len1, len2 = len(args1), len(args2)
	a, b = args1[0], args2[0]
	i = j = k = 0

	while 1:
		if a <= b:
			results.append(a)
			i += 1
			j += 1
			if j >= len1:
				break
			a = args1[j]
		else:
			results.append(b)
			i += 1
			k += 1
			if k >= len2:
				break
			b = args2[k]

	if j < len1:
		results += args1[j:]
	if k < len2:
		results += args2[k:]

	return results

def mergesort(args: list) -> list:
	if len(args) <= 1:
		return args

	args1, args2 = split(args)
	return merge(mergesort(args1), mergesort(args2))


print('results1:\t', mergesort(init_args))


# sorting 2 (comb sort)
# ref. https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%A0%E3%82%BD%E3%83%BC%E3%83%88
print('\ninit_args:\t', init_args)

def swap(args: list, i: int, j: int):
	temp = args[i]
	args[i] = args[j]
	args[j] = temp

def combsort(args: list) -> list:
	length = len(args)
	h = int(length * 10 / 13)
	while 1:
		swaps = 0
		for i in range(length):
			if i + h >= length:
				break
			if args[i] > args[i + h]:
				swap(args, i, i + h)
				swaps += 1
		if h == 1:
			if swaps == 0:
				break
		else:
			h = int(h * 10 / 13)

	return args

print('results2:\t', combsort(init_args))
