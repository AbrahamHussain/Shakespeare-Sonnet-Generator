# file for testing syllable issue on fake words

from nltk.corpus import cmudict

# finds the number of syllables in a word.
d = cmudict.dict()

# does not work if word is not recognized in NLTK
def nsyl(word):
    try:
        s = [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    except KeyError:
        new_word = word[:-1]
        s = nsyl(new_word)
    return s


def main():
    strings = ['dogs', 'beauty', 'tomato', 'showst', 'ffsfas']


    for string in strings:
        print nsyl(string)

main()