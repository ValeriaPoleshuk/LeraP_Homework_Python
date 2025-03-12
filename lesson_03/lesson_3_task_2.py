from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy", "+79297239272" ),
    Smartphone("Apple", "iPhone_15", "+79297274298" ),
    Smartphone("Huawei", "12SE", "+79227219061"),
    Smartphone("Redmi", "A91", "+79615208112"),
    Smartphone("Xiaomi", "SU7", "+79061194437")
]

for smartphone in catalog:
    print(f"{smartphone.make}, {smartphone.type}, {smartphone.phone_number}")
