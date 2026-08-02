import numpy

numbers = []

for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

numbers_array = numpy.array(numbers)

average = numpy.mean(numbers_array)

print("Numbers:", numbers_array)
print("Mean:", average)