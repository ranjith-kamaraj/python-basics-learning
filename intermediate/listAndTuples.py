#2 - Dimensional List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])
matrix[0][1] = 25
print(matrix[0][1])
print(matrix)

#print all item
for row in matrix:
    for item in row:
        print(item)


#List Methods
# A list is a collection of values that can be of any data type, including strings, integers, floats, and other lists. 
# Lists are defined by enclosing a sequence of values in square brackets [].
# Lists are Mutable, Indexable, Ordered, Heterogeneous.
print("*** List Start ***")
numbers = [1, 4, 5, 7, 9, 44, 5]
numbers.append(76)
numbers.insert(3, 23)
numbers.remove(7)

print(numbers.index(9))
print(9 in numbers)
print(numbers.count(5))
print(len(numbers))

#asc
numbers.sort()
print('Asc:',  numbers)
numbers.reverse()
print('Desc:'  ,  numbers)

#copy - It will behave two independent variables
numbers1 = numbers.copy()
numbers.append(24)
print(numbers)
print(numbers1)

print("*** List Ends ***")

#Tuples - Are similar to list represents in () format
#A collection of values that can be of any data type, defined by enclosing a sequence of values 
# in parentheses (). Tuples are immutable, ordered, indexable, and homogeneous.
print("*** Tuples Start ***")
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Output: 1

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:3])  # Output: (2, 3)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
my_tuple = tuple1 + tuple2
print(my_tuple)  # Output: (1, 2, 3, 4, 5, 6)

my_tuple = (1, 2, 3)
new_tuple = my_tuple * 2
print(new_tuple)  # Output: (1, 2, 3, 1, 2, 3)

tuple1 = ('a', 'b')
tuple2 = tuple1 * 2
print(tuple2)  # Output: ('a', 'b', 'a', 'b')

my_tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True

my_tuple = (1, 2, 3, 4, 5)
print(6 in my_tuple)  # Output: False

