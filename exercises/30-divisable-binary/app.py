csv_sequence = input()
for binary in csv_sequence.split(","):
    if int(binary, base=2) % 5 == 0:
        print(binary)
    