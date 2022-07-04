import numpy as np
import matplotlib.pyplot as pl ;
import scipy.integrate as ig;

def NeAiNu(x_data, y_data):
    n = np.size(y_data);
    TAB = np.block([[y_data] ,[np.zeros((n-1, n))]]);
    for i in range(1, n):
        for j in range(i, n ):
            TAB [i][j]=(x_data[j]*TAB[i -1][j-1]
                -x_data[j-i]*TAB[i-1][j])/(x_data[j]-x_data[j-i]);
    return TAB[n-1][n-1];


def trapez_integra_extra(**kwargs):
    # Parameter:
    x_0=kwargs.get("x_0"); x_E =kwargs.get("x_E"); n =kwargs.get("n"); N =kwargs.get("N"); pr =kwargs.get("pr");
    f=kwargs.get("func");
    # Ausgabe :
    print(' --------------------------------------------------');
    print(__file__);
    print (' --------------------------------------------------');
    # Berechnungen :
    h_data = np.zeros(n);
    I_data = np.zeros(n);
    for k in range (0, n):
        h=(x_E-x_0)/ N ;
        x_data= np.linspace(x_0 , x_E , N);
        f_data= f(x_data);
        # Integration :
        I = np.trapz(f_data , x_data);
        h_data[k]= h;
        I_data[k]= I;
        print(f"I = {I:#.16g} | N = {N:g}");
        N =2* N;
    I_raw = I_data [-1];
    I_ext = NeAiNu(h_data , I_data);
    # Ausgabe :
    print (' --------------------------------------------------');
    print(f" I_raw = { I_raw :#.{pr}g}");
    print(f" I_ext = { I_ext :#.{pr}g}");
    print (' --------------------------------------------------');


def simpson_integra(**kwargs):
    # Parameter:
    x_0=kwargs.get("x_0"); x_E =kwargs.get("x_E"); n =kwargs.get("n"); N =kwargs.get("N"); pr =kwargs.get("pr");
    f=kwargs.get("func");
    # Ausgabe :
    print(' --------------------------------------------------');
    print(__file__);
    print (' --------------------------------------------------');
    # Berechnungen :
    for k in range (0, n):
        x_data = np.linspace(x_0, x_E, N );
        f_data = f(x_data);
        # Integration :
        I = ig.simps(f_data, x_data);
        print(f"I = {I:#.16g} | N = {N:g}");
        N =2*N;

    # Ausgabe :
    print (' --------------------------------------------------');
    print ( f"I = {I:#.{pr}g}");
    print (' --------------------------------------------------');

def integrand(x): y = ((1+x)**2)*(np.cos(x)**2)*(np.e**((-x**2)/(3))); return y;

def a():
    x_data = np.linspace(-6 , 6 , 501);
    fh=pl.figure();
    pl.plot(x_data,integrand(x_data),linewidth=1);
    pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
    pl.grid(visible=True); pl.axis('image');
    pl.savefig("aufgabe_7.png")

def b():
    x_data = np.linspace(-6 , 6 , 501);
    f_data = integrand(x_data);
    # Integration :
    I = np.trapz(f_data , x_data );
    print(f"I = {I:#.7g}");

def c():
    x_0=-6;x_E=6;n=10;N=201;pr=7;f=integrand;
    trapez_integra_extra(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)

def d():
    x_0=-6;x_E=6;n=10;N=201;pr=7;f=integrand;
    simpson_integra(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)

a()
b()
c()
d()