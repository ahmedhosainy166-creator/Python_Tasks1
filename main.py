# task 1

print("Welcom to Instant Discount System ")

amount = float(input("Enter your Value of purchases :"))
if amount < 100: 
    Discount = 0
elif amount >= 100 and amount < 500 :
    Discount = 0.10
else:
    Discount = 0.20

discount_amount = amount * Discount
final_price =  amount - discount_amount

print(f"Your discount value is: {discount_amount} and The amount due after the discount is: {final_price} ")