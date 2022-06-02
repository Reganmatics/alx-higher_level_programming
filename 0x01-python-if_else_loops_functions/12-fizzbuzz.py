#!/usr/bin/python3
for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz", end =" ")
        continue
    if i % 5 == 0:
        print("Buzz", end =" ")
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end = " ")
        continue
    if i == 100:
        print("Buzz\n")
        continue
    print(i, end=" ")
