"""10 liczb pierwszych """
counter = 0
number = 2
list = []


while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        list.append(str(number))
        counter += 1
    number += 1
print(','.join(list))