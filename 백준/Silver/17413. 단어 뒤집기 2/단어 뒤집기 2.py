import sys

def reverse_words_in_string(s):
    result = []
    word = []
    in_tag = False

    for char in s:
        if char == '<':
            if word:
                result.extend(word[::-1])
                word = []
            in_tag = True
            result.append(char)
        elif char == '>':
            in_tag = False
            result.append(char)
        elif in_tag:
            result.append(char)
        else:
            if char == ' ':
                result.extend(word[::-1])
                result.append(char)
                word = []
            else:
                word.append(char)
    
    if word:
        result.extend(word[::-1])

    return ''.join(result)

if __name__ == "__main__":
    input_string = sys.stdin.readline().strip()
    print(reverse_words_in_string(input_string))
