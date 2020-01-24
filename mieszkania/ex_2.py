import numpy as np # Do obsługi tablic
import pandas as pd # Do oczytu danych z pliku
import matplotlib.pyplot as plt # Do wizualizacji
from mpl_toolkits.mplot3d import Axes3D # Do generowania wykresu 3D
from sklearn.linear_model import LinearRegression # Do minimalizacji fukncji kosztu

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

x_y = np.column_stack((x,y)) # Połączenie dwóch kolumn
model = LinearRegression() # Stworzenie instancji modelu
model.fit(x_y, z) # Trenowanie na podstawie danych wsadowych
theta_0 = model.intercept_ # Pobranie wyuczonego parametru theta zero
theta_1 = model.coef_[0] # Pobranie wyuczonego parametru theta jeden
theta_2 = model.coef_[1] # Pobranie wyuczonego parametru theta dwa

# Dodawanie hipotezy do wykresu
# i oznacza liczbę pokoi
for i in range(1,5):
    x = np.array([40,100])
    y = np.array([i,i])
    z = theta_0 + theta_1 * x + theta_2 * y
    ax.plot(x,y,z)

plt.show() # Wyświetlenie wykresu