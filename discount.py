# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher, apply it
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the final price
    if final_price == price:
        print(f"No discount applied. The original price is: ${price:.2f}")
    else:
        print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for price and discount percentage.")
