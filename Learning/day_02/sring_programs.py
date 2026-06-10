"""
Level 1: Basic String Programs (1-10)

These help you understand string operations and methods.

Print a string.
Find the length of a string.
Convert a string to uppercase.
Convert a string to lowercase.
Count the number of characters in a string.
Reverse a string.
Check whether a string is empty or not.
Concatenate two strings.
Print each character of a string using a loop.
Count the occurrences of a specific character in a string.
Level 2: Intermediate String Programs (11-20)

These introduce logic-building and interview concepts.

Check whether a string is a palindrome.
Count the number of vowels in a string.
Count the number of consonants in a string.
Count the number of words in a sentence.
Find the first occurrence of a character in a string.
Find the last occurrence of a character in a string.
Remove all spaces from a string.
Replace a word with another word in a string.
Check whether two strings are equal.
Check whether one string is a substring of another.
Level 3: Advanced String Programs (21-30)

These are commonly asked in interviews and coding assessments.

Check whether two strings are anagrams.
Find duplicate characters in a string.
Find the frequency of each character in a string.
Find the first non-repeating character in a string.
Find the first repeating character in a string.
Remove duplicate characters from a string.
Find the character with the maximum occurrence in a string.
Compress a string (Example: "aaabbc" → "a3b2c1").
Check whether a string contains only digits.
Reverse the words in a sentence without reversing the characters.
"""

#This class will explain about the above all the questions.

class Stringprograms:
    def __init__(self):
        pass

    # Existing Methods
    def string(self, text):
        return text

    def len_str(self, text):
        return len(text)

    def rev_str(self, text):
        return text[::-1]

    def lower_str(self, text):
        return text.lower()

    def upper_str(self, text):
        return text.upper()

    def is_empty(self, text):
        return len(text) == 0

    def concatenate(self, str1, str2):
        return str1 + str2

    def count_character(self, text, char):
        return text.count(char)

    def palindrome(self, text):
        return text == text[::-1]

    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0

        for ch in text:
            if ch in vowels:
                count += 1

        return count

    # 13. Count Consonants
    def count_consonants(self, text):
        vowels = "aeiouAEIOU"
        count = 0

        for ch in text:
            if ch.isalpha() and ch not in vowels:
                count += 1

        return count

    # 14. Count Words
    def count_words(self, text):
        return len(text.split())

    # 15. First Occurrence
    def first_occurrence(self, text, char):
        return text.find(char)

    # 16. Last Occurrence
    def last_occurrence(self, text, char):
        return text.rfind(char)

    # 17. Remove Spaces
    def remove_spaces(self, text):
        return text.replace(" ", "")

    # 18. Replace Word
    def replace_word(self, text, old, new):
        return text.replace(old, new)

    # 19. Compare Strings
    def compare_strings(self, str1, str2):
        return str1 == str2

    # 20. Check Substring
    def is_substring(self, main_string, sub_string):
        return sub_string in main_string

    # 21. Anagram Check
    def is_anagram(self, str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    # 22. Duplicate Characters
    def duplicate_characters(self, text):
        duplicates = []

        for ch in text:
            if text.count(ch) > 1 and ch not in duplicates:
                duplicates.append(ch)

        return duplicates

    # 23. Frequency of Each Character
    def character_frequency(self, text):
        freq = {}

        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        return freq

    # 24. First Non-Repeating Character
    def first_non_repeating(self, text):
        for ch in text:
            if text.count(ch) == 1:
                return ch
        return None

    # 25. First Repeating Character
    def first_repeating(self, text):
        seen = set()

        for ch in text:
            if ch in seen:
                return ch
            seen.add(ch)

        return None

    # 26. Remove Duplicate Characters
    def remove_duplicates(self, text):
        result = ""

        for ch in text:
            if ch not in result:
                result += ch

        return result

    # 27. Maximum Occurring Character
    def max_occurring_character(self, text):
        if not text:
            return ""
        freq = {}
        for ch in text:
            freq[ch] = freq.get(ch, 0) + 1

        return max(freq, key=freq.get)
    # 28. String Compression
    def compress_string(self, text):
        compressed = ""
        count = 1

        for i in range(len(text)):
            if i < len(text) - 1 and text[i] == text[i + 1]:
                count += 1
            else:
                compressed += text[i] + str(count)
                count = 1

        return compressed

    # 29. Check Digits Only
    def contains_only_digits(self, text):
        return text.isdigit()

    # 30. Reverse Words
    def reverse_words(self, text):
        words = text.split()
        return " ".join(words[::-1])
    
    def print_characters(self, text):
        chars = []
        for ch in text:
            chars.append(ch)
        return chars
    
# Create Object
obj = Stringprograms()

print("1. Print String:")
print(obj.string("Python"))

print("\n2. Length of String:")
print(obj.len_str("Python"))

print("\n3. Reverse String:")
print(obj.rev_str("Python"))

print("\n4. Lowercase:")
print(obj.lower_str("PYTHON"))

print("\n5. Uppercase:")
print(obj.upper_str("python"))

print("\n6. Check Empty String:")
print(obj.is_empty(""))
print(obj.is_empty("Python"))

print("\n7. Concatenate Strings:")
print(obj.concatenate("Hello ", "World"))

print("\n8. Count Character:")
print(obj.count_character("banana", "a"))

print("\n9. Palindrome Check:")
print(obj.palindrome("madam"))
print(obj.palindrome("python"))

print("\n10. Count Vowels:")
print(obj.count_vowels("Programming"))

print("\n11. Count Consonants:")
print(obj.count_consonants("Programming"))

print("\n12. Count Words:")
print(obj.count_words("Python is easy to learn"))

print("\n13. First Occurrence:")
print(obj.first_occurrence("banana", "a"))

print("\n14. Last Occurrence:")
print(obj.last_occurrence("banana", "a"))

print("\n15. Remove Spaces:")
print(obj.remove_spaces("Python is easy"))

print("\n16. Replace Word:")
print(obj.replace_word("Python is easy", "easy", "awesome"))

print("\n17. Compare Strings:")
print(obj.compare_strings("python", "python"))
print(obj.compare_strings("python", "java"))

print("\n18. Check Substring:")
print(obj.is_substring("Python Programming", "Program"))
print(obj.is_substring("Python Programming", "Java"))

print("\n19. Anagram Check:")
print(obj.is_anagram("listen", "silent"))
print(obj.is_anagram("hello", "world"))

print("\n20. Duplicate Characters:")
print(obj.duplicate_characters("programming"))

print("\n21. Character Frequency:")
print(obj.character_frequency("banana"))

print("\n22. First Non-Repeating Character:")
print(obj.first_non_repeating("aabbcdde"))

print("\n23. First Repeating Character:")
print(obj.first_repeating("abccde"))

print("\n24. Remove Duplicate Characters:")
print(obj.remove_duplicates("programming"))

print("\n25. Maximum Occurring Character:")
print(obj.max_occurring_character("programming"))

print("\n26. String Compression:")
print(obj.compress_string("aaabbccccdd"))

print("\n27. Contains Only Digits:")
print(obj.contains_only_digits("12345"))
print(obj.contains_only_digits("123abc"))

print("\n28. Reverse Words:")
print(obj.reverse_words("Python is awesome"))