#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 22:30:43 2022

@author: janswider
"""

# Importowanie bibliotek
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from IPython.display import display


# Czytanie danych plec wzrost waga z pliku csv
dfBMI = pd.read_csv("daneBMI.csv")

display(dfBMI)

dfBMI['BMI']= 0
dfBMI['Kategoria'] = 'a'
#display(dfBMI)


for i in range(len(dfBMI)):
    bmi = round(dfBMI.loc[i][1]/((dfBMI.loc[i][2]/100)*(dfBMI.loc[i][2]/100)),2)
    dfBMI.loc[i,'BMI'] = bmi  
    if bmi < 16:
        dfBMI.loc[i,'Kategoria'] = "wygłodzenie"
    if bmi >= 16 and bmi <= 16.99:
        dfBMI.loc[i,'Kategoria'] = "wychudzenie"
    if bmi >= 17 and bmi <= 18.49:
        dfBMI.loc[i,'Kategoria'] = "niedowaga"
    if bmi >=18.50 and bmi <= 24.99:
        dfBMI.loc[i,'Kategoria'] = "pożądana masa ciała"
    if bmi >= 25 and bmi <= 29.99:
        dfBMI.loc[i,'Kategoria'] = "nadwaga"
    if bmi >= 30 and bmi <= 34.99:
        dfBMI.loc[i,'Kategoria'] = "otyłość I stopnia"
    if bmi >= 35 and bmi <= 39.99:
        dfBMI.loc[i,'Kategoria'] = "otyłość II stopnia (duża)"
    if bmi >= 40:
        dfBMI.loc[i,'Kategoria'] = "otyłość III stopnia (chorobliwa)"


#display(dfBMI)


# Ustawienie tła wykresu
sns.set_theme(style="whitegrid")

# Okrelenie palety kolorów dla hue

paleta = {
    'otyłość III stopnia (chorobliwa)': 'tab:brown',
    'otyłość II stopnia (duża)': 'tab:red',
    'otyłość I stopnia': 'tab:orange',
    'nadwaga': 'tab:olive',
    'pożądana masa ciała': 'tab:green',
    'niedowaga': 'tab:grey',
    'wychudzenie': 'tab:cyan',
    'wygłodzenie': 'tab:blue',
}

kolejnosc = ['wygłodzenie','wychudzenie','niedowaga','pożądana masa ciała',
             'nadwaga','otyłość I stopnia','otyłość II stopnia (duża)','otyłość III stopnia (chorobliwa)'
    ]



# Sporządzenie wykresu
sns.relplot(
    data=dfBMI,
   x="Wzrost", 
   y="Waga", 
   col="Płeć",
   hue="Kategoria",
   palette = paleta,
   hue_order = kolejnosc,
   #style="Kategoria", 
   size='BMI',
)

