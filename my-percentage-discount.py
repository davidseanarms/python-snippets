def my_discount():
  price = float(input("What is the original price of the product? "))
  discount_percentage = float(input("What is the % discount ? "))

  discount_amount = price * (discount_percentage/100)
  price_after_discount = price - discount_amount

  return price_after_discount

print(my_discount())
