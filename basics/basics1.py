print("Ranjith Kamaraj!")
print('Hello world!!')

#
# 1. python interpeter will run the code line by line
# 2. It's an case sensitive language - always use lowercase letter when defining variables
#

#expression - piece of code it's produces the value
print('*' * 10) 

#variables - It will store the value of binary expression ex: 1011111
price = 100
rating = 4.7
name = 'Raj'
is_published = True

print(is_published) 

#user input
name = input('What is your name? ')
print('Hi ' + name)

#type conversion - int(), float(), bool()
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2026 - int(birth_year)
print(age)

#strings
course = "Python's for Beginners"
print(course[0])
print(course[-1])#index from the last one
print(course[0:5])
print(course[2:])
print(course[:5])
another = course[:]#clone or copy of the variable
print(another)

course1 = 'Python for "Beginners"'
multiple_lines = ''' Hi, 

Good Morning!!

Thank You!
'''

print(multiple_lines)


#formatted strings
first = 'Ajith'
last = 'Kumar'

msg = f'{first} [{last}]  is a coder' 

print(msg)