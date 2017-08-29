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
    for i in range(len(words)-2):
        temp_tup = (words[i], words[i + 1])
        # if temp_tup in chains:
        #     chains[temp_tup] = chains[temp_tup] + [words[i + 2]]
        # else:
        #     chains[temp_tup] = [words[i + 2]]
        chains.setdefault(temp_tup, [])
        chains[temp_tup].append(words[i + 2])
        #chains[temp_tup] = chains.get(temp_tup, []) + [words[i + 2]]

    return chains


print make_chains('Hello I hackbright am at I hackbright test')
