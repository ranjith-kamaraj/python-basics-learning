#Logical Operators

a = True
b = False
c = True

if a and c:
    print('And - all condtion to match')

if a or b:
    print('OR - any one condtion to match')

if a and not b:
    print('Not - Basically inverse the any boolean value')



#Comparision operators
temp = 30

if temp == 30:
    print('== Equal Operator')

if temp != 30:
    print('!= Not Equal Operator')

if temp >= 30:
    print('>= Greater than and  Equal Operator')

#Weight conversion
unit = int(input("Weight:"))
method = input("(L)bs or (K)gs:")

if method.upper() == 'L':
    converted = unit * 0.45
    print(f'Your: {converted}')
else:
    converted = unit / 0.45 #/-> will convert into float and //-> will convert into integer
    print(f'Your Float: {converted}')
    converted = unit // 0.45 #/-> will convert into float and //-> will convert into integer
    print(f'Your Int: {converted}')
