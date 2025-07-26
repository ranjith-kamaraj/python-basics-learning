#Variable names - case sensitive
#A mnemonic variable is a variable name chosen to be a memory aid, helping the programmer 
# quickly understand the variable's purpose. It's a way to make code more readable and easier
#  to maintain by using names that clearly indicate what data the variable holds. 

spam = 2
Spam = 3
SPAM = 4

#Assignment Statement
value = 5

#Expression (+, _, * , etc...) - It's on the right hand side
val = value  + 5

a = 5
b = 6

c = a + b
d = a -b
e = a * b
f = a / b #division
g = a % b #reminder
h = a ** b #exponential power


#Operator precedence -> Paranthesis + Mul + Add + Left to Right
x = 1 + 2 ** 3 / 4 * 5
print(x)

y = 'Hello ' + 'World'
z = 'eeee' + 1 #error
type(z)

#Type conversions
f = float(123) #123.0
i = int(1234.988) #1234

#integer division is different between python 2.0 and 3.0 - verify it

#user input - always returns string
nam = input('Hi!!') #user inputs in keyboard as 'Hello'
print('Welcome', nam) #Welcome Hello -> Every comma add an space
