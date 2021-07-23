'''
Author: Eduardo Ortega
Date Created: 7/23/2021
'''
#Import statements
import math
import mmh3
import bitarray

class BloomFilter(object):
	def __init__(self, num_items, prob_fp):
		# False Postive rate
		self.prob_fp = prob_fp

		# Size of bit array for Bloom Filter
		self.size = self.get_size(num_items, prob_fp)

		# Count of hash functions and bit array based on previously declared size
		self.hash_func_count = self.get_hash_func_count(self.size, num_items)
		self.bit_array = bitarray.bitarray(self.size)

		# Initialize the bits of the bloom filter to be used
		self.bit_array.setall(0)

	def get_size(self, num_item, prob_fp):
		size = -(num_item * math.log(prob_fp))/(math.log(2)**2)
		return int(size)

	def get_hash_func_count(self, size, nums_items):
		hash_count = (size/nums_items) * math.log(2)
		return int(hash_count)

	def check(self, item):
		for hash_func in range(self.hash_func_count):
			check_entry = mmh3.hash(item, hash_func) % self.size
			if self.bit_array[check_entry] == False:
				return False
			return True

	def add(self, item):
		filter_list = []
		for hash_func in range(self.hash_func_count):
			entry = mmh3.hash(item, hash_func) % self.size
			filter_list.append(entry)
			self.bit_array[entry] = True
		
