# Python
# AUEM
# 2022-05-08
# Begin
# --------------------------------------------------------------------------------------
# Python initialisieren:
import numpy as np;
#
print('--------------------------------------------------------------------------------------');
print(__file__);
print('--------------------------------------------------------------------------------------');
print('b)');
# Parameter:
n=15; pr_a=4; pr_b=3;
# Funktionen:
def LGLS_Hilbert(n):
    k_data=np.r_[1:n+1];
    [i_grid,j_grid]=np.meshgrid(k_data,k_data);
    A=1./(i_grid+j_grid-1);
    b=np.sum(A,axis=1);
    return A,b;
#
print('--------------------------------------------------------------------------------------');
print('c)');
# Berechnungen:
[A,b]=LGLS_Hilbert(n);
G=np.block([A,np.expand_dims(b,axis=1)]);
x=np.linalg.solve(A,b);
C=np.linalg.cond(A);
D=np.linalg.det(A);
# Ausgabe:
with np.printoptions(precision=pr_a):
    print(f"G = \n{G}\n");
    print(f"x = \n{x}\n");
print(f"C = {C:#.{pr_b}g}\n");
print(f"D = {D:#.{pr_b}g}\n");
#
print('--------------------------------------------------------------------------------------');
#
# --------------------------------------------------------------------------------------
# End
