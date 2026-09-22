price = float(input("price="))
discount = float(input("discount="))
vat = float(input("vat="))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print("База после скидки: " + str(f"{base:.2f}") + " ₽")
print("НДС: " + str(f"{vat_amount:.2f}") + " ₽")
print("Итого к оплате: " + str(f"{total:.2f}") + " ₽")