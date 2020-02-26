#V1

print "Hello, today I will be coding Blockchain technology on this Mac computer"

def greet():
    print"Let's Begin."

greet()

#Define a function to make the code cleaner

def get_last_blockchain_value():
    return blockchain[-1]

#How Do You Define It


blockchain = []

#Default Arguments
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=0.9) # --- X

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)
add_value(10.89, get_last_blockchain_value()) #---- X

print(blockchain)
#Storing Nested lists




#THIS VERSION HAS ISSUES


#V2

print "Hello, today I will be coding Blockchain technology on this Mac computer"

def greet():
    print"Let's Begin."

greet()

#Define a function to make the code cleaner

def get_last_blockchain_value():
    return blockchain[-1]

#How Do You Define It


blockchain = []

#Default Arguments
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount)

tx_amount = float(input('Your transaction amount please: '))
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = float(input('Your transaction amount please: '))
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
#Storing Nested lists



#V3 Even cleaner code

print "Hello, today I will be coding Blockchain technology on this Mac computer"

def greet():
    print"Let's Begin."

greet()

#Define a function to make the code cleaner

def get_last_blockchain_value():
    return blockchain[-1]

#How Do You Define It


blockchain = []

#Default Arguments
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])

def get_user_input():
    return float(input('Your transaction amount please: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)
#Storing Nested lists

