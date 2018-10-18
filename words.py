import sys
import string
from collections import deque
# Author: Emily Vogelsperger
# Date: Fall 2018
# Filename: words.py
#
# Description: Implementation of a search algorithm to find a
# shortest path of words from a given start word to a given
# goal word. At each step, any single letter in the word
# can be changed to any other letter, provided
# that the resulting word is also in the dictionary.
#
# A dictionary of English words a text file, a start word,
# and a goal word are passed as command line arguments.
#
# Usage: python3 words.py dictionaryFile startWord endWord

def read_file(filename):
    """Read in each word from a dictionary where each
    word is listed on a single line."""
    print("Reading dictionary: " +filename)
    word_dict = set()

    dictionary = open(filename)

    # Read each word from the dictionary
    for word in dictionary:
        # Remove the trailing newline character
        word = word.rstrip('\n')

        # Convert to lowercase
        word = word.lower()

        word_dict.add(word)

    dictionary.close()

    return word_dict

class Node:
    def __init__(self, state, parent = None):
        self.state = state
        self.parent = parent

def find_path(startWord, goalWord, word_dict):
    """Returns a list of words in word_dict
    that form the shortest path from startWord to goalWord,
    and returns None if no such path exists."""

    frontier = deque()
    explored = set()
    solution = set()

    tree = Node
    tree.state = startWord

    if tree.state == goalWord:
        return tree

    frontier.append(tree)

    while frontier:
        # pop from frontier
        parentWord = frontier.pop()
        # add to explored
        explored.add(parentWord.state)
        # start exploring every available action
        for i in range(len(parentWord.state)):
            for k in string.ascii_lowercase:
                childWord = Node
                childWord.parent = parentWord
                childWord.state = parentWord.state[:int(i)] + string.ascii_lowercase[int(k)] + parentWord.state[int(k):]
                if childWord not in word_dict:
                    if childWord not in explored:
                        if childWord not in frontier:
                            if childWord.state.equals(goalWord):
                                # backtrack through the linked list
                                while childWord.parent != None:
                                    solution.append(childWord.state)
                                    childWord = childWord.parent
                                return solution

    return None

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 words.py dictionaryFile startWord goalWord")
    else:
        dictionaryFile = sys.argv[1]
        startWord = sys.argv[2]
        goalWord = sys.argv[3]

        word_dict = set()
        word_dict = read_file(dictionaryFile)

        if startWord not in word_dict:
            print(startWord + " is not in the given dictionary.")
        else:
            print("-- Shortest path from " + startWord + " to " + goalWord + " --")

            solution = find_path(startWord, goalWord, word_dict)

            if(solution is None):
                print("None exists!")
            else:
                for word in solution:
                    print(word)

if __name__ == "__main__":
    main()
