def thesaurus_adv(*args):
    names_dict = {}
    for name in args:
        first_name, last_name = name.split()
        names_dict.setdefault(last_name[0], {}).setdefault(first_name[0], []).append(name)
    return {key: names_dict[key] for key in sorted(names_dict)}


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
