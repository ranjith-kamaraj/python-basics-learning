#Functions used defined by keyword 'def'
#For multiple words separate from '_' ex: greet_user

def thing():
    print('Hello')
    print('Fun')

thing()
print('**************')
thing()

#pre-defined functions
big = max('Hello world')
print(big)

small = min('Hello-world')
print(small)


#positional arguments
def add_data(a, b):
    print(a + b)

add_data(5, 7)

#keyword arguments
def add_data2(a, b):
    print(a + b)

add_data2(b=10, a=15)

def print_hello():
    return 'Hello'

print(print_hello(), 'World')
print(print_hello(), 'People')


#May work but try to use - '_'
def greetUsr():
    return 'Hello User'
print(greetUsr())


    








