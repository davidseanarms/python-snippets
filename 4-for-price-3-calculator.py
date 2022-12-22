def FourForThreeDiscount(products):
    cheapest_product = min(products)
    total_cost = sum(products)
    discounted_cost = total_cost - cheapest_product
    discount_percent = (1 - (discounted_cost / total_cost)) * 100
    discount_amount = total_cost - discounted_cost
    avg_cost_per_product = discounted_cost / 3
    print("What you pay: $", discounted_cost)
    print("One item costs on average: $", avg_cost_per_product)
    print("Your saving in $ form: $", discount_amount)

p1 = float(input("Enter the price of the first product: "))
p2 = float(input("Enter the price of the second product: "))
p3 = float(input("Enter the price of the third product: "))
p4 = float(input("Enter the price of the fourth product: "))
FourForThreeDiscount([p1, p2, p3, p4])
