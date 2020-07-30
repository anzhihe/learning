def save_transaction(price, credit_card, description): 
    file = open("transactions.txt", "a")
    file.write("%s%07d%s\n" % (credit_card, price * 100, description)) 
    file.close()
