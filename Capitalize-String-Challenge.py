def capitalize():
    str = input("Enter a string to capitalize: ")
    words = str.split(' ')
    words_capitalized = []
    for word in words:
        first_letter = word[0].upper()
        rest_of_word = word[1:]
        capitalized_word = first_letter + rest_of_word
        words_capitalized.append(capitalized_word)
    return ' '.join(words_capitalized)
def main():
    capitalized_string = capitalize()
    print(capitalized_string)
if __name__ == '__main__':
    main()
def capitalize():
    user_string = input("Enter a string to capitalize: ")
    words = user_string.split(' ')
    capitalized_words = []
    for word in words:
        first_letter = word[0].upper()
        rest_of_word = word[1:]
        capitalized_word = first_letter + rest_of_word
        capitalized_words.append(capitalized_word)
    capitalized_string = ' '.join(capitalized_words)
    return capitalized_string
def main():
    capitalized = capitalize()
    print(capitalized)
if __name__ == '__main__':
    main()
