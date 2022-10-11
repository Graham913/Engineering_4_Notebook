#type:ignore
def area_calc(x1, x2, x3, y1, y2, y3):
    area = abs((1/2) * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) ) )

    print(area)
    return area

while True:
  print('Enter the first coordinate in format x,y:')
  coordinate1 = input()
  print('Enter the second coordinate in format x,y:')
  coordinate2 = input()
  print('Enter the third coordinate in format x,y:')
  coordinate3 = input()

  try:
    coordinate1 = coordinate1.split(",")
    coordinate2 = coordinate2.split(",")
    coordinate3 = coordinate3.split(",")
    x1 = float(coordinate1[0])
    x2 = float(coordinate2[0])
    x3 = float(coordinate3[0])

    y1 = float(coordinate1[1])
    y2 = float(coordinate2[1])
    y3 = float(coordinate3[1])
    print(y3)

    area = area_calc(x1, x2, x3, y1, y2, y3)
    ans = area
  
    print(f"The area of the triangle with vertices {coordinate1}, {coordinate2}, {coordinate3} is {ans} square kilometers.")


  except:
    print("these points are not a valid triangle.")


  