transaction_log = " "
while transaction_log:
    transaction_log = input()
    bank_account = 0
    for i,transaction in enumerate(transaction_log.split(" ")):
        if transaction == "D":
            bank_account += int(transaction_log.split(" ")[i+1])
        elif transaction == "W":
            bank_account -= int(transaction_log.split(" ")[i+1])
print("account balance: ", bank_account)