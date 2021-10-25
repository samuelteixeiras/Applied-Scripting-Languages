# Student id = A00291713

text = input("Enter a series of numbers, separated by spaces: ")

numbers = [ int(i) for i in text.split(" ") ]

def getMean(total, consideredValues):
    return (float(total / consideredValues))

print(f"Number of values: {len(numbers)}")
print(f"Total: {sum(numbers)}")
print(f"Mean: {getMean(sum(numbers),len(numbers)):.1f}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
