x = 5

#Indent and deindent - the space added after all the conditions 
if x > 10:
    print('Higher') 
    if x > 100:
        print('More Higher')
elif x < 10:
    print('Smaller')
else:
    print('Finish')
print('Conditional statement')


#try-catch logic

x = 'Test'
try:
    y = int(x)
    print(y)
except:
    y = -1
finally:
    print(' Always runs, whether exception occurred or not')
print('Done', y) #-1



x = '123'
try:
    y = int(x)
    print(y)
except:
    y = -1
finally:
    print(' Always runs, whether exception occurred or not')
print('Done', y) #123

