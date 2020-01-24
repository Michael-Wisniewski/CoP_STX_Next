import pandas as pd # Do oczytu danych z pliku
import matplotlib.pyplot as plt # Do wizualizacji

data = pd.read_csv('data.csv') # Wczytanie danych

# Podzielenie na osobne tablice i skonwertowanie 
# do obiektu numpy.ndarray
x = data.iloc[:, 0].values
y = data.iloc[:, 1].values

plt.xlabel('Populacja w 10.000') # Opis osi X
plt.ylabel('Zysk w 10.000 PLN') # Opis osi Y

plt.scatter(x, y, marker="x", color="red") # Dodanie wykresu punktowego
plt.grid(True) # Linie pomocnicze
plt.show() # Wyświetlenie wykresu