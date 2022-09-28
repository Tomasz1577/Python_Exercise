"""FizzBuzz"""

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:  #sprawdzenie podzielności przez 3 i 5 - wydrkuje FizzBuzz
        print('FizzBuzz')
    elif i % 3 == 0:                # jeśli liczba będzie podzielna przez 3 wydrkuje  Fizz
        print('Fizz')
    elif i % 5 == 0:            # jeśli liczba jest podzielna przez 5, wydrukuje Buzz
        print('Buzz')
    else:
        print(i)

