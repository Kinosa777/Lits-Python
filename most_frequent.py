def find_most_frequent(text):
    """Returns the most frequently used words used in txt.
    All words are in lower case.
    If more than one - sorts the list in alphabetical order."""
    text = text.lower()
    for punct in ',.:;!?-':
        text = text.replace(punct, ' ')
    words = text.split()
    uses = {}
    for wrd in words:
        if wrd not in uses:
            uses[wrd] = 1
        else:
            uses[wrd] += 1
    max_value = max(uses.values())
    frequent = []
    for wrd in uses:
        if uses.get(wrd) == max_value:
            frequent.append(wrd)
    frequent.sort()
    return frequent


print(find_most_frequent('Hello,Hello, my dear!'))
print(find_most_frequent('to understand recursion you need first to understand recursion...'))
print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))
print(find_most_frequent("Hello,Hello, my dear!"))
