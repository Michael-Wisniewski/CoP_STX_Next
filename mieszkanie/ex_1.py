import pandas as pd # Do oczytu danych z pliku
import matplotlib.pyplot as plt # Do wizualizacji
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('data.csv') # Wczytanie danych

# Podzielenie na osobne tablice i skonwertowanie 
# do obiektu numpy.ndarray
x = data.iloc[:, 0].values
y = data.iloc[:, 2].values
z = data.iloc[:, 3].values



fig = plt.figure()
ax = Axes3D(fig)



ax.scatter(x, y, z)

# plt.scatter(x, y, marker="x", color="red") # Dodanie wykresu punktowego
# plt.grid(True) # Linie pomocnicze
# plt.xlabel('Populacja w 10.000') # Opis osi X
# plt.ylabel('Zysk w 10.000$') # Opis osi Y
plt.show() # Wyświetlenie wykresu