"""
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

def netAmount():
    listTransaction = []
    while True:
        transaction = input("Please enter a transaction: ")
        if len(transaction) != 0:
            listTransaction.append(transaction)
        else:
            break
    trans_hist = {"D":0, "W":0}
    for trans in listTransaction:
        x = trans.split()
        if x[0] == "D":
            trans_hist["D"] += int(x[1])
        elif x[0] == "W":
            trans_hist["W"] += int(x[1])
    return trans_hist["D"] - trans_hist["W"]

print(netAmount())

