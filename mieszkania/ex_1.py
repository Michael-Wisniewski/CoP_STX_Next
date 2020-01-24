import pandas as pd # Do oczytu danych z pliku
import matplotlib.pyplot as plt # Do wizualizacji
from mpl_toolkits.mplot3d import Axes3D # Do generowania wykresu 3D

data = pd.read_csv('data.csv') # Wczytanie danych

# Podzielenie na osobne tablice i skonwertowanie 
# do obiektu numpy.ndarray
x = data.iloc[:, 0].values
y = data.iloc[:, 2].values
z = data.iloc[:, 3].values

fig = plt.figure() # Stworzenie obiektu na trójwymiarowym wykresie
ax = Axes3D(fig)

ax.set_xlabel('Metraż w m2') # Opis osi X
ax.set_ylabel('Liczba pokoi') # Opis osi Y
ax.set_zlabel('Cena w tys. PLN') # Opis osi Z

ax.scatter(x, y, z) # Dodanie wykresu punktowego
plt.show() # Wyświetlenie wykresu