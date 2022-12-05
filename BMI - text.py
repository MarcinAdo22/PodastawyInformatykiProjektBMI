import pandas

excel = pandas.read_excel(r'listaBMI.xlsx')

osoby = excel.iloc

for osoba in osoby:
    imie = osoba['imie']
    nazwisko = osoba['nazwisko']
    wagaOsoby = osoba['waga']
    wzrostOsoby = osoba['wzrost']/100
    BMI = (wagaOsoby/(wzrostOsoby*wzrostOsoby))
    print(imie + " " + nazwisko + "posiada BMI" + str(BMI))
