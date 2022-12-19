import zebra
import smtplib
barcode = input("Enter the barcode or barcode number to search for a product: ")
inventory = zebra.Zebra().check_inventory(barcode)
message = f"The product with barcode {barcode} has {inventory} in stock in the warehouse."
server = smtplib.SMTP('smtp.store.name', 587)
server.starttls()
server.login("inventory@store.name", "password")
server.sendmail("inventory@store.name", "inventory@store.name", message)
server.quit()
