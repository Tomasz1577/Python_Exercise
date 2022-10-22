'''Sortowanie zagnieżdzonego obiektu tupli po drugim elemencie (wiek)'''

info = (('Monika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))

asc = tuple(sorted(info, key= lambda x:x[1]))
desc = tuple(sorted(info, key= lambda x:x[1], reverse=True))

print(f'Rosnąco: {asc}')
print(f'Malejąco: {desc}')