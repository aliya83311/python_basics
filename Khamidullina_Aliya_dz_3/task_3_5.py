from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# words = ["похоже", "к сожалению", "почему-то", "внезапно", "наконец-то"]


def get_jokes(num, repeat=True, **kwargs):
    """ Make jokes from strings stored in lists.

        Keyword arguments:
        num -- required. The number of jokes the user wants to make.
        repeat -- optional. If True, one word can be used in multiple jokes.
        If False, one word can be used in one joke only.
        kwargs -- required. Any number of lists from which jokes should be made.

        Returns a list containing strings.
        """
    result = []
    if repeat:
        for i in range(num):
            joke = ""
            for value in kwargs.values():
                joke += f"{value[randrange(len(value))]} "
            result.append(joke[:-1])
        return result
    else:
        try:
            for i in range(num):
                joke = ""
                for value in kwargs.values():
                    word = value[randrange(len(value))]
                    joke += f"{word} "
                    value.remove(word)
                result.append(joke[:-1])
        except ValueError:
            print("Закончились слова в списках!")
        finally:
            return result


print(get_jokes(4, False, nouns=nouns, adverbs=adverbs, adjectives=adjectives))
