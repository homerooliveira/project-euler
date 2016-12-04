# 1)Multiples of 3 and 5
def problem1():
    total = sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])
    print(total)


# 6) Sum square difference
def problem6():
    numbers = list(range(1, 101))
    difference = (pow(sum(numbers), 2)) - (sum([pow(i, 2) for i in numbers]))
    print(difference)


if __name__ == '__main__':
    problem1()
