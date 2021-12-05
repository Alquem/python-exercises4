words = input("sequence of words: ")
words_list = words.split(",")
words_list.sort()
print(",".join(words_list))