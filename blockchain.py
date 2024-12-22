blockchain = []

def get_last_blocked_value():
    return blockchain[-1]
def add_value(transaction_amount, last_transaction =[1]):
    blockchain.append([last_transaction,transaction_amount])


trx_amount = input("Enter the transaction amount: ")
add_value(int(trx_amount))
add_value(last_transaction=get_last_blocked_value(), transaction_amount=3)
add_value(4, get_last_blocked_value())
print(blockchain)

