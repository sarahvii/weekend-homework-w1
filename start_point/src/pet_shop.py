# WRITE YOUR FUNCTIONS HERE

# I've added comments after some of my solutions

def get_pet_shop_name(name_of_petshop):
    return name_of_petshop["name"]

def get_total_cash(cash_held_by_admin):
    return cash_held_by_admin["admin"]["total_cash"]

def add_or_remove_cash(cash_held_by_admin, cash):
    cash_held_by_admin["admin"]["total_cash"] += cash

# Feet very lost with add_or_remove_cash.  Could not move beyond this item without help.

def get_pets_sold(number):
    return number["admin"]["pets_sold"]

# is this right? 

def increase_pets_sold(number, increased_number):
    number["admin"]["pets_sold"] += increased_number

# Why is return not needed here?

def get_stock_count(stock):
    return len(stock["pets"])

# Figured this one out really quickly - not all hope is lost!

def get_pets_by_breed(pet_shop, breed_name):
    breed_collection = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            breed_collection.append(pet["breed"])
    return breed_collection

# Really struggled with this one. I knew what I wanted the code to do, but struggled to make it work.

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        
# Took a while.

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet): 
    pet_shop["pets"].append(new_pet)

# Is this all that is needed?

def get_customer_cash(customer_cash):
    return customer_cash["cash"]

def remove_customer_cash(customer_cash, amount_removed):
    customer_cash["cash"] -= amount_removed

# This took a long time. I'm not clear on when 'return' etc should be used and when not

def get_customer_pet_count(customer_in_list):
    return len(customer_in_list["pets"])

# figured this out quickly but not convinced I fully understand why

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])

# --- OPTIONAL --- 





    




    



