import main


def test_main_1():
    N = 5
    numbers = main.getRandom(N)
    print(f'The original list values : { numbers }')
    average = sum(numbers) / len(numbers)
    ret = main.filterAvg(numbers)
    print(f'The average value: {sum(numbers)/len(numbers)}')
    print(f'The return values from filterAvg() : { ret }')
    check = [v for v in ret if v < average]
    assert check == []


def test_main_2():
    N = 10
    numbers = main.getRandom(N)
    print(f'The original list values : { numbers }')
    average = sum(numbers) / len(numbers)
    ret = main.filterAvg(numbers)
    print(f'The average value: {sum(numbers)/len(numbers)}')
    print(f'The return values from filterAvg() : { ret }')
    check = [v for v in ret if v < average]
    assert check == []
