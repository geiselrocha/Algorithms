def is_palindrome_iterative(word):
    if not word:
        return False

    word = word.lower()
    reversed_word = word[::-1]

    for n in range(0, len(word)):
        if word[n] != reversed_word[n]:
            return False

    return True
