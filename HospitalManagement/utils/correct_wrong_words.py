import enchant

d = enchant.Dict("en_US")


def fix_wrong_words(text):
    words = text.split()
    fixed_text = []
    for word in words:
        if d.check(word):
            fixed_text.append(word)
        else:
            suggestions = d.suggest(word)
            if suggestions:
                fixed_text.append(suggestions[0])
            else:
                fixed_text.append(word)
    new_fixed_text = " ".join(fixed_text)
    return new_fixed_text
