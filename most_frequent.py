def find_most_frequent(text):
    """Returns the most frequently used words used in txt"""
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
    max_value = 0
    for wrd in uses:
        if uses.get(wrd) == max_value:
            frequent.append(wrd)
        elif uses.get(wrd) > max_value:
            frequent = [wrd,]
            max_value = uses.get(wrd)
    frequent.sort()
    return frequent


print(find_most_frequent('Hello,Hello, my dear!'))
print(find_most_frequent('to understand recursion you need first to understand recursion...'))
print(find_most_frequent('Mom! Mom! Are you sleeping?!!!'))
print(find_most_frequent("Hello,Hello, my dear!"))




