import string

def check_alphabet(sentence_str):
    # Convert the sentence to lowercase and remove non-alphabetic characters
    sentence_str = sentence_str.lower()
    
    # Set of all letters in the alphabet
    alphabet_set = set(string.ascii_lowercase)
    
    # Create a set of letters found in the sentence
    sentence_set = set(char for char in sentence_str if char in alphabet_set)
    
    # Check if the sentence contains every letter of the alphabet
    if sentence_set == alphabet_set:
        return True
    else:
        # If not, find the missing letters
        missing_letters = alphabet_set - sentence_set
        print(f"Missing letters: {', '.join(sorted(missing_letters))}")
        return False

# Example usage
sentence = input("Enter a sentence: ")
if check_alphabet(sentence):
    print("The sentence contains every letter of the alphabet.")
else:
    print("The sentence does not contain every letter of the alphabet.")
