"""Sprawdzenie czy rok jest przestępny"""

def is_leap(year):
    if year%4==0 and (year%100!=0 or year%400==0):
        return True
    else:
        return False

print(is_leap(2000))
print(is_leap(1992))
print(is_leap(2400))
print(is_leap(2401))
print(is_leap(1351))