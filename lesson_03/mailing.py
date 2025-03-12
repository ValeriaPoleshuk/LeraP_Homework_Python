class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address # адрес получчателя
        self.from_address = from_address #адрес отправителя
        self.cost = cost #стоимость отправления
        self.track = track #трек-номер отправления

    def __str__(self):
            return (f"Отправление {self.track} из {str(self.from_address)} в {str(self.to_address)}. "
                    f"Стоимость {self.cost} рублей.")

    to_address = Address("123456", "Москва", "Ленина", "10", "15")
    from_address = Address("654321", "Санкт-Петербург", "Невский", "25", "7")

    mailing = Mailing(to_address, from_address, 500, "ABC123456789")


    print(mailing)
