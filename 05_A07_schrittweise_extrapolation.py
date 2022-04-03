# Python initialisieren
NeAiNu = __import__('05_A03_neville_aitken_schema').NeAiNu
import numpy as np;

# Parameter
pr=16;

# Daten:
h_data = np.array([
    3.110487775831478e-2,
    1.555243887915739e-2,
    7.776219439578696e-3,
    3.888109719789348e-3
])
I_data = np.array([
    1.999835503887443,
    1.999959284652254,
    1.999989871646689,
    1.999997474185016
]);

# Berechnungen:
I = NeAiNu(h_data, I_data);
# Ausgabe :
print (' --------------------------------------------------');
print ( __file__ );
print (' --------------------------------------------------');
print ( f"I = {I:#.{pr}g}");
print (' --------------------------------------------------');