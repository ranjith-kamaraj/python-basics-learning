x = 2
x = x + 3
print(x)

#Conditional Statement
x = 5
if(x < 20):
    print('Smaller')
elif(x > 20):
    print('Bigger')
print('Finish!')

#Repeat Statement
n = 5
while n > 0:
    print(n)
    n = n-1
print('Balstoff')


##Print Multiple Lines
course = '''
Hi,
    How are you doing?

Thank You!!
'''
print(course)

#Indexing
course = 'Python for Beginners'

print(course[-2])#reverse
print(course[0:4])

copyCourse = course[:]#copy the value
print(copyCourse)
print(course[2:-4])

print(f'{copyCourse} and {course}')