weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def add_zero(seq):
    for item in range(len(seq)):
        if seq[item].startswith('+'):
            seq[item] = seq[item].replace('+', '0')
            seq[item] = f'"+{seq[item]}"'
        if seq[item].isdigit():
            seq[item] = f'"{seq[item].zfill(2)}"'
    return ' '.join(seq)


print(id(weather))
print(add_zero(weather))
print(id(weather))
