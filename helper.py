def get_input(message):
    try:
        selection = int(input(message))
    except:
        print("Invalid selection")
        return -1
    else:
        return selection

def get_amount(message):
    try:
        amount = float(input(message))



    except:
        print("Invalid amount")
        return -1
    else:
        return amount