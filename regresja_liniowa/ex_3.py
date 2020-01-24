import numpy as np # Do obsługi tablic
import pandas as pd # Do oczytu danych z pliku
import matplotlib.pyplot as plt # Do wizualizacji
from sklearn.linear_model import LinearRegression # Do minimalizacji fukncji kosztu

data = pd.read_csv('data.csv') # Wczytanie danych

# Podzielenie na osobne tablice i skonwertowanie 
# do obiektu numpy.ndarray

# Metoda fit() obiektu klasy LinearRegression wymaga dwu wymiarowej tablicy jako argumentu.
# Należy dokonać konwersji z tablicy jedno na dwuwymiarową za pomocą metody reshape()
x = data.iloc[:, 0].values.reshape([-1,1]) 
y = data.iloc[:, 1].values
plt.scatter(x, y, marker="x", color="red") # Dodanie wykresu punktowego

model = LinearRegression() # Stworzenie instancji modelu
model.fit(x, y) # Trenowanie na podstawie danych wsadowych
theta_0 = model.intercept_ # Pobranie wyuczonego parametru theta zero
theta_1 = model.coef_ # Pobranie wyuczonego parametru theta jeden

x = np.array([0, 5]) # Zdefiniowanie argumentów
hypothesis = theta_0 + theta_1 * x # Obliczenie wartości hipotezy
plt.plot(x, hypothesis, color="red") # Dodanie hipotezy do wykresu

print('Otrzymane parametry to:\ntheta_0: {}\ntheta_1: {}'.format(theta_0, theta_1))
plt.grid(True)
plt.show()