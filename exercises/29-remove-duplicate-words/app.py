words_sequence = input()
removed_duplicate_words = " ".join(sorted(set(words_sequence.split(" "))))
print(removed_duplicate_words)