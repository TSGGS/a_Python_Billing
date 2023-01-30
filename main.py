from helper import *
import random

def main():
    global items

    items = [
        {"id": 1, "name": "LA Lakers", "unit_price": 330},
        {"id": 2, "name": "Chicago Bulls", "unit_price": 350},
        {"id": 3, "name": "Golden State Warriors", "unit_price": 330},
        {"id": 4, "name": "New York Knicks", "unit_price": 330},
        {"id": 5, "name": "Gilas Pilipinas", "unit_price": 300},
    ]

    print("BILLING SYSTEM\n")
    print("Menu Options")
    print("[1] Scan Items")
    print("[2] Edit Items")
    print("[3] View Scanned Items")
    print("[0] Exit\n")

    session_exit = False
    while not session_exit:
        selected_option = get_input("Selected Option: ")

        if selected_option == 0:
            exit()

        elif selected_option == 1:
            scan_items()

        elif selected_option == 2:
            edit_scanned_items()

        elif selected_option == 3:
            view_scanned_items()

        elif selected_option == 4:
            generate_receipt()

        else:
            print("Invalid selection")

def scan_items():
    print("\nSCAN ITEMS")
    print("Scan customer's items\n")

    print("Items")
    for item in items:
        print(f"[%s] %s" % (item["id"], item["name"]))

    print("\n[0] End Scan\n")

    done = False
    while not done:
        item_selection = get_input("\nItem Selection: ")

        if item_selection > 0  and item_selection <= len(items):
            item_index = findItem(item_selection)

            if item_index != -1:
                qty = get_input("Add quantity to %s: " % items[item_selection - 1]["name"])
                if qty > 0:
                    cart[item_index]["qty"] += qty
            else:
                qty = get_input("Quantity of %s: " % items[item_selection - 1]["name"])
                if qty > 0:
                    cart.append({
                        "id": items[item_selection - 1]["id"],
                        "name": items[item_selection - 1]["name"],
                        "qty": qty
                    })
        elif item_selection == 0:
            return
        
        elif item_selection != -1:
            print("Invalid item")

def edit_scanned_items():
    print("\nEdit Items")

    for index, item in enumerate(cart):
        print("[%i] %s: %i" % (index + 1, item["name"], item["qty"]))

    print("\n[0] End Edit\n")

    done = False
    while not done:
        item_selection = get_input("Edit Item: ")

        if item_selection > 0 and item_selection <= len(cart):
            new_qty = get_input("Update %s quantity to: " % cart[item_selection - 1]["name"])
            
            if new_qty == 0:
                del cart[item_selection - 1]
            elif new_qty > 0:
                cart[item_selection - 1]["qty"] = new_qty

            view_scanned_items()

        elif item_selection == 0:
            return


def view_scanned_items():
    print("\nScanned Items")

    for item in cart:
        print("%s: %i" % (item["name"], item["qty"]))

    print()

def generate_receipt():
    global cart

    if len(cart) == 0:
        return
    else:
        computed = compute()
        
    store_name = "BILLING SYSTEM"
    quantity = "Quantity"
    item = "Item"
    price = "Price"
    discountStr = "Discount"
    vatStr = "Value Added Tax"
    totalStr = "TOTAL"
    subtotalStr = "Subtotal"
    tenderedStr = "Tendered Amount"
    changeStr = "Change"

    invoice = "Inovoice No." + str(random.randrange(1000000000,9999999999))

    subtotal = computed["subtotal"]
    discount = computed["discount"]
    vat = computed["vat"]
    total = computed["total"]
    tendered = computed["tendered"]
    change = computed["change"]

    print("==================================================")
    print(f"{store_name:^50}")
    print(f"{invoice:^50}")
    print("==================================================")
    print(f"{quantity:<10}{item:^30}{price:>10}")
    
    for i in cart:
        quantity = i["qty"]
        item = i["name"]
        for x in items:
            if i["id"] == x["id"]:
                price = x["unit_price"] * quantity
            
        print(f"{quantity:<10}{item:^30}{price:>10}")
    print(f"\n{subtotalStr:<40}{subtotal:>10}")
    print(f"{discountStr:<40}{discount:>10}")
    print(f"{vatStr:<40}{vat:>10}")
    print(f"{totalStr:<40}{total:>10}")
    print("==================================================")
    print(f"{tenderedStr:<40}{tendered:>10}")
    print(f"{changeStr:<40}{change:>10}")
    print("==================================================")

    cart = []

# SUB HELPER
def findItem(item_selection):
    if len(cart) > 0:
        for index, item in enumerate(cart):
            if item["name"] == items[item_selection - 1]["name"]:
                return index
            
    return -1

def compute():
    subtotal = 0.0
    apply_discount = get_input("Apply Discount (%): ")
    discount = round(apply_discount / 100, 3)
    vat = 0.0

    for i in cart:
        quantity = i["qty"]

        for x in items:
            if i["id"] == x["id"]:
                price = x["unit_price"] * quantity
                subtotal += price

    discount = subtotal * discount
    discounted_amount = subtotal - discount
    vat = round(discounted_amount * .12, 3)
    total = round(discounted_amount + vat, 3)

    amount_tendered = 0
    while amount_tendered < total:
        amount_tendered = get_amount("Amount Tendered: ")

    change = round(amount_tendered - total, 3)

    return {"discount": discount, "subtotal": subtotal, "vat": vat, "total": total, "tendered":amount_tendered, "change": change}

if __name__ == '__main__':
    global cart

    cart = []

    main()