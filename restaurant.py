# ======= FRAME DEFINITIONS =======

# Menu items stored as frames (dictionaries)
menu = {
    "Grilled Chicken": {
        "ingredients": ["chicken", "oil", "spices"],
        "price": 850,
        "type": "main"
    },
    "Beef Stew": {
        "ingredients": ["beef", "milk", "spices"],
        "price": 950,
        "type": "main"
    },
    "Veggie Pasta": {
        "ingredients": ["pasta", "tomato", "cheese"],
        "price": 780,
        "type": "main"
    }
}

# Customer data frame
customer = {
    "name": "Etemesi",
    "allergies": ["dairy"],
    "type": "new"
}

# Time of day for special suggestions
current_time = "lunch"  # Options: breakfast, lunch, dinner


# ======= PRODUCTION RULES =======

def suggest_specials(customer, time):
    if time == "lunch" and customer["type"] == "new":
        print(
            f"👨‍🍳 Suggestion for {customer['name']}: Try our lunch special - Veggie Pasta 🍝")


def allergy_check(customer, dish_name):
    dish = menu[dish_name]
    for allergen in customer["allergies"]:
        for ingredient in dish["ingredients"]:
            if allergen in ingredient:
                print(
                    f"⚠️ Allergy Alert: {customer['name']} is allergic to {allergen} in {dish_name}")
                return False
    return True


def recommend_dish(customer):
    print(
        f"\n🧠 Inference Engine: Finding safe dishes for {customer['name']}...")
    for dish_name in menu:
        if allergy_check(customer, dish_name):
            print(
                f"✅ Recommended: {dish_name} - KSh {menu[dish_name]['price']}")
        else:
            print(f"⛔ Skipped: {dish_name}")
    print()


# ======= INFERENCE ENGINE EXECUTION =======

print("🍽️ Welcome to AI Restaurant Expert System!\n")
suggest_specials(customer, current_time)
recommend_dish(customer)

# ======= END OF PROGRAM =======
print("Thank you for visiting! Enjoy your meal! 🍴")
