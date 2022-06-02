def thesaurus(*args):
    names_dict = {}
    for name in args:
        names_dict.setdefault(name[0], []).append(name)
    return {key: names_dict[key] for key in sorted(names_dict)}


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Анна", "Фёдор"))
