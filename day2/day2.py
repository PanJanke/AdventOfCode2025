def check_range(value, min_value, max_value):
    return min_value <= value <= max_value

def find_sum_of_palindromic_numbers(a, b):
    sum_palindromic = 0
    str_start = str(a)
    str_end = str(b)
    if len(str_start) == len(str_end) and len(str_end)%2 !=0:  # odd length
        return sum_palindromic
    num = a

    while num <= b:
        str_num = str(num)
        mid = len(str_num) // 2
        first_half = str_num[:mid]
        second_half = str_num[mid:]
        if first_half == second_half:
            sum_palindromic += num
            new_base = int(first_half) + 1
            new_base = new_base*(10 ** len(str(new_base))) + new_base
            if check_range(new_base, a, b):
                num = new_base
                continue
        num += 1
    return sum_palindromic

result = 0
with open('../data/day2.txt', 'r') as f:
        line = f.readline().rstrip('\n').split(',')
        for ranges in line:
            start, end = ranges.split('-')
            result += find_sum_of_palindromic_numbers(int(start),int(end))
        print(result)



