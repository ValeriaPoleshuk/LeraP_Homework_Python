class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index #индекс
        self.city = city #город
        self.street = street #улица
        self.house = house #дом
        self.apartment = apartment #квартира

    def __str__(self):
        return f"{self.index}, {self.city}, {self.street}, {self.house} - {self.apartment}"