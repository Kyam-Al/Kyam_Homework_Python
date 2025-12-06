from lesson_3.address import Address
from lesson_3.mailing import Mailing

from_address = Address("123456", "Москва", "Тверская", "10", "25")
to_address = Address("654321", "Санкт-Петербург", "Невский", "20", "50")

mailing = Mailing(to_address, from_address, 500.50, "TRACK12345ABC")

output_string = (
    f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)

print(output_string)