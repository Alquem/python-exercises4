letter_list = "abcdefghijklmnopqrstuvwxyz"
upper_letter_list = "abcdefghijklmnopqrstuvwxyz".upper()
upper_case = 0
lower_case = 0
sentence = input("write the sentence: ")
for character in sentence:
    if character in letter_list:
        lower_case += 1
    elif character in upper_letter_list:
        upper_case += 1
print("UPPER CASE "+str(upper_case), "LOWER CASE "+str(lower_case))