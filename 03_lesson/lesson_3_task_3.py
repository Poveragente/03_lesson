import mailing
import address

addr_otp = address.address(344258, "Санкт-Петербург", "ул Генерала Хрулёва", 35, 11)
addr_pol = address.address(255144, "Москва", "Воробьевы Горы", 24,14)
mail_1 = mailing.mailing(addr_otp, addr_pol, 5000, 'sm001-ph-001t')

print(
    f"Отправление: {mail_1.track} "
    f"из {mail_1.from_address.index}, {mail_1.from_address.city}, "
    f"{mail_1.from_address.street}, {mail_1.from_address.house}, "
    f" {mail_1.from_address.flat} "
    f"в {mail_1.to_address.index}, {mail_1.to_address.city}, "
    f"{mail_1.to_address.street},  {mail_1.to_address.house}, "
    f" {mail_1.to_address.flat}. Стоимость: {mail_1.cost} рублей."
)