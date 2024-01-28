# Constants
PIZZA_PRICE = 12.00
TUESDAY_DISCOUNT = 0.5
DELIVERY_CHARGE = 2.50
FREE_DELIVERY = 5
APP_DISCOUNT = 0.25

def get_positive_integer_input(prompt):
    """Get a positive integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_no_input(prompt):
    """Get a yes/no input from the user."""
    while True:
        answer = input(prompt).lower()
        if answer in ['y', 'n']:
            return answer
        else:
            print('Please answer "Y" or "N".')

def calculate_order_price(num_pizzas, is_tuesday, use_delivery, use_app):
    """Calculate and return the total price for the order."""
    # Calculate pizza subtotal with Tuesday discount
    pizza_subtotal = num_pizzas * PIZZA_PRICE * (1 - TUESDAY_DISCOUNT) if is_tuesday else num_pizzas * PIZZA_PRICE

    # Calculate delivery charge (if applicable)
    delivery_charge = DELIVERY_CHARGE if use_delivery and num_pizzas < FREE_DELIVERY else 0

    # Calculate order total and apply app discount
    order_total = (pizza_subtotal + delivery_charge) * (1 - APP_DISCOUNT) if use_app else pizza_subtotal + delivery_charge

    # Round total to two decimal places
    order_total = round(order_total, 2)

    return order_total

def main():
    """ Shows the BPP Pizza Price Calculator program."""
    print("BPP Pizza Price Calculator\n==========================\n")

    # Get user input
    num_pizzas = get_positive_integer_input("How many pizzas ordered? ")
    use_delivery = get_yes_no_input("Is delivery required? ")
    is_tuesday = get_yes_no_input("Is it Tuesday? ")
    use_app = get_yes_no_input("Did the customer use the app? ")

    # Calculate and display total price
    order_total = calculate_order_price(num_pizzas, is_tuesday == 'y', use_delivery == 'y', use_app == 'y')
    print(f"\nTotal Price: £{order_total:.2f}.")

if __name__ == "__main__":
    main()
