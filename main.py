#   A simple script to calculate the gst on a fixed invoice amount
#   Idea being to get the total amount and then work out what the net would
#   be before the gst is added to get the total

#   This method is used to get the gst component from the gross price
def __calculate_gst_amount(gross_amount: float) -> float:
    gst_inclusive_multiplier = 1.10

    return gross_amount - (gross_amount / gst_inclusive_multiplier)

#   This method is used to get the purchase price from the user
def __get_purchase_price() -> float:
    return __get_float_input_from_user("What was the purchase price of the item? ")

# This method gets a valid float input from the user
def __get_float_input_from_user(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

purchase_price = __get_purchase_price()
gst_amount = __calculate_gst_amount(purchase_price)
net_amount = purchase_price - gst_amount

print(f"Total: ${purchase_price:.2f}")
print(f"GST: ${gst_amount:.2f}")
print(f"Net: ${net_amount:.2f}")