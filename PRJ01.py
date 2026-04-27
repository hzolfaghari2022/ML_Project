x = [5,3,-1,2,6]
y = [14,6,-5.5,3.5,18]
print(x,y)
X,Y, Xi2,XiYi = 0,0,0,0
n = len(x)
for i in range(n):
  X = X + x[i]
  Y = Y + y[i]
  XiYi = XiYi + x[i]*y[i]
  Xi2 = Xi2 + x[i]*x[i]
print(n,X,Y,XiYi,Xi2)
w1 = (n*XiYi-X*Y)/(n*Xi2-X*X)
w0 = (Y-w1*X)/n
print(w0,w1)