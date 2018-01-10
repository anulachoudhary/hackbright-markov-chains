"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    
    file_name = open(file_path)
    text = file_name.read()
    file_name.close()   


    return text


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
        keys = (words[i], words[i + 1])

        values = words[i + 2]

        if keys not in chains:

            chains[keys] = [values]

        else:
            chains[keys].append(values)

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

    # return a random tuple key from chains using
    random_starting_bigram = choice(chains.keys())

    # next word will be a random choice from the dictionary at the random starting bigram key
    next_word = choice(chains[random_starting_bigram]) 

    # casting the tuple as a list
    random_starting_bigram = list(random_starting_bigram)

    print "Random_bigram", random_starting_bigram

    # extending our empty list words, with the starting_bigram 
    words.extend(random_starting_bigram)

    # also appending our list with the randomly selected word from our value list in our dict
    words.append(next_word)

    print words

    ###WHILE LOOP:

    # generating our new bigram by indexing into our list to get our last two values and making that a tuple
    new_bigram = (words[-2], words[-1])

    print new_bigram

    # getting a random value from our dictionary at new_bigram
    new_word = choice(chains[new_bigram])

    # appending that new random word to our words list
    words.append(new_word)

    print words

    # while new_key is not None:
        
        
    #     words.append(next_word)

    #     new_key = (words[-2], words[-1])

    #     # new_text = random_bigram[0] + " " + random_bigram[1]

    #     # new_text += next_word

    #     # new_key = (random_bigram[1], next_word)


    # return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)



# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
