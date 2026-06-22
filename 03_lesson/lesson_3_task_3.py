from address import Address
from mailing import Mailing

# Создаём адреса
to_address = Address("123456", "Москва", "Тверская", "15", "45")
from_address = Address("654321", "Санкт-Петербург", "Невский", "10", "12")

# Создаём почтовое отправление
mailing = Mailing(to_address, from_address, 350.50, "ABC123456789")

# Вывод в требуемом формате
print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.city}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)