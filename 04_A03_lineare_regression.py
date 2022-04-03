# Python initialisieren :
import matplotlib.pyplot as pl ;
import numpy as np ;

def linear_regression(suffix, **kwargs):
    pl.close('all');
    # Parameter :
    x_0=kwargs.get("x_0")
    x_E=kwargs.get("x_E")
    y_a=kwargs.get("y_a")
    y_b=kwargs.get("y_b")
    dg=kwargs.get("dg", 1)
    pr=kwargs.get("pr", 3)
    lw=kwargs.get("lw", 3)
    fig=kwargs.get("fig")
    tc_x=kwargs.get("tc_x")
    tc_y=kwargs.get("tc_y")
    # Daten :
    x_data=kwargs.get("x_data")
    y_data=kwargs.get("y_data")
    # Berechnungen :
    p = np.polyfit( x_data , y_data , dg );
    g_data = np.polyval(p , x_data );
    # Ausgabe :
    print(' --------------------------------------------------');
    print( __file__ );
    print(' --------------------------------------------------');
    print( f" Steigung : m = {p[0]:#.{pr}g}");
    print( f"y- Achsabschnitt : q = {p[1]:#.{pr}g}");
    print(' --------------------------------------------------');
    # Plot :
    fh = pl.figure( fig );
    pl.plot( x_data , g_data , linewidth = lw );
    pl.plot( x_data , y_data ,'o', linewidth = lw );
    pl.xlabel(r'$x$'); pl.ylabel(r'$y$');
    pl.xticks( tc_x ); pl.yticks( tc_y );
    pl.grid( visible = True ); pl.axis('image');
    filename=f"04_A03_{suffix}).png"
    pl.savefig(filename)

# a)
# Parameter :
x_0 =1.; x_E =7.; y_a = -2.; y_b =3.; dg =1; pr =3; lw =3; fig =1;
tc_x = np.r_[ x_0 : x_E +0.5:0.5]; tc_y = np.r_[ y_a : y_b +0.5:0.5];
# Daten :
x_data = np.r_[ x_0 : x_E +1];
y_data = np.array([2.5 ,2.2 ,1.5 ,1.0 ,0.6 , -0.3 , -1.4]);
# Funktionsaufruf
linear_regression(
    "a",
    x_0=x_0,
    x_E=x_E,
    y_a=y_a,
    y_b=y_b,
    dg=dg,
    pr=pr,
    lw=lw,
    fig=fig,
    tc_x=tc_x,
    tc_y=tc_y,
    x_data=x_data,
    y_data=y_data
)

# b)
# Parameter :
x_0 =-2.; x_E =10.; y_a = 0.; y_b =5.; dg =1; pr =3; lw =3; fig =2;
tc_x = np.r_[ x_0 : x_E+1]; tc_y = np.r_[ y_a : y_b +1];
# Daten :
x_data = np.r_[ x_0 : x_E +2:2];
y_data = np.array([0.5 ,0.4 ,1.1 ,1.8 ,3.5 ,3.0 ,4.2]);
# Funktionsaufruf
linear_regression(
    "b",
    x_0=x_0,
    x_E=x_E,
    y_a=y_a,
    y_b=y_b,
    dg=dg,
    pr=pr,
    lw=lw,
    fig=fig,
    tc_x=tc_x,
    tc_y=tc_y,
    x_data=x_data,
    y_data=y_data
)