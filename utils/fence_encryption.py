def remove_spaces(text):
    result = ""
    for letter in text:
        if letter != ' ':
            result += letter
    return result


def fence_encrypt(text: str):
    text = remove_spaces(text)
    result = text[0::2] + text[1::2]
    return result
    


def fence_decrypt(text: str):
    result = ""
    
    middle = len(text) //2 
    right_index = middle

    last = ""
    if len(text) % 2 == 1:
        last = text[right_index]
        right_index += 1

    for index in range(middle):
        result += text[index] + text[right_index]
        right_index += 1
     
    return result + last
