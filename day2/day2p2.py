def find_sum_of_all_of_palindromic_numbers(a, b):
    sum_palindromic = 0
    for num in range(a, b+1):
        str_num = str(num)
        n = len(str_num)
        for size in range(1, n // 2 + 1):
            parts = [str_num[i:i+size] for i in range(0, n, size)]
            if len(set(parts)) == 1:
                sum_palindromic += num
                break
    return sum_palindromic

result = 0

with open('../data/day2.txt', 'r') as f:
        line = f.readline().rstrip('\n').split(',')
        for ranges in line:
            start, end = ranges.split('-')
            result += find_sum_of_all_of_palindromic_numbers(int(start),int(end))
        print(result)




