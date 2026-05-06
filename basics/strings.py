#string methods
print('string methods')
course = 'Python for Beginners'

print(len(course))
#Some function depends on some object/others called as 'Methods'
#Ex: print(), len() - General functions  not depend on others
#Ex: .upper(), .lower() - Depend on String values so called as Methods

print(course.upper())
print(course.lower())
print(course.find('o'))
print(course.find('for'))
print(course.replace('for', 'to'))
print('Python' in course)

s = "Hello World"  # define a variable s to hold our string 'Hello world'
print(s)  			# output should be Hello World as per the definition (no changes in original data type due to no method call on it. As str is immutable, this will print initial value of any unmodified object). 1st example for capitalize() function called with s because if we don't pass an argument then 's'.capitalize().
print(s.upper())  	# output should be HELLO WORLD as the .upper method converts all characters to upper case and returns a new string (same object is modified). 2nd example for capitalizing first character in each word of s using '.lower()' followed by 'capitalize().
print(s.replace("World", "Python"))	# output should be Hello Python as replace replaces all occurrences from the second argument with third one and returns a new string (same object is modified). 3rd example for replacing characters in s using '.split()' followed by 'upper()).join('-')'.
print(s.lower().replace("hello", "hi"))	# output should be hi WORLD as lower converts all letters to lower case and then replace method replaces the first occurrence of second argument with third one, returning a new string (same object is modified). 4th example for replacing in s using '.split()' followed by 'upper().replace(" ", "")'.
print(s.startswith('Hello'))		# output should be True as startswith method checks if the given prefix/substring from str variable starts at index i and ends before n characters, returning a boolean value (whether it started or not). 5th example for checking whether s is alphanumeric using '.isalnum()'.
print(s.split())				# output should be ['Hello', 'World'] as split splits string on space ('') into list and returns an iterable object of strings, if no separator provided then default delimiter ie a blank ("") is used to separate the characters in each word (if there are multiple spaces between words it will still only consider one).
print(s.find('o'))				# output should be 4 as find method returns index at which first occurrence of given substring/character from str variable starts, returning an integer value if not found then -1 is returned indicating no such character in the string (same object remains unchanged due to finding operation on it).
print(s.isalnum())				# output should be False as isnumeric method checks whether all characters are numbers or letters and returns a boolean respectively, for example here s has numerical digits only so will return false but alphanum can contain both numerics & non-numerical chars ie '12345' also contains lowercase/upper case etc.
print(s.__len__())				# output should be 9 as length method returns the number of characters in a string, for this we are getting total count not individual character counts and hence will return its actual size or no of elements (same object remains unchanged due to fetching operation on it). Also __getitem__(key) can also give us element at given index.
print(s + '12345')				# output should be Hello World as concatenation operator in python is used with strings and returns new string which holds the combination of both, here s itself will get appended by ‘'+’ followed by a series/number ie ('Hello world'->-> 	'helloWorld12345').
print(s * -1)					# output should be WORLD HELLO as in python multiplication operator is used with string and returns new modified version of the same object. However, s itself will get reversed hence 'WORLD' which was initially becomes last character first ie '->-> 	‘worldHEllo’ (s stays unchanged).
print('H'.join(['E', 12345]))	# output should be HELLO as join method combines given iterable objects into one string with the specified delimiter and returns a new modified version of s. In this case, it is joining '['Hello World' to make final result ie ->-> 	'HElloWorld12345').

