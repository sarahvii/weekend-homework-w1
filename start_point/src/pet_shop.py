# WRITE YOUR FUNCTIONS HERE

# Comments after solutions

def get_pet_shop_name(name_of_petshop):
    return name_of_petshop["name"]

def get_total_cash(cash_held_by_admin):
    return cash_held_by_admin["admin"]["total_cash"]

def add_or_remove_cash(cash_held_by_admin, cash):
    cash_held_by_admin["admin"]["total_cash"] += cash

# Felt very lost with add_or_remove_cash.  Could not move beyond this without help.

def get_pets_sold(number):
    return number["admin"]["pets_sold"]

# Passes but is this all that is needed? 

def increase_pets_sold(number, increased_number):
    number["admin"]["pets_sold"] += increased_number

def get_stock_count(stock):
    return len(stock["pets"])

def get_pets_by_breed(pet_shop, breed_name):
    breed_collection = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            breed_collection.append(pet["breed"])
    return breed_collection

# Really struggled with this one.

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

def get_customer_cash(customer_cash):
    return customer_cash["cash"]

def remove_customer_cash(customer_cash, amount_removed):
    customer_cash["cash"] -= amount_removed

# This took a long time. I was looking to 'return' something.

def get_customer_pet_count(customer_in_list):
    return len(customer_in_list["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])

# --- OPTIONAL ---

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] - new_pet["price"] >= 0:
        return True
    else:
        return False
    
# def sell_pet_to_customer(pet_shop, pet, customer):

# #  LOST!
    





    




    



