import re
import random
import main


def test_main_1():

    number1 = [0, 2, 3]
    number2 = [1, 4, 5, 6, 9]
    print('Test data')
    print(number1)
    print(number2)
    retlist = main.merge(number1, number2)
    print('After merge', retlist)
    assert retlist[0] == 0
    assert retlist[1] == 1
    assert retlist[2] == 2
    assert retlist[3] == 3
    assert retlist[4] == 4
    assert retlist[5] == 5
    assert retlist[6] == 6
    assert retlist[7] == 9
    # #########################################


def test_main_2():
    n1 = [random.randint(0, 20) for i in range(5)]
    n2 = [random.randint(0, 20) for i in range(3)]
    n1.sort()
    n2.sort()
    tlist = n1 + n2
    tlist.sort()
    print('Test data')
    print(n1)
    print(n2)
    retlist = main.merge(n1, n2)
    print('After merge', retlist)
    print(tlist)
    print(retlist)
    assert tlist == retlist


def check_file_for_sort_function(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Regular expression pattern to match 'sort('
            pattern = r'\bsort\s*\('
            matches = re.findall(pattern, content)
            for match in matches:
                if not is_within_comment(content, match):
                    return True
            return False
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return False


def is_within_comment(content, match):
    lines = content.split("\n")
    for line in lines:
        comment_start = line.find("#")
        if comment_start != -1 and comment_start < line.find(match):
            return True
    return False


def test_sort():
    flag = check_file_for_sort_function('main.py')
    assert flag == False, 'Do not use sort functions '

# def test_sort():
#     with open('main.py') as f:
#         flag = True
#         for line in f:
#             if 'main()' in line:
#                 break
#             if 'sort' in line:
#                 flag = False
#                 break
#     assert flag == True
