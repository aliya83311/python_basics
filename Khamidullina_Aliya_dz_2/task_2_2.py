weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def add_zero(seq):
    for item in range(len(seq)):
        if seq[item].startswith('+'):
            seq[item] = seq[item].replace('+', '0')
        if seq[item].isdigit():
            seq[item] = seq[item].zfill(2)
    seq = ['"' + item + '"' if item.isdigit() else item for item in seq]
    return ' '.join(seq)


print(id(weather))
print(add_zero(weather))
print(id(weather))
