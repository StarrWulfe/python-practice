def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance
balance = withdraw_money(100, 80)
print("The balance is", balance)

if (balance <= 50):
    print("we need to make a deposit")
else:
    print('nothing to see here!')

           