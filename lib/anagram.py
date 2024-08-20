# your cod
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        # Sort the characters of the word to create a standard form
        sorted_word = sorted(self.word)
        
        # Return the list of anagrams
        return [anagram for anagram in possible_anagrams if sorted(anagram.lower()) == sorted_word]


