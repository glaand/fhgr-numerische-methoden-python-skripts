import numpy as np ;
# Parameter :
x =3.; pr =16;

# Funktionen :
def NeAi(x, x_data, y_data):
    n = np.size(y_data );
    TAB = np.block([[y_data] ,[np.zeros((n-1, n))]]);
    for i in range(1, n):
        for j in range(i, n ):
            TAB[i][j]=((x-x_data[j-i])*TAB[i-1][j]
                        -(x-x_data[j])*TAB[i-1][j-1])/(x_data[j]-x_data[j-i]);
    print(TAB)
    return TAB[n-1][n-1];

def NeAiNu(x_data, y_data):
    n = np.size(y_data);
    TAB = np.block([[y_data] ,[np.zeros((n-1, n))]]);
    for i in range(1, n):
        for j in range(i, n ):
            TAB [i][j]=(x_data[j]*TAB[i -1][j-1]
                -x_data[j-i]*TAB[i-1][j])/(x_data[j]-x_data[j-i]);
    return TAB[n-1][n-1];

if __name__ == "__main__":
    # Berechnungen :
    # a)
    print("Teilaufgabe a)")
    x_data = np.array([4., 8.]);
    y_data = np.array([1., -1.]);
    y = NeAi(x , x_data , y_data);
    print(f"Für x={x}, ergibt sich y={y}")
    print("")

    # b)
    print("Teilaufgabe b)")
    x_data = np.array([-1., 1., 2.]);
    y_data = np.array([15. ,5. ,9.]);
    y = NeAi(x , x_data , y_data);
    print(f"Für x={x}, ergibt sich y={y}")
    print("")

    # c)
    print("Teilaufgabe c)")
    x_data = np.array([-1. ,0. ,1. ,2.]);
    y_data = np.array([-5. , -1. , -1. ,1.]);
    y = NeAi(x , x_data , y_data);
    print(f"Für x={x}, ergibt sich y={y}")
    print("")