import numpy as np
import matplotlib.pyplot as plt

def f(x): y = 1+(1/3)*x; return y;

x_data = [1]
y_data = []

n = 10
curx = 0

for i in range(n):
    x = x_data[curx]
    new_y = f(x)
    y_data.append(new_y)
    x_data.append(new_y)
    curx += 1
x_data.pop()

fh=plt.figure()
plt.plot(x_data,y_data,linewidth=1, label=" ")
plt.plot(x_data,x_data,c="b", linewidth=2, label="Fixpunkt-Gerade")
plt.scatter(x_data,y_data,color="r", linewidth=2, label=" ")
plt.xlabel(r'$x$'); plt.ylabel(r'$y$')
plt.grid(visible=True); plt.axis('image')
plt.savefig("rekursiv_plotter.png")
plt.legend()
print(x_data)
print(y_data)