def percent_maker(num):
    if num % 100 == 11 or num % 100 == 12 or num % 100 == 13 or num % 100 == 14:
        return f"{num} процентов"
    elif num % 10 == 1:
        return f"{num} процент"
    elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
        return f"{num} процента"
    else:
        return f"{num} процентов"


for i in range(1, 101):
    print(percent_maker(i))
