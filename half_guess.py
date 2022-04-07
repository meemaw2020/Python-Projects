import random

a = 0
b = input("Type a number for top range: ")

if b.isdigit():
    b = int(b)

    if b <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

target =  random.randint(0, b)
print("The program generated", target)

count_times = 0

while True:
    count_times += 1
    m = int((a + b) / 2)
    if m == target:
        print(f'The number is {m}.')
        print("It guessed in", count_times, "times")
        break

    elif m < target:
            print(f"The program guessed {m} and it's lower than {target}")
            a = m

    elif m > target:
            print(f"The program guessed {m} and it's higher than {target}")
            b = m
