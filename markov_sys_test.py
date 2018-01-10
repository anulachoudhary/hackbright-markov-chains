"""Generate Markov text from text files."""
    
from random import choice
import sys

# def open_and_read_file():
   
    # file_obj.close()
    # file_obj.close()   

    # with open(file_path) as file_obj:
    #     text = file_obj.read()

    # return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = text_string.split()

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])

        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        
        chains[key].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # start with an empty list
    # first, use choice() to select a random key from our dictionary
    # using that random key, select a random word from the list at the key
    # append these three words to the empty word list
    # our new key, will be the last two values of the words list-- we want this returned as a tuple
    # use this new key to look into the dictionary and at that key, get a new random word out of this new list

    # return a random tuple key from chains using choice
    random_starting_bigram = choice(chains.keys())

    # next word will be a random choice from the dictionary at the random starting bigram key
    next_word = choice(chains[random_starting_bigram]) 
    
    # extending our empty list words, with the starting_bigram 
    words.extend(random_starting_bigram)

    # also appending our list with the randomly selected word from our value list in our dict
    words.append(next_word)


    # WHILE LOOP
    while True:

        # generating our new bigram by indexing into our list to get our last two values and making that a tuple
        new_bigram = (words[-2], words[-1])

        # check whethe new_bigram is a key in our dict
        # if not, break
        # if so, cont. to new word

        if new_bigram not in chains:
            break
    
        # getting a random value from our dictionary at new_bigram
        new_word = choice(chains[new_bigram])

        # appending that new random word to our words list
        words.append(new_word)



    # while new_key is not None:
        
        
    #     words.append(next_word)

    #     new_key = (words[-2], words[-1])

    #     # new_text = random_bigram[0] + " " + random_bigram[1]

    #     # new_text += next_word

    #     # new_key = (random_bigram[1], next_word)

    print " ".join(words)
    return " ".join(words)


path = sys.argv[1]

with open(path) as file_obj:
# file_obj = open(file_path)
    text = file_obj.read()


# Get a Markov chain
chains = make_chains(text)

# Produce random text
random_text = make_text(chains)

print random_text
