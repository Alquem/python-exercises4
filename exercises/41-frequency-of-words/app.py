from collections import Counter

input_words = input().split()
input_words.sort()
word_count = dict(sorted(Counter(input_words).items()))
print(" ".join(":".join(str(j) for j in i) for i in word_count.items()))