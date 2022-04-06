import numpy as np
import matplotlib.pyplot as pl ;

def f(x): y = 1 - x**2; return y;

x_data = [1/2]
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

fh=pl.figure();
pl.plot(x_data,y_data,linewidth=1);
pl.plot(x_data,x_data,c="m", linewidth=1);
pl.scatter(x_data,y_data,color="r", linewidth=2);
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.grid(visible=True); pl.axis('image');
pl.savefig("rekursiv_plotter.png")