nums_dict = {
    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate_adv(word):
    if word.istitle():
        word = word.lower()
        return nums_dict.get(word).capitalize()
    else:
        word = word.lower()
        return nums_dict.get(word)


user_word = input("Type any number from 0 to 10: ")
print(num_translate_adv(user_word))
