def find_outlier(integers):
    odd = [n for n in integers if n%2 !=0]
    even = [n for n in integers if n%2 == 0]
    return even[0] if len(even)<len(odd)else odd[0]




assert find_outlier([2, 4, 6, 8, 10,3]) == 3,'\033[93m'+"Test Failed"
print('\033[92m'+"Test ok")
assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])== 11,"Test Failed"
print("Test Ok")
assert find_outlier([160, 3, 1719, 19, 11, 13, -21])== 160, "Test Failed"
print("Test ok")