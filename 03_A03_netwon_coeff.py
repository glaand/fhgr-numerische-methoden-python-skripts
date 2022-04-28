# Python
# AUEM
# 2022-03-13
# Begin
# --------------------------------------------------------------------------------------
# Python initialisieren:
import matplotlib.pyplot as pl;
import scipy.integrate as ig;
import numpy as np;
# Python konfigurieren:
pl.close('all');
pl.rcParams['figure.figsize']=(7.03,8);
pl.rcParams['font.size']=9;
pl.rcParams['font.family']='serif';
pl.rcParams['text.usetex']=True;
#
print('--------------------------------------------------------------------------------------');
print(__file__);
print('--------------------------------------------------------------------------------------');
print('a)');
# Parameter:
x_data=np.array([1,2,3]);
y_data=np.array([2,4,8]);
x_0=x_data[0]; x_E=x_data[-1]; N=3; lw=3; fig=1;
# Berechnungen:
n=np.size(y_data);
TAB=np.block([[y_data],[np.zeros((n-1,n))]]);
c_data=np.zeros(n);
c_data[0]=y_data[0];
for i in range(1,n):
    for j in range(i,n):
        TAB[i][j]=(TAB[i-1][j]-TAB[i-1][j-1])/(x_data[j]-x_data[j-i]);
    c_data[i]=TAB[i][i];
# Ausgabe:
print('--------------------------------------------------');
print(__file__);
print('--------------------------------------------------');
print(f"Daten Argumente:      x = {x_data}");
print(f"Daten Funktionswerte: y = {y_data}");
print(f"Newton-Koeffizienten: c = {c_data}");
print('--------------------------------------------------');
# Funktionen:
def p(x):
    d=1.; y=c_data[0];
    for k in range(1,n):
        d=d*(x-x_data[k-1]);
        y=y+c_data[k]*d;
    return y;
# Daten:
u_data=np.linspace(x_0,x_E,N);
v_data=p(u_data);
# Plot:
fh=pl.figure(fig);
pl.plot(u_data,v_data,linewidth=lw);
pl.plot(x_data,y_data,'o',linewidth=lw);
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.grid(visible=True); pl.axis('image');
pl.savefig("03_A03_a).png")
#
print('--------------------------------------------------------------------------------------');
print('b)');
# Parameter:
x_data=np.array([-1.,1.,2.]);
y_data=np.array([15.,5.,9.]);
x_0=x_data[0]; x_E=x_data[-1]; N=201; lw=3; fig=fig+1;
# Berechnungen:
n=np.size(y_data);
TAB=np.block([[y_data],[np.zeros((n-1,n))]]);
c_data=np.zeros(n);
c_data[0]=y_data[0];
for i in range(1,n):
    for j in range(i,n):
        TAB[i][j]=(TAB[i-1][j]-TAB[i-1][j-1])/(x_data[j]-x_data[j-i]);
    c_data[i]=TAB[i][i];
# Ausgabe:
print('--------------------------------------------------');
print(__file__);
print('--------------------------------------------------');
print(f"Daten Argumente:      x = {x_data}");
print(f"Daten Funktionswerte: y = {y_data}");
print(f"Newton-Koeffizienten: c = {c_data}");
print('--------------------------------------------------');
# Funktionen:
def p(x):
    d=1.; y=c_data[0];
    for k in range(1,n):
        d=d*(x-x_data[k-1]);
        y=y+c_data[k]*d;
    return y;
# Daten:
u_data=np.linspace(x_0,x_E,N);
v_data=p(u_data);
# Plot:
fh=pl.figure(fig);
pl.plot(u_data,v_data,linewidth=lw);
pl.plot(x_data,y_data,'o',linewidth=lw);
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.grid(visible=True); pl.axis('image');
pl.savefig("03_A03_b).png")
#
print('--------------------------------------------------------------------------------------');
print('c)');
# Parameter:
x_data=np.array([-1.,0.,1.,2.]);
y_data=np.array([-5.,-1.,-1.,1.]);
x_0=x_data[0]; x_E=x_data[-1]; N=201; lw=3; fig=fig+1;
# Berechnungen:
n=np.size(y_data);
TAB=np.block([[y_data],[np.zeros((n-1,n))]]);
c_data=np.zeros(n);
c_data[0]=y_data[0];
for i in range(1,n):
    for j in range(i,n):
        TAB[i][j]=(TAB[i-1][j]-TAB[i-1][j-1])/(x_data[j]-x_data[j-i]);
    c_data[i]=TAB[i][i];
# Ausgabe:
print('--------------------------------------------------');
print(__file__);
print('--------------------------------------------------');
print(f"Daten Argumente:      x = {x_data}");
print(f"Daten Funktionswerte: y = {y_data}");
print(f"Newton-Koeffizienten: c = {c_data}");
print('--------------------------------------------------');
# Funktionen:
def p(x):
    d=1.; y=c_data[0];
    for k in range(1,n):
        d=d*(x-x_data[k-1]);
        y=y+c_data[k]*d;
    return y;
# Daten:
u_data=np.linspace(x_0,x_E,N);
v_data=p(u_data);
# Plot:
fh=pl.figure(fig);
pl.plot(u_data,v_data,linewidth=lw);
pl.plot(x_data,y_data,'o',linewidth=lw);
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.grid(visible=True); pl.axis('image');
pl.savefig("03_A03_c).png")
#
print('--------------------------------------------------------------------------------------');
#
# --------------------------------------------------------------------------------------
# End
