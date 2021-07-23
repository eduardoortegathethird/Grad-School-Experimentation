'''
Author: Eduardo Ortega
Date: 7/23/2021
'''
# Import Statements
from bloom_filter import BloomFilter
import random

#Variables to use
number_of_items = 20
false_positive_rate = 0.05

def print_information(bloom_filter):
	print("=================================================")
	print(f"Bit Array Size is {bloom_filter.size}")
	print(f"False Positive Rate is {bloom_filter.prob_fp}")
	print(f"Number of Hash Functions is {bloom_filter.hash_func_count}")
	print("=================================================")

def main():
	bloom_filter = BloomFilter(number_of_items, false_positive_rate)
	print_information(bloom_filter)
	words_to_be_added = ['New York', 'Seattle', 'Los Angeles', 'San Diego', 'Mission Beach',
						'Pacific Beach', 'La Jolla', 'Sorrento Valley', 'Gaslamp Quarter', 'Chula Vista',
						'Point Loma', 'Ocean Beach', 'Poway', 'Carlsbad', 'Linda Vista',
						'Santee', 'Julian', 'La Mesa', 'National City', 'Barrio Logan']
	words_not_added = ['red', 'blue', 'yellow', 'orange', 'purple',
						'white', 'black', 'grey', 'navy', 'teal',
						'green', 'cyan', 'rose', 'gold', 'brick']
	
	for word in words_to_be_added:
		bloom_filter.add(word)

	test_words = words_to_be_added[:10] + words_not_added
	random.shuffle(test_words)
	for word in test_words:
		if bloom_filter.check(word):
			if word in words_not_added:
				print(f"{word} is a found! NOT, this is a false positive")
			else:
				print(f"{word} is found!")
		else:
			print(f"{word} is not there!")

if __name__=="__main__":
	main()
