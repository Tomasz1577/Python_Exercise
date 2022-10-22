"""Obliczanie wartości przyszłej kwoty w okresie inwestycji"""

pv = 1000 #Kwota wejściowa
r = 0.03 #roczna stopa procentowa
n = 5 # okres inwestycji w latach

fv = pv * (1 + r) ** n
print(f'Wartość końcowa inwestycji wynosi: {fv:.2f} PLN')