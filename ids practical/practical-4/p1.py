# 1. Create a list of words from the sentence given by the user.
sentence = input("Enter a sentence: ")
words_list = sentence.split()

# 2. Join the above created list of words using ‘#’ symbol.
joined_string = "#".join(words_list)

# 3. Replace a substring of the main string with another string.
substring_to_replace = input("Enter a substring to replace: ")
replacement_string = input("Enter the replacement string: ")
modified_string = joined_string.replace(substring_to_replace, replacement_string)

# 4. Check whether the main string starts with the given string.
start_string = input("Enter a string to check if the main string starts with it: ")
starts_with_check = modified_string.startswith(start_string)

# 5. Check whether the main string ends with the given string.
end_string = input("Enter a string to check if the main string ends with it: ")
ends_with_check = modified_string.endswith(end_string)

# 6. Remove extra space from the given string using strip() method.
stripped_string = modified_string.strip()

# 7. Check whether the given string is numeric or not.
numeric_check = stripped_string.isnumeric()

# 8. Write a program to check given input is palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

palindrome_check = is_palindrome(stripped_string)

# Display results
print(f"List of words: {words_list}")
print(f"Joined string: {joined_string}")
print(f"Modified string: {modified_string}")
print(f"Starts with '{start_string}': {starts_with_check}")
print(f"Ends with '{end_string}': {ends_with_check}")
print(f"Stripped string: {stripped_string}")
print(f"Is numeric: {numeric_check}")
print(f"Is palindrome: {palindrome_check}")

