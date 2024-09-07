def calculate_discount(price, discount_percentage):
    if discount_percentage >=20:
        discount_amount=(discount_percentage/100)*price
        final_price=price-discount_amount
        return final_price
    
    else:
        return price
    
original_price=float(input("Enter the original price:"))
discount_percentage=float(input("Enter the discount percentage:"))

final_price=calculate_discount(original_price, discount_percentage)

if final_price !=original_price:
    print("The final price after the discount is:", final_price)

else:
    print(f"No discount applied.The original price is:")