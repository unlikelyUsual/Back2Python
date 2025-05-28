# Tuples are list but immutable
# doesn't have insert, and mutable function
numbers = (1, 2, 3, 2, 2)

numbers[0] = 10 # throw error, immutable

numbers.count(2) # counts the number of occurance of 2 : 3

numbers.index(2) # first index of 2 : 1