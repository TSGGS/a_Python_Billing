def get_input(message):
    try:
        selection = int(input(message))
    except:
        print("Invalid selection")
        return -1
    else:
        return selection
