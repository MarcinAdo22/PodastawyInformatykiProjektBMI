import pandas as pd
import csv

liczba = int(input("Podaj liczbę obserwacji: "))

jedn = int(input("jakie jednostki chcesz wprowadzac (0 - metryczne, 1 - imperialne): "))

people_data = []

i = 0
if jedn > 0:
    lista = []
    while i < liczba:
        plec = str(input("Podaj plec(K - kobieta, M - mezczyzna): "))
        waga_pound = float(input("Podaj wage (Ib): "))
        wzrost_foot = float(input("Podaj wzrost (ft): "))
        BMI = (waga_pound * 0.450) / ((wzrost_foot * 0.3048) * (wzrost_foot * 0.3048))
        print(" ")
        lista.append(plec)
        lista.append(waga_pound)
        lista.append(wzrost_foot)
        lista.append(BMI)
        people_data.append(lista)
        lista = []
        i = i+1

else:
    while i < liczba:
        lista = []
        plec = str(input("Podaj plec(K - kobieta, M - mezczyzna): "))
        waga_kg = float(input("Podaj wage (kg): "))
        wzrost_cm = float(input("Podaj wzrost (cm): "))
        BMI = waga_kg / ((wzrost_cm / 100) * (wzrost_cm / 100))
        print(" ")
        lista.append(plec)
        lista.append(waga_kg)
        lista.append(wzrost_cm)
        lista.append(BMI)
        people_data.append(lista)
        lista = []
        i = i+1


df_people_data = pd.DataFrame(people_data)
df_people_data.columns = 'Plec', 'Waga', 'Wzrost', 'BMI'
print(df_people_data)

df_people_data.to_csv('BMI_wprowadze_recznie.csv')
