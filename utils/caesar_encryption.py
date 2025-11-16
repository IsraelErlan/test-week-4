LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
LEN_LETTERS = 26

def caeser_encrypt(text: str, offset: int):
    text = text.lower()
    offset = offset%26

    result_text = ""
    for letter in text:
        if letter.isalpha():
            letter_idx = LETTERS.index(letter)
            encrypt_letter_index = letter_idx - (LEN_LETTERS - offset)
            result_text += LETTERS[encrypt_letter_index]
        elif letter == ' ':
            result_text += ' '
        else: 
            print(f"Please note that {letter} is not letter.")
    return result_text


def caeser_decrypt(text: str, offset: int):
    text = text.lower()
    offset = offset%26

    result_text = ""
    for letter in text:
        if letter.isalpha():
            letter_idx = LETTERS.index(letter)
            result_text += LETTERS[letter_idx - offset]
        elif letter == ' ':
            result_text += ' '
        else: 
            print(f"Please note that {letter} is not letter.")

    return result_text
