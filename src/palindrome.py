import re
def is_palindrome(word: str) -> bool:
    word = re.sub(r'[^a-záéíóúüñ]', '', word.lower())
    if word[0::] == word[::-1]:
        return True 
    else:
        return False