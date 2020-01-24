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

x = np.array([4.5, 22.5]) # Zdefiniowanie argumentów
hypothesis = theta_0 + theta_1 * x # Obliczenie wartości hipotezy
plt.plot(x, hypothesis, color="blue") # Dodanie hipotezy do wykresu

x = np.array([17.5]) # Zdefiniowanie argumentu
sought_value = theta_0 + theta_1 * x # Obliczenie szukanej wartości
plt.scatter(x, sought_value, marker="x", color="green", s=100, linewidth='4') # Dodanie szukanej wartości do wykresu

print('Otrzymane parametry to:\ntheta_0: {}\ntheta_1: {}'.format(theta_0, theta_1))
print('Szacowany zysk dla o populacji 175000 osób to: {}'.format(sought_value))
plt.grid(True) # Linie pomocnicze
plt.xlabel('Populacja w 10.000') # Opis osi X
plt.ylabel('Zysk w 10.000 PLN') # Opis osi Y
plt.show() # Wyświetlenie wykresu