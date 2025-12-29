from pathlib import Path

#Absolute Path: it's from root directory - /Users/ranjithkamaraj/WORKSPACE/python-basics-learning/module/math.py
#Relative Path: It's from file - module/math.py

path = Path('intermediate')
print(path.exists())

path = Path('mail')
print('Create Mail Dir:', path.mkdir())
print('Delete Mail Dir:', path.rmdir())

#access global files
path = Path()
for file in path.glob('*.*'):
    print(file)

for file in path.glob('*'):
    print(file)


