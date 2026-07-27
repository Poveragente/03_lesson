import smartphone

catalog = \
[
    smartphone.smartphone("RealMi","13+PRO","+799677770707"),
    smartphone.smartphone("Samsung", "Galaxy S24", "+79990002525"),
    smartphone.smartphone("Google", "Pixel 8", "+79910010022"),
    smartphone.smartphone("Xiaomi", "13T", "+79119992511"),
    smartphone.smartphone("OneHell", "999", "+79996669666")
]

for phone in catalog:
    print(phone)
