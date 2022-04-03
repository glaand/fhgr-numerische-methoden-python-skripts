# Python initialisieren :
import matplotlib.pyplot as pl;
import numpy as np;
# Parameter:
q=4.; x_0=-12.; x_1=-0.2; x_2=- x_1; x_E=- x_0;
y_a=-6.; y_b=- y_a; N_f =201; N_g =3; lw =3; fig =1;
tc_x=np.r_[x_0: x_E +1.:1.]; tc_y=np.r_[y_a: y_b +1.:1.];
# Funktionen :
def f(x): y =0.5*(x + q / x); return y;
# Daten :
x_a_data=np.linspace(x_0, x_E, N_f);
x_b_data=np.linspace(x_0, x_E, N_f);
f_a_data=f(x_a_data);
f_b_data=f(x_b_data);
x_data=np.linspace(x_0, x_E, N_g);
g_data=x_data;
# Plot :
fh=pl.figure(fig);
pl.plot(x_a_data, f_a_data, linewidth=lw);
pl.plot(x_data, g_data, linewidth=lw);
pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
pl.xticks(tc_x); pl.yticks(tc_y);
pl.grid(visible=True); pl.axis('image');
pl.xlim([x_0, x_E]); pl.ylim([y_a, y_b]);
pl.savefig("02_A04_fixpunkt_iteration.png")