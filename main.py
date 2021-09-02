

def find_outlier(integers):
    odd_number = []
    even_number = []
    for n in integers:
        if n % 2 == 0:
            odd_number.append(n)
        else:
            even_number.append(n)
    if len(odd_number) == 1:
        return odd_number[0]
    else:
        return even_number[0]




assert find_outlier([2, 4, 6, 8, 10,3]) == 3,'\033[93m'+"Test Failed"
print('\033[92m'+"Test ok")
assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])== 11,"Test Failed"
print("Test Ok")
assert find_outlier([160, 3, 1719, 19, 11, 13, -21])== 160, "Test Failed"
print("Test ok")