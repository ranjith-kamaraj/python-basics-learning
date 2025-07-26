#Functions used defined by keyword 'def'

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

def add_data(a, b):
    print(a + b)

add_data(5, 7)


def print_hello():
    return 'Hello'

print(print_hello(), 'World')
print(print_hello(), 'People')
