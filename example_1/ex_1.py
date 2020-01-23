import pandas as pd # Do oczytu danych z pliku
import matplotlib.pyplot as plt # Do wizualizacji

data = pd.read_csv('data.csv') # Wczytanie danych

# Podzielenie na osobne tablice i skonwertowanie 
# do obiektu numpy.ndarray
x = data.iloc[:, 0]
y = data.iloc[:, 1]

plt.scatter(x, y, marker="x", color="red") # Dodanie wykresu punktowego
plt.grid(True) # Linie pomocnicze
plt.show() # Wyświetlenie wykresu