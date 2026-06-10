import unittest
from Learning.day_02.sring_programs import Stringprograms


class TestStringPrograms(unittest.TestCase):

    def setUp(self):
        self.obj = Stringprograms()

    # 1. string()
    def test_string(self):
        self.assertEqual(self.obj.string("Python"), "Python")
        self.assertEqual(self.obj.string(""), "")
        self.assertEqual(self.obj.string("123"), "123")
        self.assertEqual(self.obj.string("Hello World"), "Hello World")
        self.assertEqual(self.obj.string("A"), "A")

    # 2. len_str()
    def test_len_str(self):
        self.assertEqual(self.obj.len_str("Python"), 6)
        self.assertEqual(self.obj.len_str(""), 0)
        self.assertEqual(self.obj.len_str("A"), 1)
        self.assertEqual(self.obj.len_str("Hello World"), 11)
        self.assertEqual(self.obj.len_str("12345"), 5)

    # 3. rev_str()
    def test_rev_str(self):
        self.assertEqual(self.obj.rev_str("Python"), "nohtyP")
        self.assertEqual(self.obj.rev_str("madam"), "madam")
        self.assertEqual(self.obj.rev_str(""), "")
        self.assertEqual(self.obj.rev_str("A"), "A")
        self.assertEqual(self.obj.rev_str("123"), "321")

    # 4. lower_str()
    def test_lower_str(self):
        self.assertEqual(self.obj.lower_str("PYTHON"), "python")
        self.assertEqual(self.obj.lower_str("HELLO"), "hello")
        self.assertEqual(self.obj.lower_str(""), "")
        self.assertEqual(self.obj.lower_str("123"), "123")
        self.assertEqual(self.obj.lower_str("AbC"), "abc")

    # 5. upper_str()
    def test_upper_str(self):
        self.assertEqual(self.obj.upper_str("python"), "PYTHON")
        self.assertEqual(self.obj.upper_str("hello"), "HELLO")
        self.assertEqual(self.obj.upper_str(""), "")
        self.assertEqual(self.obj.upper_str("123"), "123")
        self.assertEqual(self.obj.upper_str("aBc"), "ABC")

    # 6. is_empty()
    def test_is_empty(self):
        self.assertTrue(self.obj.is_empty(""))
        self.assertFalse(self.obj.is_empty("Python"))
        self.assertFalse(self.obj.is_empty(" "))
        self.assertFalse(self.obj.is_empty("123"))
        self.assertFalse(self.obj.is_empty("A"))

    # 7. concatenate()
    def test_concatenate(self):
        self.assertEqual(self.obj.concatenate("Hello", "World"), "HelloWorld")
        self.assertEqual(self.obj.concatenate("", ""), "")
        self.assertEqual(self.obj.concatenate("Python", ""), "Python")
        self.assertEqual(self.obj.concatenate("", "Java"), "Java")
        self.assertEqual(self.obj.concatenate("123", "456"), "123456")

    # 8. count_character()
    def test_count_character(self):
        self.assertEqual(self.obj.count_character("banana", "a"), 3)
        self.assertEqual(self.obj.count_character("hello", "l"), 2)
        self.assertEqual(self.obj.count_character("", "a"), 0)
        self.assertEqual(self.obj.count_character("aaaa", "a"), 4)
        self.assertEqual(self.obj.count_character("python", "z"), 0)

    # 9. palindrome()
    def test_palindrome(self):
        self.assertTrue(self.obj.palindrome("madam"))
        self.assertTrue(self.obj.palindrome("racecar"))
        self.assertFalse(self.obj.palindrome("python"))
        self.assertTrue(self.obj.palindrome("a"))
        self.assertTrue(self.obj.palindrome(""))

    # 10. count_vowels()
    def test_count_vowels(self):
        self.assertEqual(self.obj.count_vowels("Programming"), 3)
        self.assertEqual(self.obj.count_vowels("AEIOU"), 5)
        self.assertEqual(self.obj.count_vowels("hello"), 2)
        self.assertEqual(self.obj.count_vowels(""), 0)
        self.assertEqual(self.obj.count_vowels("bcdfg"), 0)

    # 11. count_consonants()
    def test_count_consonants(self):
        self.assertEqual(self.obj.count_consonants("Programming"), 8)
        self.assertEqual(self.obj.count_consonants("hello"), 3)
        self.assertEqual(self.obj.count_consonants("AEIOU"), 0)
        self.assertEqual(self.obj.count_consonants(""), 0)
        self.assertEqual(self.obj.count_consonants("Python"), 5)

    # 12. count_words()
    def test_count_words(self):
        self.assertEqual(self.obj.count_words("Python is easy"), 3)
        self.assertEqual(self.obj.count_words("Hello"), 1)
        self.assertEqual(self.obj.count_words(""), 0)
        self.assertEqual(self.obj.count_words("one two three four"), 4)
        self.assertEqual(self.obj.count_words("a b c"), 3)

    # 13. first_occurrence()
    def test_first_occurrence(self):
        self.assertEqual(self.obj.first_occurrence("banana", "a"), 1)
        self.assertEqual(self.obj.first_occurrence("hello", "l"), 2)
        self.assertEqual(self.obj.first_occurrence("python", "z"), -1)
        self.assertEqual(self.obj.first_occurrence("", "a"), -1)
        self.assertEqual(self.obj.first_occurrence("aaaa", "a"), 0)

    # 14. last_occurrence()
    def test_last_occurrence(self):
        self.assertEqual(self.obj.last_occurrence("banana", "a"), 5)
        self.assertEqual(self.obj.last_occurrence("hello", "l"), 3)
        self.assertEqual(self.obj.last_occurrence("python", "z"), -1)
        self.assertEqual(self.obj.last_occurrence("", "a"), -1)
        self.assertEqual(self.obj.last_occurrence("aaaa", "a"), 3)

    # 15. remove_spaces()
    def test_remove_spaces(self):
        self.assertEqual(self.obj.remove_spaces("Python is easy"), "Pythoniseasy")
        self.assertEqual(self.obj.remove_spaces(" "), "")
        self.assertEqual(self.obj.remove_spaces("Hello World"), "HelloWorld")
        self.assertEqual(self.obj.remove_spaces(""), "")
        self.assertEqual(self.obj.remove_spaces("A B C"), "ABC")

    # 16. replace_word()
    def test_replace_word(self):
        self.assertEqual(self.obj.replace_word("Python is easy", "easy", "awesome"), "Python is awesome")
        self.assertEqual(self.obj.replace_word("hello world", "world", "python"), "hello python")
        self.assertEqual(self.obj.replace_word("", "a", "b"), "")
        self.assertEqual(self.obj.replace_word("aaa", "a", "b"), "bbb")
        self.assertEqual(self.obj.replace_word("python", "java", "c++"), "python")

    # 17. compare_strings()
    def test_compare_strings(self):
        self.assertTrue(self.obj.compare_strings("python", "python"))
        self.assertFalse(self.obj.compare_strings("python", "java"))
        self.assertTrue(self.obj.compare_strings("", ""))
        self.assertFalse(self.obj.compare_strings("A", "a"))
        self.assertTrue(self.obj.compare_strings("123", "123"))

    # 18. is_substring()
    def test_is_substring(self):
        self.assertTrue(self.obj.is_substring("Python Programming", "Program"))
        self.assertFalse(self.obj.is_substring("Python Programming", "Java"))
        self.assertTrue(self.obj.is_substring("hello", "ell"))
        self.assertFalse(self.obj.is_substring("", "a"))
        self.assertTrue(self.obj.is_substring("abc", "a"))

    # 19. is_anagram()
    def test_is_anagram(self):
        self.assertTrue(self.obj.is_anagram("listen", "silent"))
        self.assertTrue(self.obj.is_anagram("heart", "earth"))
        self.assertFalse(self.obj.is_anagram("python", "java"))
        self.assertTrue(self.obj.is_anagram("Race", "Care"))
        self.assertFalse(self.obj.is_anagram("abc", "abcd"))

    # 20. contains_only_digits()
    def test_contains_only_digits(self):
        self.assertTrue(self.obj.contains_only_digits("12345"))
        self.assertFalse(self.obj.contains_only_digits("123abc"))
        self.assertFalse(self.obj.contains_only_digits(""))
        self.assertTrue(self.obj.contains_only_digits("0"))
        self.assertFalse(self.obj.contains_only_digits("12.5"))

    # 21. reverse_words()
    def test_reverse_words(self):
        self.assertEqual(self.obj.reverse_words("Python is awesome"), "awesome is Python")
        self.assertEqual(self.obj.reverse_words("Hello World"), "World Hello")
        self.assertEqual(self.obj.reverse_words("A"), "A")
        self.assertEqual(self.obj.reverse_words(""), "")
        self.assertEqual(self.obj.reverse_words("one two three four"), "four three two one")

    def test_duplicate_characters(self):
        self.assertEqual(self.obj.duplicate_characters("programming"), ['r', 'g', 'm'])
        self.assertEqual(self.obj.duplicate_characters("banana"), ['a', 'n'])
        self.assertEqual(self.obj.duplicate_characters("abc"), [])
        self.assertEqual(self.obj.duplicate_characters("aaaa"), ['a'])
        self.assertEqual(self.obj.duplicate_characters(""), [])

    def test_character_frequency(self):
        self.assertEqual(self.obj.character_frequency("banana"),{'b': 1, 'a': 3, 'n': 2})
        self.assertEqual(self.obj.character_frequency("aaaa"),{'a': 4})
        self.assertEqual(self.obj.character_frequency("abc"),{'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(self.obj.character_frequency(""), {})
        self.assertEqual(self.obj.character_frequency("11"), {'1': 2})
    
    def test_first_non_repeating(self):
        self.assertEqual(self.obj.first_non_repeating("aabbcdde"), 'c')
        self.assertEqual(self.obj.first_non_repeating("swiss"), 'w')
        self.assertEqual(self.obj.first_non_repeating("abcd"), 'a')
        self.assertIsNone(self.obj.first_non_repeating("aabb"))
        self.assertIsNone(self.obj.first_non_repeating(""))

    def test_first_repeating(self):
        self.assertEqual(self.obj.first_repeating("abccde"), 'c')
        self.assertEqual(self.obj.first_repeating("banana"), 'a')
        self.assertEqual(self.obj.first_repeating("aabb"), 'a')
        self.assertIsNone(self.obj.first_repeating("abcd"))
        self.assertIsNone(self.obj.first_repeating(""))
    
    def test_remove_duplicates(self):
        self.assertEqual(self.obj.remove_duplicates("programming"), "progamin")
        self.assertEqual(self.obj.remove_duplicates("banana"), "ban")
        self.assertEqual(self.obj.remove_duplicates("aaaa"), "a")
        self.assertEqual(self.obj.remove_duplicates("abc"),"abc")
        self.assertEqual(self.obj.remove_duplicates(""), "")
    
    def test_max_occurring_character(self):
        self.assertIn(self.obj.max_occurring_character("programming"), ('r','g','m'))
        self.assertEqual(self.obj.max_occurring_character("banana"), 'a')
        self.assertEqual(self.obj.max_occurring_character("aaaa"), 'a')
        self.assertEqual(self.obj.max_occurring_character("abc"), 'a')
        self.assertEqual(self.obj.max_occurring_character(""), '')
    
    def test_compress_string(self):
        self.assertEqual(self.obj.compress_string("aaabbccccdd"),"a3b2c4d2")
        self.assertEqual(self.obj.compress_string("aaaa"), "a4")
        self.assertEqual(self.obj.compress_string("abc"), "a1b1c1")
        self.assertEqual(self.obj.compress_string("a"),"a1")
        self.assertEqual(self.obj.compress_string("aabb"),"a2b2")
    
    def print_characters(self, text):
        chars = []
        for ch in text:
            chars.append(ch)
        return chars

    def test_print_characters(self):
        self.assertEqual(self.obj.print_characters("Python"),['P', 'y', 't', 'h', 'o', 'n'])
        self.assertEqual(self.obj.print_characters("A"),['A'])
        self.assertEqual(self.obj.print_characters(""), [])
        self.assertEqual(self.obj.print_characters("123"), ['1', '2', '3'])
        self.assertEqual(self.obj.print_characters("ab"), ['a', 'b'])


if __name__ == "__main__":
    unittest.main(verbosity=2)