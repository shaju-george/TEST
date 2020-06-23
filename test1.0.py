
# Following code will satisfy case 1 and case 2 . 
x = list()
xy=[]

n = int(input("Enter number of coordinates : ")) 
print("enter x-coordinate and then y-coordinate")
# iterating till the range 
for i in range(0, n): 
    ele =  ele = [float(input()), float(input())]
    xy.append(ele) 

print("your input coordinates are\n")  
print(xy)
print()

#finding x-coordinate
for i in range(0,n):
    x.append(xy[i][0])
x.sort()
# print(x)

y = list()
for i in range(0,n):
    y.append(xy[i][1])
y.sort()
#print(y)
print()

coordinate = []
t=int(x[-1])+1 #last element in x when considered in range()
t1=int(y[-1])+1
for i in range(int(x[0]),t):
    for j in range(int(y[0]),t1):
        coordinate.append([float(i),float(j)])

#print(coordinate)

point = []
print ('enter coordinates of points to be find in 2-D')
       
for i in range(2):
    temp = float(input())
    point.append(temp)
       
print("point you entered is " , point)
# print(type(point))

if point in coordinate :
    print(" point 'p' lies inside the polygon ")
else:
 print("false,point 'p' is outside ")
