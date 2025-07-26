#Loops and Iterations
n = 5

#Indefinite Loops
while n > 0:
    print(n)
    n = n -1
print('End!!')

n = 10
while n > 0:
    print(n)
    if(n == 8):
        n = n -1
        print('Continue Statement')
        continue
    if(n == 7):
        print('Break Statement')
        break
    n = n -1
print('End!!')


#Definite Loops
for i in [1, 2, 3, 4, 5]:
    print(i)
print('Closed!!')

friends = ['Raj', 'Ram', 'Zia']
for friend in friends:
    print(friend)
print('Closed!!!')
    
#Loop Idioms
largest = -1
sum = 0
for num in [1, -75, -6, 91 , 88, 67]:
    sum = sum + num
    if num > largest:
        largest = num
print('Largest:', largest)
print('Sum:', sum)
