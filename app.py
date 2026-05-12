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



import sys

# Display all command line arguments
print("Script name:", sys.argv[0])
print("All arguments:", sys.argv)

# Check if arguments are provided
if len(sys.argv) > 1:
  name = sys.argv[1]
  print(f"Hello, {name}!")
else:
  print("No name provided. Usage: python script.py <name>")


