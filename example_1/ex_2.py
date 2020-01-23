import numpy as np # Do obsługi tablic
import pandas as pd # Do oczytu danych z pliku
import matplotlib.pyplot as plt # Do wizualizacji

data = pd.read_csv('data.csv') # Wczytanie danych

# Podzielenie na osobne tablice i skonwertowanie 
# do obiektu numpy.ndarray
x = data.iloc[:, 0]
y = data.iloc[:, 1]

plt.scatter(x, y, marker="x", color="red") # Dodanie wykresu punktowego

x = np.array([0, 5]) # Zdefiniowanie argumentów
hypothesis_1 = 0 + 1 * x # Wartości pierwszej hipotezy
hypothesis_2 = 0.5 + 0.5 * x # Wartości drugiej hipotezy

plt.plot(x, hypothesis_1, color="green") # Dodanie pierwszej hipotezy do wykresu
plt.plot(x, hypothesis_2, color="blue") # Dodanie drugiej hipotezy do wykresu
plt.grid(True) # Linie pomocnicze
plt.show() # Wyświetlenie wykresu