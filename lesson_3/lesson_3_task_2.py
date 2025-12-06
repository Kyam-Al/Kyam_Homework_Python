from lesson_3.smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Samsung", "Galaxy S23", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79998887766"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79001112233"))
catalog.append(Smartphone("Google", "Pixel 7", "+79223334455"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+79335556677"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
