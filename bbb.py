"""Najmniejsza i największa liczba"""


list = [1,4,8,12,57,-1,-15,-100,101]

najmniejsza = None
najwieksza = None

for i in list:
    if najmniejsza == None or najmniejsza > i:
        najmniejsza =  i

    if najwieksza == None or najwieksza < i:
        najwieksza = i

print("Najwieksza liczba to:", najwieksza)
print("Najmniejsza liczba to:", najmniejsza)