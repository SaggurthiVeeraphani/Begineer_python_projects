from spellchecker import spellchecker, SpellChecker

checker = SpellChecker()

input_word = input("enter the word to check: ")

if input_word in checker:
    print("you entered the correct word")
else:
    correct_word = checker.correction(input_word)
    print(correct_word)



