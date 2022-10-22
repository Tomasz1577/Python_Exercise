items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

histogram = {}

for i in items:
    if i not in histogram:
        histogram[i] = 1
    else:
        histogram[i] +=1
print(histogram)