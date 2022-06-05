# Version 1
def make_tuples(lst1, lst2):
    """ Make tuples from two lists.

    :param lst1: list of tutors
    :param lst2: lists of classes
    :return: tuples containing names of tutors and classes
    """
    while len(lst1) > len(lst2):
        lst2.append(None)
    return zip(lst1, lst2)


# Version 2
# from itertools import zip_longest
#
#
# def make_tuples(*args):
#     """ Make tuples from two or more lists
#
#     :param args: lists containing names of tutors and classes
#     :return: tuples containing names of tutors and classes
#     """
#     return zip_longest(*args)


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А']

lessons = make_tuples(tutors, classes)
print(type(lessons))
for lesson in lessons:
    print(lesson)
print(next(lessons))
