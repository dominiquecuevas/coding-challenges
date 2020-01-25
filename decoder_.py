string = "0h1ae2bcy"

def decoder(string):
    
    code = ""
    for idx, char in enumerate(string):
        if char.isdigit():
            code += string[idx + int(char) + 1]
    
    return code