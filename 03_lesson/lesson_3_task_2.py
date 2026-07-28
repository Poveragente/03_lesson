import smartphone

catalog = \
[
    smartphone.Smartphone("RealMi","13+PRO","+799677770707"),
    smartphone.Smartphone("Samsung", "Galaxy S24", "+79990002525"),
    smartphone.Smartphone("Google", "Pixel 8", "+79910010022"),
    smartphone.Smartphone("Xiaomi", "13T", "+79119992511"),
    smartphone.Smartphone("OneHell", "999", "+79996669666")
]

for phone in catalog:
    print(phone)
