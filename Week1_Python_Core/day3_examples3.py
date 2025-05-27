
##Simulate an ATM that checks if you have enough balance.

balance = 5000
withdraw = int(input("Enter amount to Withdraw: "))

if withdraw > balance:
    print("insufficiant balance! your currant balance is:", balance)
else:
    balance -= withdraw
    print("withdrawal successful. new balance", balance)