def distance(x1, y1, x2, y2):
     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5

 def triangle_perimetr(x1, y1, x2, y2, x3, y3):
     a = distance(x1, y1, x2, y2)
     b = distance(x2, y2, x3, y3)Больше действий
     c = distance(x3, y3, x1, y1)
     return a + b + c

 print(triangle_perimetr(1, 2, 4, 5, 6, 7))