def caesar(text, sh):
    result=''
    for i in range(len(text)):
        ch = text[i]
        if ch.isupper(): # for uppercase characters
            result += chr((ord(ch)+sh-65)%26+65)
        else:            # for lowercase characters
            result += chr((ord(ch)+sh-97)%26+97)
    return result
#text = str(input('Input text:'))
#sh = int(input('Input shift :'))
text = str('ynkooejcpdanqxeykjrbdofgkq')
print('text : ', text)
for i in range(27):
    print('shift', i, ' : picoCTF{',caesar(text, i), '}',sep='')
