def display_menu(sizes, toppings):
    print("PIZZA BILL GENERATOR")
    
    print("\n--- Available Sizes ---")
    for size, price in sizes.items():
        print(f"{size.title()}: ₹{price:.2f}")
        
    print("\n--- Available Toppings ---")
    for topping, price in toppings.items():
        print(f"{topping.title()}: ₹{price:.2f}")
   

def main():
    pizza_sizes = {
        "small": 99,
        "medium": 199,
        "large": 299,
        "family": 499
    }

    available_toppings = {
        "capcicum": 30,
        "mushrooms": 40,
        "onions": 20,
        "olives": 30,
        "corn": 30,
        "extra cheese": 40,
        "jalapeno": 40
    }

    display_menu(pizza_sizes, available_toppings)

    selected_size = ""
    while selected_size not in pizza_sizes:
        user_input = input("Choose a pizza size: ").lower().strip()
        if user_input in pizza_sizes:
            selected_size = user_input
        else:
            print("Invalid size. Please choose from Small, Medium, Large, or Family.")

    total_cost = pizza_sizes[selected_size]
    order_list = []

    print(f"\nSelected {selected_size.title()} pizza (Base price: ₹{total_cost:.2f})")
    print("Type the topping name to add it. Type 'done' when finished.")

    while True:
        topping_input = input("\n Add topping: ").lower().strip()

        if topping_input == 'done':
            break
        
        if topping_input in available_toppings:
            cost = available_toppings[topping_input]
            total_cost += cost
            order_list.append(topping_input)
            print(f"+ Added {topping_input.title()} (+₹{cost:.2f})")
        else:
            print("Topping not found in menu. Try again.")

    print("\n" + "-"*30)
    print("ORDER SUMMARY")
    print("-"*30)
    print(f"Pizza Size: {selected_size.title()} (₹{pizza_sizes[selected_size]:.2f})")
    
    if order_list:
        print("\nToppings:")
        for item in order_list:
            print(f" - {item.title()} (₹{available_toppings[item]:.2f})")
    else:
        print("\nToppings: None (Cheese Only)")

    print("-"*30)
    print(f"TOTAL PRICE: ₹{total_cost:.2f}")
    print("-"*30)
    
main()