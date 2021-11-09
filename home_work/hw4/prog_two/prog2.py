'''
Author      Jonathan Hogan
Class       Dr.Das - CMPS 4143 Contemporary Programming Languages
Due         11/10/21    

(35 points)Given an array of strings, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.
'''

def get_anagrams(words):
    anagrams = {}
    for word in words:
        #Sort the words
        key = ''.join(sorted(word))
        #Check if the sorted word is already a key in the anagrams dictionary
        if key not in anagrams:
            #If not, add the key
            anagrams[key] = []
        #Add the word to the group
        anagrams[key].append(word)
    #Return a list of anagrams
    return [val for key,val in anagrams.items()]

wordList = ['eat','tea','tan','ate','nat','bat']
print(get_anagrams(wordList))