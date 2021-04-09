# For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

word_list = ['hello', 'world']
for word in word_list:
    print(word.upper())
    
# Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

def print_upper_words(word_list):
    """Prints words from a list of words in uppercase""" 
    for word in word_list:
        print(word.upper())

# Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

def only_e_words(word_list):
    for word in word_list:
        if word.startswith('e') or word.startswith('E'):
            print(word.lower())

# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words(word_list, must_start_with):
    for word in word_list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper()) 
