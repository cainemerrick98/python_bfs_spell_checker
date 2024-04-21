import unittest
from spell_checker import SpellCheckerBase, SpellCheckerBFS

class TestBaseImplementations(unittest.TestCase):

    def setUp(self):
        self.spellchecker_base = SpellCheckerBase()
        self.english_word = 'hello'
        self.not_english_word = 'worldd'
        self.invalid_chars_ws = ' hello '
        self.invalid_chars_na = '_hello'

    def test_max_word_length(self):
        self.assertEqual(28, self.spellchecker_base.max_word_length)

    def test_is_an_english_word_valid_word(self):
        self.assertTrue(self.spellchecker_base.is_an_english_word(self.english_word))

    def test_is_an_english_word_invalid_word(self):
        self.assertFalse(self.spellchecker_base.is_an_english_word(self.not_english_word))
    
    def test_valid_characters_valid(self):
        self.assertTrue(self.spellchecker_base.validate_characters(self.english_word))
        self.assertTrue(self.spellchecker_base.validate_characters(self.not_english_word))
    
    def test_valid_characters_invalid(self):
        self.assertRaises(ValueError, self.spellchecker_base.validate_characters, word=self.invalid_chars_na)
        self.assertRaises(ValueError, self.spellchecker_base.validate_characters, word=self.invalid_chars_ws)
    
    def test_check_spelling_not_implemented(self):
        self.assertRaises(NotImplementedError, self.spellchecker_base.check_spelling)


class TestSpellCheckerBFS(unittest.TestCase):
    def setUp(self):
        self.spellchecker = SpellCheckerBFS()
        self.word = 'helol'
        self.letter = 'a'
    
    def test_find_connected_nodes(self):
        connections = self.spellchecker.find_connected_nodes(self.letter, [])
        self.assertEqual(len(connections), 25)

    def test_check_spelling(self):
        correct_word_generator = self.spellchecker.check_spelling(self.word)
        for i in correct_word_generator:
            print(i)

