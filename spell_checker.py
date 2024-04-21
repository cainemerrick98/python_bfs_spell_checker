from english_words import get_english_words_set
from string import ascii_lowercase
from collections import deque

class SpellCheckerBase:
    """
    A base class for spell checkers. Implements the word validation,
    the method to check for a correctly spelt word and the initialisation 
    of the dictionary of words and english letters.The abstract method 'check spelling' 
    should be overridden by subclasses to implement their own strategy for spell checking.
    """

    def __init__(self):
        self.words = get_english_words_set(['web2'], lower=True)
        self.alphabet = [letter for letter in ascii_lowercase]
        self.max_word_length = max(*map(len, self.words))

    def check_spelling(self, word=None):
        raise NotImplementedError('this method should be overridden')
    
    def is_an_english_word(self, word:str)->bool:
        """
        Checks if the word exists in the set of legitimate english words.
        """
        if word in self.words:
            return True
        
        return False

    def validate_characters(self, word:str):
        """
        Ensures the word passed to the spell checker only contains
        ascii lowercase letters, there is no leading or trailing 
        whitespace.
        """
        if word.startswith('\s') or word.endswith('\s'):
            raise ValueError('word contains trailing or leading whitespace')
        
        for char in word:
            if char not in self.alphabet:
                raise ValueError(f'word contains non ascii lowercase character: "{char}"')
        
        return True
    


class SpellCheckerBFS(SpellCheckerBase):

    def __init__(self):
        super().__init__()

    def check_spelling(self, word:str):
        """
        Implements a BFS algorithm for finding legitimate alternatives
        to the word passed to the method.
        """
        if self.is_an_english_word(word):
            return word
        
        if self.validate_characters(word):
            checked = []

            graph = {}
            graph[word] = self.find_connected_nodes(word, checked) #a graph connecting words to their one step variations
            
            queue = deque() #a queue of the words we need to check
            queue.extend(graph[word])
            iters = 0
            while queue:
                word_to_check = queue.popleft()
                if word_to_check not in checked:    
                    checked.append(word_to_check)
                    if self.is_an_english_word(word_to_check):
                        yield word_to_check
                    else:
                        graph[word_to_check] = self.find_connected_nodes(word_to_check, checked)
                        queue.extend(graph[word_to_check])
                iters+=1
                if iters >= 5:
                    break
            
            return None


    def find_connected_nodes(self, word:str, checked:list[str]) -> list[str]:
        """
        Given a word finds all the possible variations of the word
        by substituting each letter of the word with another word from 
        the alphabet
        """
        variations = []

        for i in range(len(word)):
            for letter in self.alphabet:
                if word[i] != letter:
                    variation = word[:i]+letter+word[i+1:]
                    if variation not in checked:
                        variations.append(variation)
        
        return variations
