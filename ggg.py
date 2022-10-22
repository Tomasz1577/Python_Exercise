'''Obliczanie miejsc zerowych funkcji kwadratowej'''

a = 1
b = 5
c = 4

d = (b**2) - (4*a*c)

x1 = ((-b) - d**(1/2)) / 2*a
x2 = ((-b) + d**(1/2)) / 2*a

print(f'x1 = {x1}')
print(f'x2 = {x2}')