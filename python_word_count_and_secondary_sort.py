#word count and secondary sort

"""Count words."""
import operator
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    dict = {} 
    # TODO: Count the number of occurences of each word in s
    for x in s.split(" "):
        if x in dict:
            dict[x] +=1
        else:
            dict[x] = 1
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    print dict
    #top_n = sorted(dict.items())
    top_n = sorted(sorted(dict.items()),  key=lambda x: x[1], reverse = True)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n[0:n]


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()