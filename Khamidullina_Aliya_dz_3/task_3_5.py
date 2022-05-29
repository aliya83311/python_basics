from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """ Make jokes from lists.

    Arguments:
    num -- number of jokes the user wants to make.
    """
    result = []
    for n in range(num):
        noun = nouns[randrange(len(nouns))]
        adverb = adverbs[randrange(len(adverbs))]
        adjective = adjectives[randrange(len(adjectives))]
        result.append(f"{noun} {adverb} {adjective}")
    return result


print(get_jokes(3))
