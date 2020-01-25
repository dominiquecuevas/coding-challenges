def decoder(string):
    code = ""
    for idx, char in enumerate(string):
        if char.isdigit():
            key_idx = idx + 1 + int(char)
            letter = string[key_idx]
            code += letter
    return code