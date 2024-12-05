def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    s = s.replace(" ", "")
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

# Test
print(count_vowels_consonants("Hello World"))  # (3, 7)
