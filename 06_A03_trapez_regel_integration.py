# Python initialisieren :
import numpy as np;

def integrate_trapz(**kwargs):
    # Parameter :
    x_0=kwargs.get("x_0"); x_E =kwargs.get("x_E"); n =kwargs.get("n"); N =kwargs.get("N"); pr =kwargs.get("pr");
    # Funktionen :
    f = kwargs.get("func")
    # Ausgabe :
    print(' --------------------------------------------------');
    print(__file__ );
    print (' --------------------------------------------------');
    # Berechnungen :
    for k in range(0 , n ):
        x_data = np.linspace(x_0 , x_E , N);
        f_data = f(x_data );
        # Integration :
        I = np.trapz(f_data , x_data );
        print(f"I = {I:#.16g} | N = {N:g}");
        N =2* N ;
    # Ausgabe :
    print(' --------------------------------------------------');
    print( f"I = {I:#.{pr}g}");
    print(' --------------------------------------------------');

print("Teilaufgabe a)")
x_0 =0; x_E =2; n =10; N =201; pr =6;
# Funktionen :
def f(x): y=np.sqrt(x+np.sin(x)); return y;
integrate_trapz(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)
print("")

print("Teilaufgabe b)")
x_0 =1; x_E =3; n =10; N =201; pr =10;
# Funktionen :
def f(x): y=(1-x**2)/(1+2**x); return y;
integrate_trapz(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)
print("")

print("Teilaufgabe c)")
# Parameter :
x_0 = -1; x_E =1; n =10; N =201; pr =8;
# Funktionen :
def f(x): y=3/np.tan(1+x**2); return y;
integrate_trapz(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)
print("")