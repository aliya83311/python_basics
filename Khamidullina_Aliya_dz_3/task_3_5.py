from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, repeat=True):
    """ Make jokes from lists.

    Arguments:
    num -- required. Sets the number of jokes the user wants to make.
    repeat -- optional. Defines if one word can be used in multiple jokes.

    The function returns a list containing strings.
    """
    result = []
    if repeat:
        for n in range(num):
            noun = nouns[randrange(len(nouns))]
            adverb = adverbs[randrange(len(adverbs))]
            adjective = adjectives[randrange(len(adjectives))]
            result.append(f"{noun} {adverb} {adjective}")
        return result
    else:
        nouns1 = nouns.copy()
        adverbs1 = adverbs.copy()
        adjectives1 = adjectives.copy()
        try:
            for n in range(num):
                noun = nouns1[randrange(len(nouns1))]
                adverb = adverbs1[randrange(len(adverbs1))]
                adjective = adjectives1[randrange(len(adjectives1))]
                result.append(f"{noun} {adverb} {adjective}")
                nouns1.pop(nouns1.index(noun))
                adverbs1.pop(adverbs1.index(adverb))
                adjectives1.pop(adjectives1.index(adjective))
        except ValueError:
            print("Закончились слова в списках!")
        finally:
            return result


print(get_jokes(8, False))
