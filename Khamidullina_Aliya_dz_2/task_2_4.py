employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']


def greeting(seq):
    for idx, item in enumerate(seq):
        seq[idx] = item.split()
        print(f"Привет, {seq[idx][len(seq[idx]) - 1].title()}!")


print(id(employees))
print(greeting(employees))
print(id(employees))
