import Mailing
import Address

addr_otp = Address.Address(344258, "Санкт-Петербург", "ул Генерала Хрулёва", 35, 11)
addr_pol = Address.Address(255144, "Москва", "Воробьевы Горы", 24,14)
mail_1 = Mailing.Mailing(addr_otp, addr_pol, 5000, 'sm001-ph-001t')

print(
    f"Отправление: {mail_1.track} "
    f"из {mail_1.from_address.index}, {mail_1.from_address.city}, "
    f"{mail_1.from_address.street}, д. {mail_1.from_address.house}, "
    f"кв. {mail_1.from_address.flat} "
    f"в {mail_1.to_address.index}, {mail_1.to_address.city}, "
    f"{mail_1.to_address.street}, д. {mail_1.to_address.house}, "
    f"кв. {mail_1.to_address.flat}. Стоимость: {mail_1.cost} рублей."
)