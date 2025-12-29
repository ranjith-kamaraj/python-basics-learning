class PointToPoint:
  
  #construtor
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def Move(self):
    print('Move')

  def draw():
    print('Draw')


point1 = PointToPoint()
point1.Move()
point1.x = 10
print(point1.x)

#New class - It won't inherit anything from above point
point2 = PointToPoint()
#point2.x = 10
print(point2.x) #will fail

#with constructor
point2 = PointToPoint(30, 40)
print(point2.x)
point2.y = 50
print(point2.y)
    