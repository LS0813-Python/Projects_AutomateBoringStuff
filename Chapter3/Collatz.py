
def collatz(number):
    print(number)
    if number == 1:
        return 1
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    collatz(number)

try:
    collatz(int(input('Input number greater than 1 : ')))
except ValueError:
    print('Input invalid!')