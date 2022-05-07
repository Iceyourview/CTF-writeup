def rot13(sentence):
    return ''.join([chr((ord(letter) - 97 + 13) % 26 + 97)
                        if 97 <= ord(letter) <= 122
                        else letter
                    for letter in sentence.lower()])
# Executes the main function
if __name__ == '__main__':
    text = input('Input :')
    print(rot13(text))

