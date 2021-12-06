sentence = input("write the sentence: ")
letters = 0
digits = 0
letter_list = "abcdefghijklmnopqrstuvwxyz"
digit_list = "0123456789"
for character in sentence:
    if character in letter_list:
        letters += 1
    elif character in digit_list:
        digits += 1
print("LETTERS "+str(letters), "DIGITS "+str(digits))