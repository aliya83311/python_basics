nums_list1 = [num**3 for num in range(1, 1001, 2)]
nums_list2 = [num**3 + 17 for num in range(1, 1001, 2)]


def sum_digits(seq):
    counter = 0
    for num in seq:
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        seq[counter] = total
        counter += 1
    return seq


def sum_numbers(seq):
    total_numbers = 0
    for number in seq:
        if number % 7 == 0:
            total_numbers += number
    return total_numbers


print(nums_list1)
print(sum_digits(nums_list1))
print(sum_numbers(nums_list1))

print(nums_list2)
print(sum_digits(nums_list2))
print(sum_numbers(nums_list2))
