def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

# Example usage
str1 = input("Enter 1st word: ")
str2 = input("Enter 2nd word: ")

if are_anagrams(str1, str2):
    print("The given words are anagrams.")
else:
    print("The given words are not anagrams.")

