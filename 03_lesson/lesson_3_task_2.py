import Smartphone

catalog = \
[
    Smartphone.Smartphone("RealMi","13+PRO","99677770707"),
    Smartphone.Smartphone("Samsung", "Galaxy S24", "9990002525"),
    Smartphone.Smartphone("Google", "Pixel 8", "9910010022"),
    Smartphone.Smartphone("Xiaomi", "13T", "9119992511"),
    Smartphone.Smartphone("OneHell", "999", "9996669666")
]

for phone in catalog:
    print(phone)
