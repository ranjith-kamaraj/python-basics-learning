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



name = 'Ranjith'
age = 25
weight = 86.77
is_active = True


if age > 30:
  print('Age High')
else: 
  print('Hii Hellooo!!')

fruits = ['Apple', 'Grapes', 'Mango']

for i in fruits:
  print(i)

n = 5
while n > 0:
  print(n)
  n = n -1 

person = {
    "name": "Ranjith",
    "age": 30,
    "is_student": False
}

for key, value in person.items():
  print(key, ':',value)

for j in person.values():
  print(j)

for j in person:
  print(j)


fruits1 = ['Apple', 'Grapes', 'Mango']
fruits1.append('Tomato')
fruits1.remove('Grapes')
print(fruits1[0])
print(fruits1[-1])


person1 = {
    "name": "Ranjith",
    "age": 30,
    "is_student": False
}

person1['weight'] = 77.88
print(person1)
print(person1['name'])
