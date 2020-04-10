def backspace(s):
    result = ''
    for i in range(len(s)):
        if s[i] =='#':
            result = result[:-1]
        else:
            result = result + s[i]

    return result

print(backspace('a##c'))
print(backspace('#a#c'))

print(backspace("ab##"))
print(backspace("c#d#"))
# "ab##", T = "c#d#"