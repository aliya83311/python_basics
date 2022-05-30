def thesaurus(*args):
    names_dict = {}
    for name in args:
        names_dict.setdefault(name[0], []).append(name)
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
