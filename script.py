letters_of_alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!,?.' "
ciphered_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
message = ""
for letter in ciphered_message:
    if not letter in punctuation:
        letter_value = letters_of_alphabet.find(letter)
        message += letters_of_alphabet[(letter_value + 10) % 26]
    else:
        message += letter
print(message)
print("===================")
letters_of_alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = "!,?.' "
ciphered_message = ""
message = "hey buddy, got your message. took me a while to decode. I really needed alot of help."
for letter in message:
    if not letter in punctuation:
        letter_value = letters_of_alphabet.find(letter)
        ciphered_message += letters_of_alphabet[(letter_value - 10) % 26]
    else:
        ciphered_message += letter
print(ciphered_message)

print("============================")

def decoder(message, offset):
    letters_of_alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "!,?.' "
    deciphered_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = letters_of_alphabet.find(letter)
            deciphered_message += letters_of_alphabet[(letter_value + offset) % 26]
        else:
            deciphered_message += letter
    return deciphered_message
print(decoder("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.",10))

print("=========================")
print(decoder("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",7)
)
print("=========================")

def vigenere_decoder(coded_message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_pointer = 0
    keyword_final = ''
    for i in range(0, len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(coded_message)):    
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))
print("=================================")

def vigenere_coder(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(vigenere_coder(message_for_v,keyword))
print(vigenere_decoder(vigenere_coder(message_for_v, keyword), keyword))
print("==============================")
