# Python initialisieren:
import numpy as np;
# Parameter:
A=np.array([[4,1,1],[1,4,1],[1,1,4]]);
b=np.array([6,6,6]);
s=0.21; N=100; n=np.shape(b)[0];
# Vorbereitungen:
#H=np.diag(1/np.diag(A)); # Jacobi-Verfahren
H=s*np.eye(n); # Richardson-Verfahren
M=np.eye(n)-H@A;
q=H@b; x=b/3; w=0.; k=0;
y=np.linalg.norm(M);
# Funktion:
def f(x): y=M@x+q; return y;
# Berechnungen:
while np.array_equal(x,w)==False and k<N:
    w=x; k=k+1;
    x=f(x);
    print(f"x_{k} = {np.array2string(x,precision=16)}");
# Ausgabe:
print(f"Loesung: x = {np.array2string(x,precision=3)}");
print(f"Norm:    y = {y}");
