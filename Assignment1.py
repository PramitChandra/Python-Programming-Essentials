lower = 1
upper = 200

print("Prime Numbers in the given range are: ")

for number in range(lower, upper + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
