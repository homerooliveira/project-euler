# 6) Sum square difference
def problem6():
    numbers = list(range(1, 101))
    difference = (pow(sum(numbers), 2)) - (sum([pow(i, 2) for i in numbers]))
    print(difference)


if __name__ == '__main__':
    problem6()