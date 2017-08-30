"""Generate Markov text from text files."""

from random import choice
from sys import argv


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_name = (open(file_path)).read()
    return file_name



def make_chains(text_string, n_gram):
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
    for i in range(len(words)-n_gram):
        temp_list = []
        for z in range(n_gram):
            temp_list = temp_list + [words[i + z]]

        temp_tup = tuple(temp_list)

        # if temp_tup in chains:
        #     chains[temp_tup] = chains[temp_tup] + [words[i + 2]]
        # else:
        #     chains[temp_tup] = [words[i + 2]]
        chains.setdefault(temp_tup, [])
        chains[temp_tup].append(words[i + n_gram])
        #chains[temp_tup] = chains.get(temp_tup, []) + [words[i + 2]]
    print chains
    return chains


def make_text(chains, n_gram):
    """Return text from chains."""
    words = []

    link_key = choice(chains.keys())


    while True:
        if link_key[0] != link_key[0].capitalize():
            link_key = choice(chains.keys())
        else:
            break
    #have random key from our dict

    words = list(link_key)

    while link_key in chains.keys():
        next_word = choice(chains[link_key])

        words.append(next_word)

        next_key = list(link_key[1:]) + [next_word]

        link_key = tuple(next_key)

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(argv[1])

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains, 2)

print random_text

len(chains.keys())
