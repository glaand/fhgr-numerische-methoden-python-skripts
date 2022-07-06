
# Python initialisieren :
import numpy as np ;
NeAiNu = __import__('05_A03_neville_aitken_schema').NeAiNu

# Funktionen:
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
    print(h_data)
    print (' --------------------------------------------------');
    print(f" I_raw = { I_raw :#.{pr}g}");
    print(f" I_ext = { I_ext :#.{pr}g}");
    print (' --------------------------------------------------');

print("Teilaufgabe a)")
# Parameter :
x_0 =0; x_E =2; n =5; N =201; pr=6;
# Funktionen :
def f(x):y=np.sqrt(x+np.sin(x)); return y;
trapez_integra_extra(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)
print("")

print("Teilaufgabe b)")
# Parameter :
x_0 =1; x_E =3; n =4; N =201; pr =10;
# Funktionen :
def f(x): y=(1-x**2)/(1+2**x); return y ;
trapez_integra_extra(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)
print("")

print("Teilaufgabe c)")
# Parameter :
x_0 = -1; x_E =1; n =4; N =201; pr =8;
# Funktionen :
def f(x): y=3/np.tan(1+x**2); return y ;
trapez_integra_extra(x_0=x_0,x_E=x_E,n=n,N=N,pr=pr,func=f)
print("")